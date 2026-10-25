# ECNG 3020 — Robotic Prosthetic Hand: Computer Vision

This folder documents the vision subsystem's development from pretrained YOLO26n webcam tests to an experimental fourteen-class dataset and prospective grasp selection.

## Development history
- [Log 001 — Setup](docs/development_log_001.md)
- [Log 002 — YOLO26n webcam baseline](docs/development_log_002.md)
- [Log 003 — YOLO-World alternative](docs/development_log_003.md)
- [Log 004 — Tennis-ball/apple fine-tuning](docs/development_log_004.md)
- [Log 005 — Dataset progression to 14 classes](docs/development_log_005.md)
- [Vision architecture and future integration](docs/vision_system_overview.md)

## Major experiment scripts
- [Initial YOLO26n webcam test](scripts/test_camera.py)
- [YOLO-World webcam test](scripts/test_yolo_world.py)
- [Train tennis-ball/apple model](scripts/train_ball_model.py)
- [Test tennis-ball/apple model](scripts/test_ball_model.py)
- [Train 14-class detector](scripts/train_prosthetic_14class.py)
- [Test 14-class detector](scripts/test_prosthetic_14class.py)
- [Draft grasp mapping](configs/grasp_mapping_draft.py)

**Important:** These scripts are reconstructed from the recorded development conversation, **not byte-for-byte verified copies** of the working SSD scripts. Check local paths and experimental settings before running them; record revisions alongside future test results. The 14-class run is prepared, **not confirmed trained/evaluated**.

Large original and derived datasets, model weights (`.pt`), training run outputs and virtual environments are excluded from these commits. Keep original Roboflow source exports and their credits/licenses separately. Do not claim verified performance without independent evaluation.

## Updated experiments (October 2026)

The original development logs above are retained as historical records. Since those logs, the **14-class model was trained and evaluated**, a **five-class model was trained and webcam-tested**, and a **three-gesture MediaPipe webcam proof of concept** was demonstrated.

- [All six experiments](experiments/README.md)
- [14-class pilot results](experiments/04_14class_pilot/README.md)
- [Five-class detector results](experiments/05_5class_model/README.md)
- [High-five, fist bump and thumbs-up](experiments/06_social_gestures/README.md)
- [Social gesture webcam test script](scripts/testing/test_social_gestures.py)
- [Dataset sources](datasets/sources.md) and [preparation notes](datasets/preparation.md)
- [Windows local setup](LOCAL_SETUP.md)
- [Vision integration plan](integration_plan.md)

**Current scope:** The two vision approaches have been tested separately on a Windows laptop. Running both together, Raspberry Pi deployment and actual prosthetic actuation have not been demonstrated. The earlier reconstructed scripts mentioned above were intentionally removed; refer to the original verified SSD scripts when restoring other tests.
