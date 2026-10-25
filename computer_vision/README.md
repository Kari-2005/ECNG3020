# Computer Vision Subsystem — ECNG3020

This folder documents the development of the computer vision part of my final-year robotic prosthetic hand project. The main idea is to use the camera to identify an object and help decide what type of grasp the hand should use. I have also started looking at simple social interactions, such as recognizing an open palm for a high-five, a closed fist for a fist bump, and a thumbs up.

I wanted to test the vision side separately before trying to connect it to the motors and the EMG system. This made it easier to understand what was and was not working without needing the physical prosthetic to be ready.

## Development process

| Experiment | What I was investigating | Outcome |
|---|---|---|
| [01 — Initial YOLO26n](experiments/01_initial_yolo/README.md) | Whether a pretrained object detector could work through my laptop webcam | Established the first working object-detection test |
| [02 — YOLO-World](experiments/02_yolo_world/README.md) | Recognizing objects by supplying names instead of training a new model | Useful experiment, but I decided to try custom training |
| [03 — Tennis ball and apple](experiments/03_tennis_ball_apple/README.md) | Training a small custom two-class model | First attempt at preparing a dataset and testing trained weights |
| [04 — 14-class pilot](experiments/04_14class_pilot/README.md) | Recognizing a wider range of everyday items | Training worked, but webcam detection had a number of problems |
| [05 — Five-class model](experiments/05_5class_model/README.md) | Improving focus by reducing the number of classes and revising the dataset | Completed a 30-epoch training run and demonstrated all five classes |
| [06 — Social gestures](experiments/06_social_gestures/README.md) | Recognizing an open palm, closed fist and thumbs up | All three gestures appeared correctly in initial webcam tests |

The first five experiments focused on **objects**. Experiment 06 is separate because it uses **hand-gesture recognition**, which could eventually let the prosthetic respond to certain social interactions as well.

## Object detection: what changed between the models

### Early YOLO and YOLO-World tests

I started with YOLO26n pretrained weights to make sure I could get object detection working through a webcam. I then tried YOLO-World because I wanted to see whether I could recognize objects by specifying category names. These tests helped me get familiar with using the models, displaying bounding boxes and working with live camera input.

### First custom model: tennis ball and apple

After the initial tests, I tried training my own two-class model using tennis-ball and apple images. This was mainly to learn how the labeled datasets, training process and testing scripts fit together. I have kept this stage in the documentation even though I moved on to more object classes afterward.

### Fourteen-class pilot

My next model covered 14 categories: bottle, can, cup, tumbler, tennis ball, apple, fork, spoon, pen, pencil, marker, bag, jug and medicine box. I trained a YOLO26n model for 10 epochs on 2,288 training images.

| Validation metric | 14-class pilot |
|---|---:|
| Precision | 70.7% |
| Recall | 67.1% |
| mAP@50 | 70.6% |
| mAP@50–95 | 51.1% |

Although the validation results were encouraging for a first larger experiment, webcam testing showed problems. Some objects were not detected well, and certain scenes produced several incorrect or unstable bounding boxes. This made me reconsider whether including so many classes at this stage was the best approach.

### Five-class model

I then narrowed the model to **bottle, tennis ball, pen, bag and phone**. I combined and remapped selected images from the earlier dataset with additional Roboflow datasets. I also checked annotations and removed 15 suspected near-duplicate training images.

The cleaned dataset had **4,630 training, 374 validation and 184 test images**. I trained from pretrained YOLO26n weights for 30 epochs, using a 416-pixel image size and batch size of 4 on the CPU. The training took approximately eight hours.

| Validation metric | Five-class model |
|---|---:|
| Precision | 88.0% |
| Recall | 77.8% |
| mAP@50 | 84.7% |
| mAP@50–95 | 65.7% |

The successful training folder is called `prosthetic_5class_v1-2`. The earlier `prosthetic_5class_v1` folder was created during an unsuccessful initial run, so `v1-2` is still the first completed five-class model, not a second trained version.

I tested each of the five categories with the webcam and got successful example detections. These validation metrics were produced on a different dataset and class set from the 14-class experiment, so they are not a controlled comparison. I still need to test the held-out images and repeat webcam tests under different conditions.

## Social gesture recognition using MediaPipe

After getting the object model working, I decided to test another feature that might make the prosthetic more interactive. I wanted it to recognize a person presenting their hand for a high-five or fist bump. I used **MediaPipe Gesture Recognizer** rather than training another YOLO model, because it already has categories for open palms and closed fists.

The original idea was just two gestures. I then modified the script to include a **thumbs up** as well.

| Recognizer output | Display label | Confidence in example screenshot |
|---|---|---:|
| `Open_Palm` | HIGH FIVE | 0.70 |
| `Closed_Fist` | FIST BUMP | 0.89 |
| `Thumb_Up` | THUMBS UP | 0.72 |

The script uses the webcam through OpenCV, displays detected hand landmarks and applies a **0.65 confidence threshold**. I also used a rolling history of seven frames: the same gesture must be predicted in at least five of those frames before its main label appears. This was intended to reduce the amount of flickering when the hand moves or the predictions change.

All three labels appeared correctly in my initial webcam examples. However, these are only individual demonstrations. I have not yet measured accuracy across different people, distances or lighting. Also, an open palm is not necessarily someone asking for a high-five; for now the program recognizes the **hand shape**, rather than knowing the person's intention.

- [Original social gesture test script](test_social_gestures.py)
- [Organized-folder version](scripts/testing/test_social_gestures.py)
- [Experiment 06 — methods, results and limitations](experiments/06_social_gestures/README.md)

## How this could eventually work on the prosthetic

The plan is to use a Raspberry Pi 5 with the Camera Module 3 Wide for the vision processing. The object detector could suggest a suitable grasp, while MediaPipe could suggest a social-interaction posture.

For example, an open palm could lead to an open-hand posture and a closed fist could lead to a fist posture. A thumbs-up response would depend on whether the thumb and finger design can produce that shape properly. The camera output alone should **not** make the prosthetic move: I still intend to use an intentional EMG signal to confirm movement, with limits on finger travel and grip pressure.

At the moment, object detection and gesture recognition have only been tested **separately on the laptop**. Combining them, testing them on the Raspberry Pi and controlling the actual servos are future steps. Handshake recognition is optional if I have enough time.

## Other files and earlier notes

- [Experiment index](experiments/README.md)
- [Dataset sources](datasets/sources.md) and [dataset preparation](datasets/preparation.md)
- [Windows / VS Code setup](LOCAL_SETUP.md)
- [Planned vision integration](integration_plan.md)
- [Log 001 — Initial setup](docs/development_log_001.md)
- [Log 002 — Pretrained YOLO webcam tests](docs/development_log_002.md)
- [Log 003 — YOLO-World](docs/development_log_003.md)
- [Log 004 — Tennis ball/apple](docs/development_log_004.md)
- [Log 005 — Building the fourteen-class dataset](docs/development_log_005.md)
- [Early system overview](docs/vision_system_overview.md)

The earlier logs are kept to show how my decisions developed. Some of those notes were written before the 14-class and five-class training was completed, so they do not always reflect the current results.

Raw dataset exports, virtual environments and larger model checkpoints are kept on the SSD rather than uploaded with the documentation.
