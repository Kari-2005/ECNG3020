# Computer Vision — ECNG3020

This folder is where I'm keeping the computer vision side of my final year robotic prosthetic project. I started by testing pretrained object detection models, then moved into training my own models for objects I wanted the hand to recognize. I also tried MediaPipe to identify simple hand gestures.

## What I've done so far

| Experiment | What I tried | Progress |
|---|---|---|
| [01 — Initial YOLO](experiments/01_initial_yolo/README.md) | Testing YOLO26n with my webcam | Tested |
| [02 — YOLO-World](experiments/02_yolo_world/README.md) | Trying object names without training my own model | Tested |
| [03 — Tennis ball and apple](experiments/03_tennis_ball_apple/README.md) | My first two-class trained model | Tested |
| [04 — 14-class model](experiments/04_14class_pilot/README.md) | Training on more everyday objects | Trained, but webcam detection needed improvement |
| [05 — 5-class model](experiments/05_5class_model/README.md) | Narrowing the model to bottle, tennis ball, pen, bag and phone | Trained and tested |
| [06 — Social gestures](experiments/06_social_gestures/README.md) | Recognizing a high-five, fist bump and thumbs up | All three detected in webcam tests |

## Social gesture recognition

I wanted the hand to be able to respond to more than just physical objects, so I tested whether a camera could recognize someone giving a high-five or fist bump. I used MediaPipe's gesture recognizer instead of training another YOLO model.

The first version recognized an open palm and a closed fist. I then added a thumbs-up gesture, and all three worked during my webcam tests.

| Detected hand gesture | Label shown |
|---|---|
| Open palm | HIGH FIVE |
| Closed fist | FIST BUMP |
| Thumbs up | THUMBS UP |

I'm keeping [my original working script](test_social_gestures.py) here. There is also a [copy adapted for the organized scripts folder](scripts/testing/test_social_gestures.py). The original expects the `models` folder to be beside it.

These are still webcam tests only. The code does not move any servos, and recognizing a hand shape doesn't prove that someone actually wants a high-five or fist bump.

## Where to look

- [All experiments](experiments/README.md)
- [Experiment 06 — how the three gestures were tested](experiments/06_social_gestures/README.md)
- [Original social gesture code](test_social_gestures.py)
- [Datasets and sources](datasets/README.md)
- [Local VS Code setup](LOCAL_SETUP.md)
- [Plans for connecting vision to the prosthetic](integration_plan.md)

## Earlier notes

I kept the earlier logs because I still want to show what I originally tried, even where my approach later changed:

- [Log 001 — Setup](docs/development_log_001.md)
- [Log 002 — YOLO26n webcam baseline](docs/development_log_002.md)
- [Log 003 — YOLO-World](docs/development_log_003.md)
- [Log 004 — Tennis ball and apple](docs/development_log_004.md)
- [Log 005 — Building the 14-class dataset](docs/development_log_005.md)
- [Early vision system overview](docs/vision_system_overview.md)

Some early notes describe plans that have since changed. The experiment pages above are the more recent record.

## Next steps

I still need to test both the object model and MediaPipe together, see how well they run on a Raspberry Pi 5 and work on connecting the output to the ESP32-S3. EMG confirmation and safe motion limits will be needed before the prosthetic actually moves in response to a detected object or gesture. Handshake recognition is something I might add if there is time.

Large datasets, training checkpoints and the virtual environment are kept outside the GitHub repository for now.
