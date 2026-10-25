# Experiment 06 — Social Gesture Recognition with MediaPipe

## 1. Aim of the experiment

The aim of this experiment was to test whether I could use a camera to identify a few basic hand gestures that might be useful for social interaction with the robotic prosthetic hand.

My original idea was to recognize **an open palm for a high-five** and **a closed fist for a fist bump**. Once those were working, I added **thumbs up** as a third category. A handshake was also considered, but I decided to leave that as a possible later extension because recognizing someone offering a handshake would be more difficult.

This experiment is only about **vision recognition** at this stage. I have not connected it to the motors or trained the prosthetic to make these hand postures.

## 2. Software and setup

I used Python with:
- **OpenCV** to capture frames from the webcam and display the output.
- **MediaPipe Gesture Recognizer** with its pretrained `gesture_recognizer.task` model.
- **MediaPipe hand landmarks** to show the locations of the detected points on the hand.
- Python's `deque` and `Counter` to check whether a gesture was being recognized consistently over several frames.

The test was run through a Windows laptop webcam. The recognizer was set to `RunningMode.VIDEO` and `num_hands=1`, since I only needed to test one hand at a time. I used monotonically increasing timestamps because MediaPipe's video mode expects frames in time order.

## 3. How the code works

The script first checks that the pretrained gesture model exists in the local `models` folder. It then opens webcam index 0 using OpenCV's DirectShow backend.

For each webcam frame:
1. The image is flipped horizontally so the preview looks like a mirror.
2. OpenCV's BGR image is converted to RGB for MediaPipe.
3. The frame and its timestamp are passed to the gesture recognizer.
4. The highest-scoring recognized category is read, along with its confidence value.
5. Predictions below **0.65** are treated as unrecognized.
6. The recognized category is mapped to the label displayed on the screen.
7. The program checks the last seven predictions and displays the gesture label only when at least five match.
8. Yellow landmark points and the current raw prediction are drawn on the webcam display.

### Gesture categories

| MediaPipe category | Label displayed on screen | Intended meaning in the project |
|---|---|---|
| `Open_Palm` | `HIGH FIVE` | Someone may be presenting an open hand for a high-five |
| `Closed_Fist` | `FIST BUMP` | Someone may be presenting a fist for a fist bump |
| `Thumb_Up` | `THUMBS UP` | Someone may be giving a thumbs-up sign |

The script also shows `NO GESTURE` when none of these categories has enough consistent predictions. The `Thumb_Up` category was the addition I made after the original two-gesture script.

### Why I used a confidence threshold and a frame history

A single frame might be misclassified when the hand is moving, partly outside the image or not clearly visible. I set the confidence threshold to **0.65** so that weak predictions are not accepted immediately.

I also added a `deque(maxlen=7)` and counted the labels within that history. The code requires **five matching frames out of the last seven**, which helps stop the displayed result from changing constantly. This is not the same as requiring five consecutive frames; some mismatches are still allowed. The current code also gives priority to high-five, then fist bump, then thumbs up if there are overlapping counts during a transition.

## 4. Results from the webcam test

I tested each gesture separately and was able to get the correct label displayed along with MediaPipe's hand landmarks.

| Test | Displayed output | Confidence seen in screenshot | Result |
|---|---|---:|---|
| Open palm | `HIGH FIVE` | 0.70 | Correct label appeared |
| Closed fist | `FIST BUMP` | 0.89 | Correct label appeared |
| Thumbs up | `THUMBS UP` | 0.72 | Correct label appeared |

I saved screenshots of these three tests as evidence of the initial result. The confidence numbers refer to individual displayed frames; they are **not** the overall accuracy of the system.

**What worked:** The pretrained recognizer detected each of the three hand shapes, and I was able to extend the original program to include an extra gesture without another training run.

**What still needs testing:** I have not yet collected repeated results across different lighting conditions, hand orientations, distances or different people. I also need to see whether the frame-history approach behaves well when someone changes quickly from one gesture to another.

## 5. How I might use this on the robotic hand

I want to keep social gesture recognition separate from the five-object YOLO detector at first. In the final design, both could potentially run on the Raspberry Pi 5 as part of the higher-level vision system.

A recognized gesture could suggest a posture for the prosthetic:

| Detected gesture | Possible prosthetic response |
|---|---|
| High-five | Open the fingers and prepare an open palm |
| Fist bump | Close the fingers into a fist |
| Thumbs up | Keep the thumb extended while curling the other fingers, if the mechanism allows it |

These are **planned responses**, not working servo movements. The camera may detect an ordinary open hand or fist even when the person does not intend to interact, so I would not use the predicted label by itself to trigger motion. I still plan to use an intentional EMG contraction as confirmation and to test the motion and gripping limits separately.

## 6. Code and local files

- [Original script used for the three-gesture test](../../test_social_gestures.py)
- [Version adjusted for the organized scripts directory](../../scripts/testing/test_social_gestures.py)
- [VS Code setup and folder paths](../../LOCAL_SETUP.md)

The original code expects the MediaPipe asset here:

`computer_vision/models/gesture_recognizer.task`

With the terminal opened in `computer_vision`, I can run the original script using:

```powershell
.\.venv-vyonix\Scripts\python.exe test_social_gestures.py
```

The webcam window closes by pressing **Q**.

## 7. Limitations and next steps

This experiment shows that a pretrained MediaPipe recognizer can identify the three **gesture shapes** in my initial tests. It does not establish whether the person actually wants a high-five or a fist bump, and it does not yet show the prosthetic performing these movements.

My next steps would be to repeat the gesture tests in different conditions, compare the recognition speed when running alongside YOLO, and decide how these labels should be handled by the grasp-selection logic. After that I can look at sending non-actuating test messages to the ESP32-S3 before allowing any movement.

If there is enough time, I may also investigate recognizing a hand being offered for a handshake, but that is outside the current working experiment.
