
from pathlib import Path
from ultralytics import YOLO

# Main project directory
project = Path(__file__).resolve().parent

# Five-class dataset
dataset = project / "datasets" / "5cat_prostheticobjects"
data_yaml = dataset / "data.yaml"

# Pretrained model
model_path = project / "yolo26n.pt"

# Verify required files
if not data_yaml.is_file():
    raise FileNotFoundError(f"Dataset YAML not found: {data_yaml}")

if not model_path.is_file():
    raise FileNotFoundError(f"YOLO weights not found: {model_path}")

# Load original pretrained YOLO26n
model = YOLO(str(model_path))

# Train five-class detector
model.train(
    data=str(data_yaml),
    epochs=30,
    patience=10,
    imgsz=416,
    batch=4,
    device="cpu",
    workers=0,
    project=str(project / "runs"),
    name="prosthetic_5class_v1",
    exist_ok=False,
    plots=True
)

print("Five-class training completed!")