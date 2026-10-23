"""Fourteen-class pilot initialized from original YOLO26n weights."""
from pathlib import Path
import yaml
from ultralytics import YOLO

project = Path(__file__).resolve().parents[1]
root = project / "datasets" / "prosthetic_vision_14class"
if not (root / "data.yaml").exists():
    raise FileNotFoundError(f"Cannot find extracted dataset at: {root}")

names = ["bottle", "can", "cup", "tumbler", "tennis_ball", "apple", "fork", "spoon",
         "pen", "pencil", "marker", "bag", "jug", "medicine_box"]
config = {"path": str(root), "train": "images/train", "val": "images/val",
          "test": "images/test", "names": dict(enumerate(names))}
local_yaml = root / "data_local.yaml"
with open(local_yaml, "w", encoding="utf-8") as f:
    yaml.safe_dump(config, f, sort_keys=False)

model = YOLO(str(project / "yolo26n.pt"))
model.train(
    data=str(local_yaml), epochs=10, imgsz=416, batch=4,
    device="cpu", workers=0, project=str(project / "runs"),
    name="prosthetic_14class_pilot"
)
