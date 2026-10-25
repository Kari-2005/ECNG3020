
from pathlib import Path
import cv2
from ultralytics import YOLO

# Main project folder
project = Path(__file__).resolve().parent

# Load our trained 14-class model
model_path = (
    project / "runs"
    / "prosthetic_14class_pilot"
    / "weights"
    / "best.pt"
)

if not model_path.exists():
    raise FileNotFoundError(f"Model not found: {model_path}")

model = YOLO(str(model_path))

print("14-class prosthetic vision model loaded!")
print("Diagnostic test: confidence threshold = 0.15")
print("Press Q to quit.")

# Open webcam
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not camera.isOpened():
    raise RuntimeError("Could not open webcam.")

try:
    while True:
        success, frame = camera.read()

        if not success:
            print("Could not read webcam frame.")
            break

        # Diagnostic detection settings
        results = model.predict(
            source=frame,
            conf=0.15,
            imgsz=640,
            device="cpu",
            verbose=False
        )

        # Draw detected objects
        annotated = results[0].plot()

        # Display webcam
        cv2.imshow(
            "ECNG3020 - 14-Class Diagnostic Test",
            annotated
        )

        # Press Q to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    camera.release()
    cv2.destroyAllWindows()