# Local model assets

Keep model weights and `.task` assets in the local workspace; they are not part of this GitHub documentation upload.

Expected local examples:
- `models/gesture_recognizer.task` — [official MediaPipe asset](https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task)
- `models/yolo26n.pt` — pretrained YOLO baseline
- `models/yolov8s-world.pt` — pretrained YOLO-World baseline
- `runs/prosthetic_14class_pilot/weights/best.pt` — completed 14-class experiment
- `runs/prosthetic_5class_v1-2/weights/best.pt` — completed 5-class experiment

Do not commit `.venv-vyonix`, raw datasets or large checkpoint archives. Confirm redistribution terms before publishing external model weights.