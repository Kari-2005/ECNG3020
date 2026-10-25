# ECNG 3020 — Robotic Prosthetic Hand: Computer Vision

This folder documents the vision subsystem's development from pretrained YOLO26n webcam tests to an experimental fourteen-class dataset and prospective grasp selection.

## Development history
- [Log 001 — Setup](docs/development_log_001.md)
- [Log 002 — YOLO26n webcam baseline](docs/development_log_002.md)
- [Log 003 — YOLO-World alternative](docs/development_log_003.md)
- [Log 004 — Tennis-ball/apple fine-tuning](docs/development_log_004.md)
- [Log 005 — Dataset progression to 14 classes](docs/development_log_005.md)
- [Vision architecture and future integration](docs/vision_system_overview.md)

## Source code and experiment scripts

- [Original MediaPipe social-gesture webcam script](test_social_gestures.py)
- [Folder-adapted MediaPipe testing script](scripts/testing/test_social_gestures.py)
- [Six experiment records](experiments/README.md)

The initial YOLO and training scripts are being restored from the verified SSD files. Earlier reconstructed versions were intentionally removed and are not presented as working source code.

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


## Extended development audit (25 October 2026)
- [Decision history and lessons learned](docs/development_decisions_and_lessons.md) — reasons for model and scope changes, observed failures and planned grasp mappings.
- [Dataset versions and quality checks](datasets/version_history.md) — class remapping, source caveats, pilot counts and QA limitations.
- [Training and evaluation summary](docs/training_and_evaluation_summary.md) — comparison of the two-class, 14-class and five-class runs.

Earlier source-code references in historical logs are retained for chronology but may point to files intentionally removed pending verification against the Samsung SSD. The original executed YOLO scripts should be restored only from the SSD. No model checkpoint or dataset ZIP was added with this audit.
