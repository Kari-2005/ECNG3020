"""Initial YOLO26n COCO-category webcam baseline (reconstructed reference)."""
import cv2
from ultralytics import YOLO

model = YOLO("yolo26n.pt")
target_objects = ["bottle", "cup", "apple", "orange", "sports ball", "spoon", "fork"]
target_classes = [i for i, name in model.names.items() if name in target_objects]
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    raise RuntimeError("Could not open webcam")
try:
    while True:
        ok, frame = camera.read()
        if not ok:
            break
        results = model.predict(frame, conf=0.40, imgsz=640, classes=target_classes, device="cpu", verbose=False)
        cv2.imshow("Prosthetic Vision - YOLO", results[0].plot())
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    camera.release()
    cv2.destroyAllWindows()
