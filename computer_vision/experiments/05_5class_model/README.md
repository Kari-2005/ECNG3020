# Experiment 05 — Five-Class YOLO26n Model

**Purpose:** Improve focus and practical reliability by concentrating on objects useful for early prosthetic testing.

**Class mapping:** `0 bottle`, `1 tennis_ball`, `2 pen`, `3 bag`, `4 phone`.

**Dataset:** Final cleaned split: 4,630 training, 374 validation, 184 test images. Source images were filtered/remapped from the prior dataset and supplemented with Water Bottle v21, Pen Detection v5, and Phones v1i from Roboflow Universe. The preparation included annotation checks and removing 15 suspected near-duplicate training images that resembled validation/test examples. Remaining labeling and generalization risks are not ruled out.

**Training:** YOLO26n initialized from `yolo26n.pt`; 30 epochs; `imgsz=416`, `batch=4`, CPU, `workers=0`; approximately 8 hours.

**Run naming:** `runs/prosthetic_5class_v1` came from an unsuccessful initial attempt; the completed first five-class model is in `runs/prosthetic_5class_v1-2`.

| Validation measure | Reported result |
|---|---:|
| Precision | 0.880 |
| Recall | 0.778 |
| mAP50 | 0.847 |
| mAP50–95 | 0.657 |

| Class | mAP50 |
|---|---:|
| Bottle | 0.687 |
| Tennis ball | 0.985 |
| Pen | 0.927 |
| Bag | 0.737 |
| Phone | 0.900 |

**Webcam test:** One successful demonstration was recorded for each of the five classes. Example model confidence scores: tennis ball 0.95, phone 0.89, bottle 0.87, pen 0.80, bag 0.79. Individual demonstration frames are not representative of overall accuracy.

**Next validation:** Evaluate the held-out test split and repeat webcam tests across different lighting, distances, backgrounds and distractor objects before Raspberry Pi deployment.

**Checkpoint path for local testing:** `runs/prosthetic_5class_v1-2/weights/best.pt`.

See [dataset preparation](../../datasets/preparation.md) and [sources](../../datasets/sources.md).

## Verified webcam screenshots (uploaded 25 October 2026)
Five user-supplied screenshots from the original webcam test `test_prosthetic_5class.py` show successful single-frame classifications and approximate object boxes:

| Object shown | Predicted class | Displayed confidence |
|---|---|---:|
| Blue ballpoint pen | pen | 0.80 |
| Handheld phone | phone | 0.89 |
| Carried purple bag | bag | 0.79 |
| Worn pale-green tennis ball | tennis_ball | 0.95 |
| Handheld water bottle | bottle | 0.87 |

The five images use the same webcam application and display a predicted bounding box around the relevant object. In the tennis-ball image the original faded ball was recognized correctly, a noteworthy qualitative improvement from the initial pretrained-model failure. These are **selected examples**, not a denominator-based accuracy or evidence of robustness to other people, scenes, or grip orientations. Image binary files remain pending upload into the repository; the screenshots were provided in the accompanying development conversation.

**Verified code links:** [training](../../scripts/training/train_prosthetic_5class.py) and [webcam test](../../scripts/testing/test_prosthetic_5class.py). The script uses `conf=0.40`, `iou=0.50`, `imgsz=416` on CPU and loads `runs/prosthetic_5class_v1-2/weights/best.pt` from the original project folder. The user-uploaded training script requests `name=prosthetic_5class_v1` with `exist_ok=False`, consistent with Ultralytics creating a numbered follow-up run after the initial attempted run.
