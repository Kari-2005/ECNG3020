"""ECNG3020 social gesture demo: webcam recognition only; NO motor control."""
from pathlib import Path
from collections import Counter, deque
import time
import cv2
import mediapipe as mp

PROJECT = Path(__file__).resolve().parents[2]
MODEL = PROJECT / "models" / "gesture_recognizer.task"
if not MODEL.is_file():
    raise FileNotFoundError(
        f"Missing MediaPipe model: {MODEL}\n"
        "Download gesture_recognizer.task and place it in the models directory."
    )

options = mp.tasks.vision.GestureRecognizerOptions(
    base_options=mp.tasks.BaseOptions(model_asset_path=str(MODEL)),
    running_mode=mp.tasks.vision.RunningMode.VIDEO,
    num_hands=1,
)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    raise RuntimeError("Could not open webcam.")

history = deque(maxlen=7)
last_timestamp = -1

print("ECNG3020 — High-five, fist bump and thumbs-up detection")
print("Press Q to exit. No servo commands are sent.")

try:
    with mp.tasks.vision.GestureRecognizer.create_from_options(options) as recognizer:
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
            timestamp = max(int(time.monotonic() * 1000), last_timestamp + 1)
            last_timestamp = timestamp

            result = recognizer.recognize_for_video(image, timestamp)
            raw = "None"
            confidence = 0.0
            if result.gestures and result.gestures[0]:
                top = result.gestures[0][0]
                raw, confidence = top.category_name, top.score
            if confidence < 0.65:
                raw = "None"

            names = {"Open_Palm": "HIGH FIVE", "Closed_Fist": "FIST BUMP",
                     "Thumb_Up": "THUMBS UP"}
            history.append(names.get(raw, "NONE"))
            counts = Counter(history)
            interaction = "NO GESTURE"
            for label in ("HIGH FIVE", "FIST BUMP", "THUMBS UP"):
                if counts[label] >= 5:
                    interaction = label
                    break

            h, w = frame.shape[:2]
            for hand in result.hand_landmarks or []:
                for point in hand:
                    cv2.circle(frame, (int(point.x * w), int(point.y * h)),
                               3, (0, 255, 255), -1)
            green = (0, 255, 0) if interaction != "NO GESTURE" else (255, 255, 255)
            cv2.putText(frame, interaction, (25, 55),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.1, green, 3)
            cv2.putText(frame, f"Raw: {raw} ({confidence:.2f})", (25, 95),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            cv2.imshow("ECNG3020 - Social Gesture Test", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
finally:
    cap.release()
    cv2.destroyAllWindows()
