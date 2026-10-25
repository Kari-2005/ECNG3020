# Experiment 04 — Fourteen-Class Pilot

**Purpose:** Explore recognition of a broad range of everyday objects.

**Classes (IDs 0–13):** bottle, can, cup, tumbler, tennis_ball, apple, fork, spoon, pen, pencil, marker, bag, jug, medicine_box.

**Model/training:** YOLO26n; 10 epochs; 416-pixel training image size; batch size 4; CPU. Split: 2,288 train, 518 validation, 366 test images.

| Validation measure | Reported result |
|---|---:|
| Precision | 0.707 |
| Recall | 0.671 |
| mAP50 | 0.706 |
| mAP50–95 | 0.511 |

The training took approximately 2.13 hours. The uploaded `runs.zip` includes checkpoints and training plots for `prosthetic_14class_pilot`; large checkpoints and raw datasets remain outside ordinary Git tracking.

**Practical observations:** Webcam experiments included unstable boxes, apparent false positives (notably bottles) and poor detection of some utensils. The strong numerical scores for certain classes did not guarantee robust operation on unseen real-world scenes.

**Decision:** Reduce the number of classes, incorporate additional source images and improve dataset preparation and label QA.

These are internal validation results, not an independently validated deployment accuracy.