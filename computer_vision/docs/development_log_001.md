# ECNG 3020 — Robotic Prosthetic Hand
## Computer Vision Development Log 001: Initial Software Environment Setup

**Date:** 22 October 2026  
**Subsystem:** Computer vision and object recognition  
**Status:** Initial Python and YOLO environment installed; webcam testing pending  
**Target deployment:** Raspberry Pi 5 with Raspberry Pi Camera Module 3 Wide (120°)

### 1. Objective
Establish a reproducible Python development environment for a YOLO-based object detection subsystem before the Raspberry Pi and camera hardware arrive. The subsystem will eventually identify objects, provide inputs to a grasp-selection algorithm, and communicate the selected grasp to the prosthetic controller. Object recognition alone must not initiate physical hand movement.

### 2. Hardware and software context
| Item | Purpose / status |
|---|---|
| Windows development laptop | Initial environment setup, programming, documentation, and testing |
| Samsung T7 Shield 1 TB external SSD | Shared storage for source code, datasets, models, and results |
| Python 3.12.10 (64-bit) | Installed on the development laptop, as reported |
| Visual Studio Code | Installed on the development laptop, as reported |
| Ultralytics package (YOLO) | Installed and successfully imported from the project virtual environment, as reported |
| Raspberry Pi 5 + Camera Module 3 Wide | Ordered for later deployment; not used during this setup |

### 3. Actions completed
1. Installed Python **3.12.10** and Visual Studio Code on the Windows development laptop.
2. Connected the Samsung T7 Shield and created/opened the project directory:
   `ECNG3020/Computer-Vision/`
3. Opened this folder in Visual Studio Code via **File → Open Folder**.
4. Opened a VS Code terminal and checked the current working directory with `pwd`, confirming work was taking place in the SSD project folder.
5. Created a Python 3.12 virtual environment inside the folder, named `.venv`:
   ```powershell
   py -3.12 -m venv .venv
   ```
6. Updated pip and installed Ultralytics within that environment:
   ```powershell
   .\.venv\Scripts\python.exe -m pip install --upgrade pip
   .\.venv\Scripts\python.exe -m pip install ultralytics
   ```
7. Verified that the Ultralytics `YOLO` import succeeded:
   ```powershell
   .\.venv\Scripts\python.exe -c "from ultralytics import YOLO; print('YOLO installed successfully!')"
   ```
   **Observed result (user-reported):** Installation and verification were successful. Exact package versions and terminal output were not recorded at this checkpoint.

### 4. Important setup decisions
- **Shared assets on SSD:** Save Python source files, pretrained model weights, sample images, datasets, and recorded results in the project folder.
- **Isolated dependencies:** Use `.venv` to keep project libraries separate from other Python projects; exclude it from version control.
- **Reproducibility:** Record dependency versions in `requirements.txt` so the environment can be recreated if necessary.
- **Deployment separation:** Initial Windows webcam input will later be replaced or adapted for Raspberry Pi Camera Module 3 Wide input, likely through Picamera2. The grasp-selection logic should remain independent of the camera interface.
- **Academic record:** Record sources, technical decisions, observed results, errors, changes, and AI assistance. Do not represent example code or planned tests as completed work.

### 5. Current directory structure
```text
Samsung T7 Shield/
└── ECNG3020/
    └── Computer-Vision/
        └── .venv/                 # Python virtual environment; do not commit
```

**Planned structure (not yet confirmed created):**
```text
Computer-Vision/
├── .venv/                      # Python environment; excluded from Git
├── src/                        # Detection and grasp-selection code
├── models/                     # Downloaded weights
├── datasets/                   # Test images / videos
├── results/                    # Outputs / measurements
├── requirements.txt            # Reproducible dependencies
└── docs/                        # Development logs and references
```

### 6. Pending work / next checkpoint
1. Record installed Python, Ultralytics, PyTorch, and OpenCV versions.
2. Generate a `requirements.txt` file to document project dependencies.
3. Download a lightweight pretrained YOLO model and verify that it loads.
4. Test object detection using the laptop webcam.
5. Log detected classes, confidence values, inference speed, failures, and representative screenshots.
6. Develop and evaluate initial object-to-grasp mapping after confirming baseline object detection.

### 7. Test evidence checklist
- [x] YOLO installation/import reported successful
- [ ] Exact Python / Ultralytics / PyTorch / OpenCV version outputs recorded
- [ ] Webcam detection output observed
- [ ] FPS or latency measured
- [ ] Detection screenshots saved
- [ ] Grasp-selection rules implemented and tested

### 8. Sources and attribution
Documentation and software references (access dates and exact model release should be confirmed when preparing the final academic bibliography):

- Python Software Foundation. *Python 3.12 Documentation*. https://docs.python.org/3.12/
- Python Software Foundation. *venv — Creation of Virtual Environments*. https://docs.python.org/3.12/library/venv.html
- Microsoft. *Visual Studio Code Documentation*. https://code.visualstudio.com/docs
- Ultralytics. *Ultralytics Documentation*. https://docs.ultralytics.com/
- Ultralytics. *ultralytics* (source repository and license). https://github.com/ultralytics/ultralytics

**Attribution note:** The environment creation and installation commands were developed with ChatGPT assistance. Ultralytics YOLO is third-party software; using its API does not mean the underlying detection model was developed as part of this project. Record any later code adapted from official documentation, examples, or other repositories with exact source links and dates. Check the license before publicly distributing integrated code or pretrained weights.

### 9. Git commit
`docs(vision): record initial Python and YOLO environment setup`
