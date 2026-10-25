# Experiment 06 — High-Five, Fist Bump and Thumbs Up

## Why I tried this

Along with detecting objects that the prosthetic might pick up, I wanted to see whether it could recognize a few basic social gestures. I started with a high-five and a fist bump, since these seemed fairly simple. I later added thumbs up to the same code.

I haven't connected this to the physical hand yet. This experiment is only to see whether the webcam can identify the gestures.

## What I used

- Python and OpenCV for the webcam.
- Google's MediaPipe Gesture Recognizer and its pretrained `gesture_recognizer.task` model.
- The laptop webcam to test the gestures.
- A seven-frame history to make the label a little less jumpy.

## How my code works

The camera captures a frame, MediaPipe checks the hand gesture and returns a category and confidence score. I used these categories:

| MediaPipe output | What my program shows |
|---|---|
| `Open_Palm` | `HIGH FIVE` |
| `Closed_Fist` | `FIST BUMP` |
| `Thumb_Up` | `THUMBS UP` |

I used a confidence threshold of **0.65**. If the result is below that, it is treated as no recognized gesture. To help with flickering, the program also needs **five matching predictions out of the most recent seven frames** before showing one of the three main labels.

It also draws the detected hand landmarks, so I can see the points that are being tracked.

## Results so far

I tried all three gestures in front of the webcam and managed to get the correct labels.

| Gesture | Confidence in screenshot |
|---|---:|
| High-five/open palm | 0.70 |
| Fist bump/closed fist | 0.89 |
| Thumbs up | 0.72 |

These scores are from individual example frames. I haven't done a proper accuracy test with different people, lighting conditions and distances yet, so I don't want to claim that the system is always correct.

## Code

- [My original test script](../../test_social_gestures.py) — this is the version I ran and edited to include thumbs up.
- [Organized-folder copy](../../scripts/testing/test_social_gestures.py) — adjusted to find the model when the code is inside `scripts/testing`.

For the original version, the MediaPipe model goes in `computer_vision/models/gesture_recognizer.task`. Run it from the `computer_vision` folder using:

```powershell
.\.venv-vyonix\Scripts\python.exe test_social_gestures.py
```

Press **Q** to close the webcam.

## What I noticed / things to improve

The three gestures were recognized in my first successful webcam tests, which means I can try using them as an extra input for the prosthetic. But an open hand might just be someone waving and a fist might not actually be an invitation for a fist bump.

For now, I only want the camera to suggest a hand posture. Before the prosthetic moves, I still plan to use the EMG signal as a confirmation and check the servo limits.

If I have enough time later, I might also try recognizing someone offering a handshake. That is not part of the working code yet.
