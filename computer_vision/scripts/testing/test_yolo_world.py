import cv2
from ultralytics import YOLOWorld

# Load YOLO-World model
model = YOLOWorld("yolov8s-world.pt")

# Define the objects we want it to look for
target_objects = [
    "water bottle",
    "cup",
    "apple",
    "orange",
    "tennis ball",
    "spoon",
    "fork",
    "pen",
    "marker",
    "house key",
    "grocery bag",
    "pitcher",
    "small box"
]

# Set those classes
model.set_classes(target_objects)

# Open webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    raise RuntimeError("Could not open webcam.")

print("YOLO-World running. Press Q to quit.")

try:
    while True:
        success, frame = camera.read()

        if not success:
            print("Failed to capture frame.")
            break

        # Run prediction
        results = model.predict(
            frame,
            conf=0.25,
            imgsz=640,
            device="cpu",
            verbose=False
        )

        # Plot results
        annotated_frame = results[0].plot()

        # Show output
        cv2.imshow("YOLO-World Test", annotated_frame)

        # Quit on Q
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    camera.release()
    cv2.destroyAllWindows()