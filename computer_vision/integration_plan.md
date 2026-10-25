# Computer Vision — Proposed Prosthetic Integration

## Status

The object detector and gesture recognizer have been tested independently using a Windows laptop webcam. Their combined real-time operation, Raspberry Pi 5 deployment, ESP32-S3 communication and physical prosthetic actuation remain untested.

## Planned architecture

1. Raspberry Pi Camera Module 3 Wide provides live frames to Raspberry Pi 5.
2. YOLO26n recognizes five selected object categories and suggests a grasp type.
3. MediaPipe independently recognizes candidate social gestures: high-five, fist bump, thumbs-up.
4. Decision layer handles conflicting/uncertain detections and asks for user confirmation.
5. The EMG interface supplies an intentional control trigger; the ESP32-S3 performs constrained low-level servo control.
6. Finger FSRs support grip-pressure feedback and the sleeve's vibration modules provide localized haptic information.

Avoid treating a video classification as a direct motor command. Include stable-confidence checks, permitted grasp states, emergency stop/timeout, appropriate servo power and force/current limits, and safe body-connected EMG electrical practices.

## Proposed verification order

- Archive code/model versions and test on the laptop.
- Evaluate held-out five-class test images; measure frame rate and latency.
- Test object and gesture recognition simultaneously.
- Deploy and profile on Raspberry Pi 5.
- Exchange *non-actuating* serial test messages with ESP32-S3.
- Validate finger tendon motion, control limits and tactile feedback on the bench.
- Introduce user-confirmed EMG-triggered interactions only after safety testing.

Handshake recognition and advanced pose imitation are explicitly optional future work.