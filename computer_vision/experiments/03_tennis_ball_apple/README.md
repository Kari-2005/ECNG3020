# Experiment 03 — Tennis Ball and Apple

**Purpose:** Test the full custom object-detection workflow with just two classes: `tennis_ball` and `apple`.

**Method:** Use annotated Roboflow-source images, fine-tune from YOLO26n pretrained weights and test predictions on the webcam.

**Evidence:** The original `test_trained_model..py` script and separately saved dataset archive. The checkpoint is referenced locally at `training_runs/tennis_ball_apple_v1-2/weights/best.pt` in the earlier laptop setup.

**Limitations:** Complete training outputs were not in the recently supplied `runs.zip`, so this document does not invent precision, recall or mAP figures.

**Decision:** Expand the experiment into a more varied everyday-object dataset.

See [dataset source attribution](../../datasets/sources.md).