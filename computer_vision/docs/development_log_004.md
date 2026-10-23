# Development Log 004 — Tennis Ball versus Apple Fine-Tuning Pilot

**Period:** October 2026  
**Status:** Training performed; informal webcam evaluation only

## Decisions 11–12: Dataset
The initial custom-learning experiment targeted the worn tennis ball's persistent misclassification as apple. Two labelled object-detection datasets were collected and combined into a two-class dataset: `0: tennis_ball`, `1: apple`. The first combined package contained **630 images** (438 train / 124 validation / 68 test). Existing class IDs and differing polygon/box annotation formats were normalized. An additional 103 apple classification-only images were found but were not included in supervised detection training because they lacked bounding boxes.

## Decision 13: Transfer learning
A training script fine-tuned pretrained `yolo26n.pt` using labelled images. The user ran **10 epochs** on CPU; weights are saved as `best.pt` and `last.pt`, not retrained each time the camera runs. Original pretrained weights were preserved. The final two-class detector does **not** automatically retain all 80 original COCO classes.

## Decision 14: First test
The user reported successful detection of their previously misclassified tennis ball using the newly trained checkpoint. This demonstrates the pipeline can be trained and tested, not that accuracy is established.

## Decision 15: Error analysis
Apple recognition still needed improvement, and the two-class model produced a false-positive tennis-ball detection on a non-target part of the scene. Potential improvements: more representative apples (including green), hard-negative empty/background scenes, stronger independent test collection, and calibrated confidence thresholds. Avoid assuming more epochs alone improves generalization.

**Code:** `../scripts/train_ball_model.py` and `../scripts/test_ball_model.py` are reconstructed examples, not verified copies of executed SSD files.

**References:** https://docs.ultralytics.com/modes/train/ ; https://docs.ultralytics.com/datasets/detect/ ; https://universe.roboflow.com/tennis-3ll0a/tennis-ball-icifx/dataset/1

*Full apple dataset author/version attribution remains to be confirmed from exported source manifests.*
