
import cv2
from ultralytics import YOLO

# Load the pretrained YOLO model
model = YOLO("yolo26n.pt")

# Objects relevant to our prosthetic
target_objects = [
    "bottle",
    "cup",
    "apple",
    "orange",
    "sports ball",
    "spoon",
    "fork"
]

# Find the class IDs corresponding to our objects
target_classes = [
    class_id
    for class_id, name in model.names.items()
    if name in target_objects
]

# Open the laptop webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    raise RuntimeError("Could not open webcam.")

print("Camera started! Press Q to quit.")

try:
    while True:
        # Capture a frame
        success, frame = camera.read()

        if not success:
            print("Failed to capture frame.")
            break

        # Run object detection
        results = model.predict(
            frame,
            conf=0.40,
            imgsz=640,
            classes=target_classes,
            device="cpu",
            verbose=False
        )

        # Draw the detected objects
        annotated_frame = results[0].plot()

        # Display the live camera feed
        cv2.imshow(
            "Prosthetic Vision - YOLO",
            annotated_frame
        )

        # Press Q to close the program
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    # Release webcam and close window
    camera.release()
    cv2.destroyAllWindows()