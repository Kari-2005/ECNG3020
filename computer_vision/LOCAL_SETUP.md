# Windows VS Code Local Setup

The **repository** tracks documentation and source. The **SSD project workspace** also holds large datasets, model files, experiment runs and a Python virtual environment. These local folders need not be pushed.

Suggested local structure:

```text
computer_vision/
  .venv-vyonix/
  test_social_gestures.py                  # original tested script
  scripts/testing/test_social_gestures.py
  models/gesture_recognizer.task
  models/yolo26n.pt
  models/yolov8s-world.pt
  runs/prosthetic_14class_pilot/weights/best.pt
  runs/prosthetic_5class_v1-2/weights/best.pt
  datasets/5cat_prostheticobjects/data.yaml
```

Run from `computer_vision` in PowerShell:

```powershell
py -m venv .venv-vyonix
.\.venv-vyonix\Scripts\python.exe -m pip install -r requirements-vision.txt
.\.venv-vyonix\Scripts\python.exe scripts\testing\test_social_gestures.py
```

Download the [MediaPipe Gesture Recognizer task model](https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task) into `models/gesture_recognizer.task` before running the gesture demo.

Your original YOLO training and test scripts were developed before this repository layout, and should be tested with path corrections against the corresponding actual local dataset and model files before treating them as runnable from this tree.

No re-training is necessary to **test** the saved five-class checkpoint, assuming the checkpoint is available locally.
The [original tested social gesture script](test_social_gestures.py) may also be run using ` .\\.venv-vyonix\\Scripts\\python.exe test_social_gestures.py` from this folder. Both script locations require `models/gesture_recognizer.task`.
