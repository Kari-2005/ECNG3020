# Development Log 002 — Initial YOLO26n Object-Detection Baseline

**Project:** ECNG 3020 Robotic Prosthetic Hand  
**Period:** October 2026  
**Status:** Exploratory webcam testing, not formal validation

## Decisions 1–6: Motivation, environment and baseline
The vision subsystem is intended to detect everyday objects and **suggest a grasp**, not to move the prosthetic autonomously. Planned architecture: camera → detector → grasp mapping → user/EMG authorization → eventual hand controller. Finger actuation and feedback remain separate subsystems.

We selected pretrained **Ultralytics YOLO26n** as a lightweight starting point rather than training a network from scratch. The development environment used Python 3.12, VS Code, Ultralytics, OpenCV and the Samsung external SSD. A Python virtual environment and pretrained `yolo26n.pt` checkpoint were set up.

An initial webcam script, `test_camera.py`, loaded the model and filtered COCO classes to bottle, cup, apple, orange, sports ball, spoon and fork. Early experiments produced repeated display windows, so the preview was changed to a continuous OpenCV `imshow` loop.

## Preliminary observations
| Object | Observation |
|---|---|
| Bottle | Detected, about 0.85 confidence |
| Cup | Detected, about 0.45 |
| Apple | Detected, about 0.51, initially from phone-displayed image |
| Orange | Detected, about 0.54, initially from phone-displayed image |
| Tennis ball | Worn/faded-green ball repeatedly misclassified as apple, about 0.66 in one observation |
| Spoon | Detected about 0.41 when broadly facing camera; missed from some views |
| Fork | Detected about 0.46 when broadly facing camera; missed from some views |

These confidence values are selected informal observations, **not accuracy estimates**, and phone-screen images do not prove performance on physical fruit.

**Finding:** The tennis-ball/apple confusion motivated a controlled fine-tuning pilot. Preserve the original pretrained model as the baseline.

**Code:** `../scripts/test_camera.py` (reconstructed reference script; compare with original computer files before treating as exact executed code).

**References:** https://docs.ultralytics.com/ ; https://docs.opencv.org/


## Verified source-code location (25 October 2026)
The original uploaded baseline script is now available at [`scripts/testing/test_camera.py`](../scripts/testing/test_camera.py). This supersedes the earlier reconstructed-code path; all earlier test observations remain exploratory.
