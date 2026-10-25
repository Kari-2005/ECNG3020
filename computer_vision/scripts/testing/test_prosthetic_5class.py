
from pathlib import Path
import cv2
from ultralytics import YOLO

# Main project folder
project = Path(__file__).resolve().parent

# Load the best trained five-class model
model_path = (
    project / "runs"
    / "prosthetic_5class_v1-2"
    / "weights"
    / "best.pt"
)

if not model_path.is_file():
    raise FileNotFoundError(f"Model not found: {model_path}")

model = YOLO(str(model_path))

print("ECNG3020 - Five-class prosthetic vision")
print("Classes:", model.names)
print("Press Q to exit.")

# Open Vyonix webcam
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not camera.isOpened():
    raise RuntimeError("Could not open webcam.")

try:
    while True:
        success, frame = camera.read()

        if not success:
            print("Unable to read camera frame.")
            break

        # Perform object detection
        results = model.predict(
            source=frame,
            conf=0.40,
            iou=0.50,
            imgsz=416,
            device="cpu",
            verbose=False
        )

        # Draw predictions on camera frame
        annotated = results[0].plot()

        cv2.imshow(
            "ECNG3020 - Prosthetic Vision (5 Classes)",
            annotated
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    camera.release()
    cv2.destroyAllWindows()