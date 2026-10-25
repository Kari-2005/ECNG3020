from pathlib import Path
from collections import deque, Counter
import time

import cv2
import mediapipe as mp

# Project folders
project = Path(__file__).resolve().parent
model_path = project / "models" / "gesture_recognizer.task"

if not model_path.is_file():
    raise FileNotFoundError(
        f"Gesture model not found: {model_path}"
    )

# MediaPipe configuration
BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
RunningMode = mp.tasks.vision.RunningMode

options = GestureRecognizerOptions(
    base_options=BaseOptions(
        model_asset_path=str(model_path)
    ),
    running_mode=RunningMode.VIDEO,
    num_hands=1
)

# Webcam
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not camera.isOpened():
    raise RuntimeError("Could not open webcam.")

# Require consistent recognition over several frames
history = deque(maxlen=7)
last_timestamp = -1

print("ECNG3020 - Social Gesture Recognition")
print("Open palm = High-five candidate")
print("Closed fist = Fist-bump candidate")
print("Thumbs up = Thumbs-Up candidate")
print("Press Q to quit.")

try:
    with GestureRecognizer.create_from_options(options) as recognizer:
        while True:
            success, frame = camera.read()

            if not success:
                break

            # Flip for a mirror-style display
            frame = cv2.flip(frame, 1)

            # Convert OpenCV BGR image into RGB
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(
                image_format=mp.ImageFormat.SRGB,
                data=rgb
            )

            # Video timestamps must increase
            timestamp = max(
                int(time.monotonic() * 1000),
                last_timestamp + 1
            )
            last_timestamp = timestamp

            result = recognizer.recognize_for_video(
                mp_image, timestamp
            )

            gesture = "None"
            confidence = 0.0

            if result.gestures and result.gestures[0]:
                top = result.gestures[0][0]
                gesture = top.category_name
                confidence = top.score

            # Accept only sufficiently confident gestures
            if confidence < 0.65:
                gesture = "None"

            if gesture == "Open_Palm":
                candidate = "HIGH FIVE"
            elif gesture == "Closed_Fist":
                candidate = "FIST BUMP"
            elif gesture == "Thumb_Up":
                candidate = "THUMBS UP"
            else:
                candidate = "NONE"

            history.append(candidate)

            # Require at least 5 matching results
            counts = Counter(history)
            interaction = "NO GESTURE"

            if counts["HIGH FIVE"] >= 5:
                interaction = "HIGH FIVE"
            elif counts["FIST BUMP"] >= 5:
                interaction = "FIST BUMP"
            elif counts["THUMBS UP"] >= 5:
                interaction = "THUMBS UP"

            # Draw hand landmarks
            if result.hand_landmarks:
                for hand in result.hand_landmarks:
                    h, w = frame.shape[:2]

                    for point in hand:
                        x = int(point.x * w)
                        y = int(point.y * h)

                        cv2.circle(
                            frame, (x, y), 3,
                            (0, 255, 255), -1
                        )

            # Display status
            color = (0, 255, 0) if interaction != "NO GESTURE" else (255, 255, 255)

            cv2.putText(
                frame,
                interaction,
                (25, 55),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.1,
                color,
                3
            )

            cv2.putText(
                frame,
                f"Raw: {gesture} ({confidence:.2f})",
                (25, 95),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2
            )

            cv2.imshow(
                "ECNG3020 - Social Gesture Test",
                frame
            )

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

finally:
    camera.release()
    cv2.destroyAllWindows()
