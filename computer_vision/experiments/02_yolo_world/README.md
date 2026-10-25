# Experiment 02 — YOLO-World

**Purpose:** Evaluate the potential of a detector that can work with user-specified object category names.

**Method:** Trial `yolov8s-world.pt` via the `YOLOWorld` interface; use class-name prompts for potential prosthetic objects and inspect webcam results.

**Observation:** The open-vocabulary experiment informed the decision to narrow and explicitly train an object vocabulary better suited to the initial proof of concept.

**Decision:** Proceed with a small supervised object-detection dataset before expanding the number of classes.

**Evidence:** `test_yolo_world.py` and earlier development log. This stage was exploratory and no reproducible aggregate metric is asserted.