"""YOLO-World prompt-based webcam evaluation (reconstructed reference)."""
import cv2
from ultralytics import YOLOWorld

model = YOLOWorld("yolov8s-world.pt")
# The prompt list was adjusted in the experiments.
classes = ["water bottle", "cup", "apple", "orange", "tennis ball", "spoon", "fork",
           "pen", "marker", "house key", "grocery bag", "pitcher", "small box"]
model.set_classes(classes)
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    raise RuntimeError("Could not open webcam")
try:
    while True:
        ok, frame = camera.read()
        if not ok:
            break
        result = model.predict(frame, conf=0.25, imgsz=640, device="cpu", verbose=False)[0]
        cv2.imshow("YOLO-World Test", result.plot())
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    camera.release()
    cv2.destroyAllWindows()
