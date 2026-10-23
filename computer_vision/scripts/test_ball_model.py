"""Two-class ball/apple webcam test; report measurements separately."""
import cv2
from pathlib import Path
from ultralytics import YOLO

project = Path(__file__).resolve().parents[1]
model = YOLO(str(project / "runs" / "tennis_apple_pilot" / "weights" / "best.pt"))
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    raise RuntimeError("Could not open webcam")
try:
    while True:
        ok, frame = camera.read()
        if not ok:
            break
        result = model.predict(frame, conf=0.40, imgsz=416, device="cpu", verbose=False)[0]
        cv2.imshow("Tennis Ball vs Apple", result.plot())
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    camera.release()
    cv2.destroyAllWindows()
