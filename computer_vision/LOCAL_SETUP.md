# Running the Computer Vision Tests in VS Code (Windows)

I keep the working datasets and trained weights on my SSD because they are too large for the normal GitHub repository. The GitHub files mainly contain the notes and Python code.

## Folder layout for the social gesture test

```text
computer_vision/
  .venv-vyonix/
  test_social_gestures.py       # original script that I tested
  scripts/
    testing/
      test_social_gestures.py   # copy with adjusted model path
  models/
    gesture_recognizer.task
    yolo26n.pt
    yolov8s-world.pt
  runs/
    prosthetic_14class_pilot/
      weights/best.pt
    prosthetic_5class_v1-2/
      weights/best.pt
  datasets/
    5cat_prostheticobjects/
      data.yaml
```

## Set up Python

Open a terminal inside `computer_vision`, then run:

```powershell
py -m venv .venv-vyonix
.\.venv-vyonix\Scripts\python.exe -m pip install -r requirements-vision.txt
```

Download [MediaPipe's gesture recognizer model](https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task) and save it as `models/gesture_recognizer.task`.

## Try the three gestures

Use the **original** version:

```powershell
.\.venv-vyonix\Scripts\python.exe test_social_gestures.py
```

Or the version stored under `scripts/testing`:

```powershell
.\.venv-vyonix\Scripts\python.exe scripts\testing\test_social_gestures.py
```

Open palm should show **HIGH FIVE**, closed fist should show **FIST BUMP** and thumbs up should show **THUMBS UP**. Press **Q** when finished.

## Other experiments

The saved five-class checkpoint goes under `runs/prosthetic_5class_v1-2/weights/best.pt`. It does not need another training run just for testing.

Other original training and testing scripts were developed with older SSD paths. Those paths should be checked against the local folder arrangement before trying to run them from this repository.
