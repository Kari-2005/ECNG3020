# Experiment 01 — Pretrained YOLO26n

**Purpose:** Establish a functioning computer-vision webcam pipeline before collecting or training specialized datasets.

**Method:** Load pretrained `yolo26n.pt` with Ultralytics and test its built-in COCO object categories using a webcam.

**Observation:** Useful as an initial object-detector baseline, but the predefined class vocabulary was not sufficiently tailored to the planned everyday-object/grasp selection use case.

**Decision:** Investigate open-vocabulary object detection and later custom training.

**Evidence:** Initial test script `test_camera.py`; see the earlier GitHub development logs. No quantitative accuracy benchmark is claimed for this experiment.