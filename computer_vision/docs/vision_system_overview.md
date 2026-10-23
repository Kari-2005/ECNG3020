# Prosthetic Computer Vision — System Overview

**ECNG 3020 Robotic Prosthetic Hand — Design and exploratory testing (October 2026)**

## Objective
Detect a focused set of everyday objects and propose grasp configurations to support the modified Yeah Hand (V2 fingers/hand plus V1 forearm). Recognition and motor control are distinct; detected objects must never directly trigger unconfirmed movement.

## Architecture (planned)
1. Raspberry Pi Camera Module 3 Wide captures images.
2. A fine-tuned, lightweight YOLO detector classifies objects (14-class pilot under preparation).
3. Independent Python logic maps objects to proposed grasp configurations.
4. The wearer confirms intent by EMG or a dedicated software safety input.
5. ROS 2 initially simulates the motion; later the ESP32-S3 commands servos and tendon actuation with mechanical limits.
6. Fingertip FSR readings and localized vibration feedback support contact/force awareness.

## Initial grasp types
- Cylindrical: bottle, can, cup body, tumbler.
- Spherical: apple, tennis ball.
- Tripod: fork, spoon, pen, pencil, marker.
- Hook/handle (stretch): bag; handle/body (stretch): jug.
- Palmar/flat-sided opposition (stretch): medicine box.

The mapping is a **proposal**, not proof that every configuration is mechanically feasible. Thumb orientation, tendon routing, object dimensions, EMG activation and safety testing remain necessary.

## Model selection
- YOLO26n: pretrained baseline; some successes, but worn tennis ball classified as apple.
- YOLO-World: open-vocabulary experiment; additional CLIP dependency and inconsistent observed detection; not selected as primary.
- Two-class fine-tuned YOLO26n: tennis-ball/apple pilot succeeded on an informal tennis-ball webcam observation; apple false positives remain.
- Fourteen-class fine-tuned YOLO26n: combined dataset and scripts prepared, but actual final training results and deployment performance are not yet verified.

Using **one specialized detector** is preferred over two concurrently running models, subject to Raspberry Pi measurements. Saved weights support inference without retraining each power-on.

## Future integration — not implemented yet
- MediaPipe hand tracking for open-palm/high-five and possible handshake signals, with user confirmation; recognition does not prove intent.
- ROS 2 Jazzy simulation for different grasp postures and safe range limits.
- Raspberry Pi 5 benchmarking/possible optimized NCNN export.
- MyoWare 2.0 EMG, ESP32-S3 motor control, five fingertip FSRs, five vibromotors and manual wrist detents.

## Current limitations
- Dataset labels and class semantics need visual auditing.
- Mixed-source augmented datasets may contain near-duplicates across splits.
- No reported 14-class per-category mAP/precision/recall or on-device benchmarks yet.
- Object detection does not estimate grasp orientation, stability or safe force by itself.

See `development_log_002.md` through `development_log_005.md` for the detailed rationale.
