# YOLO Training and Evaluation Summary

**Status:** Consolidated from development notes and later experiment records. Model results below were *reported* for the relevant training runs; unprovided terminal logs and machine-readable artifacts remain to be verified against the SSD.

| Experiment | Classes | Train / Val / Test | Epochs | Input | Batch | Compute | Duration | Outcome |
|---|---:|---|---:|---:|---:|---|---|---|
| Tennis ball vs apple | 2 | 438 / 124 / 68 | 10 | 416 | **8** | Windows CPU | Not recorded | User reported worn tennis ball recognized; apple weakness and false positives remain |
| Broad 14-class pilot | 14 | 2,288 / 518 / 366 | 10 | 416 | 4 | Windows CPU | ~2.13 h | Validation P=.707, R=.671, mAP50=.706, mAP50–95=.511 |
| Focused five-class model | 5 | 4,630 / 374 / 184 | 30 | 416 | 4 | Windows CPU | ~8 h | Validation P=.880, R=.778, mAP50=.847, mAP50–95=.657 |

All custom YOLO experiments used **YOLO26n pretrained initialization** where documented. The training workflow saves `best.pt` and `last.pt` checkpoints for later inference; no retraining is required at each webcam launch.

## Experiment-specific details
**Two-class:** attempted to correct tennis-ball confusion with apple; user reported successful webcam detection but also inappropriate ball classification on a non-target region. Exact model metrics and local path remain to be verified.

**Fourteen-class:** run `prosthetic_14class_pilot`. Good validation figures for selected categories did not necessarily translate to stable webcam bounding boxes and utensil recognition.

**Five-class:** classes: bottle, tennis_ball, pen, bag, phone. Original run name `prosthetic_5class_v1` corresponds to an unsuccessful early attempt; the completed run is `prosthetic_5class_v1-2`, with weights under `runs/prosthetic_5class_v1-2/weights/best.pt`. Five-class reported mAP50 by category: bottle .687, tennis_ball .985, pen .927, bag .737, phone .900. Single webcam demonstration examples had confidence .95, .89, .87, .80 and .79 (respectively), **not category accuracy**.

## Interpretation caveats
These validation runs have different class lists, data amounts and splits. The mAP differences are **not controlled evidence** of a universally superior detector, and a 30-epoch versus 10-epoch comparison changes more than one variable. The held-out test split and independently captured physical-object webcam videos should be evaluated using a reproducible protocol.

## Needed artifacts
Exact original scripts, YAMLs, run `args.yaml`, `results.csv`, confusion matrix images, validation plots, training package versions, independent test scores and optional original model files or hashes. Model weights should remain on SSD or an appropriate release/artifact host, not ordinary Git.

References: [14-class run](../experiments/04_14class_pilot/README.md), [five-class run](../experiments/05_5class_model/README.md), [source provenance](../datasets/sources.md).


## Verified original two-class run configuration — 25 October 2026
The original Ultralytics `args.yaml` from `training_runs/tennis_ball_apple_v1-2` was supplied and confirms model `yolo26n.pt`, data `datasets/ball_experiment/combined/data.yaml`, epochs **10**, batch **8**, input size **416**, CPU, `workers=0`, `pretrained=true`, `optimizer=auto`, `seed=0`, `val=true` and `plots=true`. **Earlier documentation stating batch 4 for this specific run was incorrect and superseded.** The original training Python script has not been located, but this saved Ultralytics run configuration documents the actual settings. The original webcam test is [`test_trained_model.py`](../scripts/testing/test_trained_model.py).
