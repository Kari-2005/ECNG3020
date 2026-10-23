"""Two-class tennis_ball/apple training pilot (reconstructed reference)."""
from pathlib import Path
import yaml
from ultralytics import YOLO

# Repository layout: computer_vision/scripts/ (edit dataset path for SSD location)
project = Path(__file__).resolve().parents[1]
root = project / "datasets" / "ball_experiment" / "combined"
if not (root / "data.yaml").exists():
    raise FileNotFoundError(f"Extract dataset first: {root}")
config = {
    "path": str(root), "train": "images/train",
    "val": "images/val", "test": "images/test",
    "names": {0: "tennis_ball", 1: "apple"}
}
local_yaml = root / "data_local.yaml"
with open(local_yaml, "w", encoding="utf-8") as f:
    yaml.safe_dump(config, f, sort_keys=False)
model = YOLO(str(project / "yolo26n.pt"))
model.train(data=str(local_yaml), epochs=10, imgsz=416, batch=4, device="cpu",
            workers=0, project=str(project / "runs"), name="tennis_apple_pilot")
