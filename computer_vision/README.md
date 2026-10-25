# ECNG 3020 — Computer Vision Subsystem

This directory documents the experimental vision subsystem for a deep-learning-assisted robotic prosthesis. **Object detection suggests a grasp; it does not authorize motor movement.**

## Development logs
- [001 — Software setup](docs/development_log_001.md)
- [002 — Pretrained YOLO26n baseline](docs/development_log_002.md)
- [003 — YOLO-World evaluation](docs/development_log_003.md)
- [004 — Tennis-ball/apple fine-tuning](docs/development_log_004.md)
- [005 — Dataset evolution to 14 classes](docs/development_log_005.md)
- [Decisions and lessons learned](docs/development_decisions_and_lessons.md)
- [Training and evaluation summary](docs/training_and_evaluation_summary.md)
- [Vision system overview](docs/vision_system_overview.md)

## Original experiment scripts (uploaded from SSD)
- [Initial pretrained YOLO webcam test](scripts/testing/test_camera.py)
- [YOLO-World open-vocabulary webcam test](scripts/testing/test_yolo_world.py)
- [First tennis-ball/apple trained-model webcam test](scripts/testing/test_trained_model.py)
- [Train 14-class detector](scripts/training/train_prosthetic_14class.py)
- [Test 14-class detector](scripts/testing/test_prosthetic_14class.py)
- [Train 5-class detector](scripts/training/train_prosthetic_5class.py)
- [Test 5-class detector](scripts/testing/test_prosthetic_5class.py)
- [Original MediaPipe gesture test](test_social_gestures.py)
- [Folder-adapted gesture test](scripts/testing/test_social_gestures.py)

These YOLO files were copied from user-uploaded SSD scripts, **not reconstructed from conversation notes**. The exact two-class *training* script has not yet been uploaded; only its original testing script is present. File-relative paths in these scripts reflect the original SSD layout and may require adjustment if run directly from the organized GitHub folders.

## Six experimental stages
[Experiment index](experiments/README.md) covers:
1. Pretrained YOLO26n webcam detection;
2. YOLO-World text-prompt detection;
3. two-class tennis-ball/apple fine-tuning;
4. fourteen-class YOLO26n pilot;
5. focused five-class YOLO26n detector (bottle, tennis_ball, pen, bag, phone);
6. MediaPipe webcam gesture recognition (open palm/high-five candidate, closed fist/fist-bump candidate, thumbs-up).

The 14-class and five-class models were trained on a Windows CPU. The six experiments are not proof of completed Raspberry Pi or prosthetic integration.

## Dataset and model evidence
- [Dataset source attribution](datasets/sources.md)
- [Version and QA history](datasets/version_history.md)
- [Data preparation](datasets/preparation.md)
- [14-class results](experiments/04_14class_pilot/README.md)
- [Five-class results](experiments/05_5class_model/README.md)
- [MediaPipe gesture results](experiments/06_social_gestures/README.md)
- [Integration plan](integration_plan.md)

Five-class screenshot examples were supplied for **pen (.80), phone (.89), bag (.79), tennis_ball (.95) and bottle (.87)**. MediaPipe examples showed **Closed_Fist (.89), Open_Palm (.70), Thumb_Up (.72)** with hand landmarks. These are **individual webcam confidence values, not model accuracy**. Original images were reviewed but are not yet stored as binary files in GitHub.

No weights (`.pt`), raw datasets, run archives or virtual environments are committed here. Dataset provenance and test-set metrics should be verified before use in a final research report.
