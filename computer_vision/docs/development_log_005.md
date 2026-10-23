# Development Log 005 — Progression to 14-Class Prosthetic Vision

**Period:** October 2026  
**Status:** 14-class dataset prepared; full training metrics not verified

## Decisions 16–17: Deployment and scope
The preferred direction is one specialized YOLO26n detector, rather than two detectors in parallel, to simplify Raspberry Pi 5 inference. This requires latency and quality benchmarking. Oranges were excluded; apple and tennis ball retain spherical-grasp coverage.

## Decision 18: Cylindrical
Selected: `bottle`, `can`, `cup`, `tumbler`. Two bottle exports and relevant cup/mug/tumbler data were combined. Some candidate can sources labeled *can defects*, not whole cans, so unrelated annotations were excluded. A balanced pilot had **1,420 images** (1,063 train, 251 val, 106 test). Handled mugs may not always use cylindrical body grasp.

## Decision 19: Tripod
Selected: `fork`, `spoon`, `pen`, `pencil`, `marker`. Fork sources were combined; segmentation polygons were converted into bounding boxes where needed. An initial ambiguous marker dataset (`Acrylic Plastic`) was superseded by a better-labelled marker dataset; supplementary spoons were added. Revised tripod pilot: **2,331 images** (1,760 train / 241 val / 330 test).

## Decision 20: 11-class pilot
Cylindrical, spherical and tripod sources were sampled/combined into a transfer-friendly balanced 11-class pilot: **2,026 images** (1,524 / 279 / 223).

## Decisions 21–22: Stretch-goal classes
Three more classes were included for future recognition, **without promising physical grasp implementation**:
- `bag`: six numeric source labels collapsed into one class; original semantics need visual audit.
- `jug`: original single-class labels retained; source had no independent test split.
- `medicine_box`: 23 product/package categories collapsed into one; do not claim general box detection.

## Decision 23: 14-class pilot
The combined pilot `prosthetic_vision_14class_pilot.zip` has **3,172 images**: **2,288 training**, **518 validation** and **366 test**. Proposed class IDs:

| ID | Class | Suggested grasp | Status |
|---:|---|---|---|
| 0 | bottle | cylindrical | primary |
| 1 | can | cylindrical | primary |
| 2 | cup | cylindrical body | primary |
| 3 | tumbler | cylindrical | primary |
| 4 | tennis_ball | spherical | primary |
| 5 | apple | spherical | primary |
| 6 | fork | tripod | primary |
| 7 | spoon | tripod | primary |
| 8 | pen | tripod | primary |
| 9 | pencil | tripod | primary |
| 10 | marker | tripod | primary |
| 11 | bag | hook/handle | stretch |
| 12 | jug | handle/body depending on geometry | stretch |
| 13 | medicine_box | palmar | stretch |

The merged package is a **selected pilot**, not all original source images. Class-ID/ZIP structural checks do **not** establish annotation quality. Review missing target boxes, dataset source versions and near-duplicates across splits prior to publishing model performance.

## Decision 24: Planned 14-class training
`train_prosthetic_14class.py` initializes from `yolo26n.pt` and uses a 10-epoch CPU pilot (`imgsz=416`, batch 4, workers 0). Planned output: `runs/prosthetic_14class_pilot/weights/best.pt`. Results have not been confirmed in the conversation at documentation time.

## Pending evaluation
- Verify sample annotations, especially ambiguous bag classes.
- Audit near-duplicate source images and train/val/test leakage.
- Document image licenses, creators and source dataset versions.
- Measure per-class precision, recall, mAP, false positives and inference latency.
- Validate objects in a real scene, not only dataset photographs.

**Sources:** https://universe.roboflow.com/leong-moxsd/bag-px1ji/dataset/1 ; https://universe.roboflow.com/yiheng-project/jug-8qerw/dataset/4 ; https://universe.roboflow.com/cv-vkzcl/medicineboxes-bk9p1/dataset/1 ; https://docs.ultralytics.com/modes/train/

**Code references:** `../scripts/train_prosthetic_14class.py`, `../scripts/test_prosthetic_14class.py` (draft reconstructions).
