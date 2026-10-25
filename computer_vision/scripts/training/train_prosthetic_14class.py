
from pathlib import Path
import yaml
from ultralytics import YOLO

# Main project folder
project = Path(__file__).resolve().parent

# Dataset folder - updated name
dataset = project / "datasets" / "14cat_prostheticobjects"

if not dataset.exists():
    raise FileNotFoundError(f"Dataset not found: {dataset}")

# Define dataset paths and 14 object classes
config = {
    "path": str(dataset),
    "train": "images/train",
    "val": "images/val",
    "test": "images/test",
    "names": {
        0: "bottle",
        1: "can",
        2: "cup",
        3: "tumbler",
        4: "tennis_ball",
        5: "apple",
        6: "fork",
        7: "spoon",
        8: "pen",
        9: "pencil",
        10: "marker",
        11: "bag",
        12: "jug",
        13: "medicine_box"
    }
}

# Create local dataset configuration
local_yaml = dataset / "data_local.yaml"

with open(local_yaml, "w", encoding="utf-8") as file:
    yaml.safe_dump(config, file, sort_keys=False)

# Load pretrained YOLO model
model = YOLO(str(project / "yolo26n.pt"))

# Train our 14-class model
model.train(
    data=str(local_yaml),
    epochs=10,
    imgsz=416,
    batch=4,
    device="cpu",
    workers=0,
    project=str(project / "runs"),
    name="prosthetic_14class_pilot",
    exist_ok=False
)