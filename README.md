# ECNG3020 — Robotic Prosthetic Project

## Project Title
**Design, Simulation, and Development of a Deep-Learning-Assisted Robotic Prosthesis with Haptic Tactile Feedback**

This repository contains the code, simulation files, design notes, documentation, and supporting project files for my ECNG3020 Final Year Project.

## Project Overview
The project focuses on the development of a proof-of-concept robotic upper-limb prosthesis based on an open-source hand platform. The proposed system combines:

- myoelectric (sEMG) user input
- vision-assisted object recognition and grasp selection
- tendon-driven finger actuation
- fingertip tactile/force sensing
- vibrotactile haptic feedback
- temperature-based safety monitoring
- embedded control
- ROS 2 and Gazebo simulation
- 3D-printed mechanical components

The intended control approach is **shared control**. The vision system assists with identifying an object and selecting a suitable grasp pattern, while the user provides the intentional command to carry out the grasp through sEMG.

## Repository Structure

```text
ECNG3020/
├── README.md
├── docs/
│   ├── ros2/
│   │   ├── 01_Setup.md
│   │   └── 02_First_Xacro_Model.md
│   └── 03_System_Overview.md
├── cad/                 # Planned CAD and mechanical design files
├── ros2_ws/             # Planned ROS 2 workspace and packages
├── firmware/            # Planned microcontroller firmware
├── vision/              # Planned object-recognition / deep-learning code
├── electronics/         # Planned circuit diagrams and hardware notes
├── testing/             # Planned test scripts, data and results
└── report/              # Planned report-related project material
```

> Some folders above are planned and will be added as the project develops.

## Current Development Areas

### Mechanical Design
- Adapt an open-source prosthetic hand platform.
- Design a forearm section to house actuation, electronics, wiring and controllers.
- Investigate tendon-driven finger actuation with passive elastic return.
- Develop an adjustable wrist mechanism.

### Myoelectric Control
- Acquire and process surface EMG signals.
- Investigate calibration, filtering and threshold-based intent detection.
- Use sEMG as the user command that triggers the selected grasp.

### Vision-Assisted Grasping
- Detect or classify objects using a camera and deep-learning model.
- Map detected objects to predefined grasp patterns.
- Retain user control of the final grasp action.

### Tactile and Haptic Feedback
- Use fingertip force-sensitive sensing to detect contact and estimate grip force.
- Investigate object-slip detection where practical.
- Map tactile information to localized vibrotactile feedback on the user.

### Safety Monitoring
- Investigate non-contact temperature sensing.
- Provide an alert for potentially unsafe hot or cold conditions.

### Simulation
- Build the prosthetic model using URDF/Xacro.
- Simulate the system using ROS 2 and Gazebo.
- Evaluate joint motion, grasping, contact behaviour and tendon behaviour where practical.

## Planned System Flow

```text
Camera
  ↓
Object Recognition / Grasp Prediction
  ↓
Selected Grasp
  ↓
User sEMG Trigger
  ↓
Embedded Controller
  ↓
Servo / Tendon Actuation
  ↓
Object Contact
  ↓
Fingertip Force Sensors
  ↓
Vibrotactile Feedback to User
```

Temperature sensing operates alongside the main grasping loop as a safety-monitoring function.

## Project Status
This repository is a working engineering repository and will change throughout the project. Design choices marked as planned or under investigation are not yet final.

For a more detailed breakdown of the planned system, see [docs/System_Overview.md](docs/System_Overview.md).

## Tools and Technologies
Current or planned tools include:

- ROS 2
- Gazebo
- URDF / Xacro
- Fusion 360 / SolidWorks
- Python
- PyTorch or TensorFlow
- OpenCV
- ESP32-S3
- Raspberry Pi or NVIDIA Jetson-class embedded platform
- 3D printing

## Author
Ansarah Mohammed  
BSc Electrical & Computer Engineering  
The University of the West Indies, St. Augustine

## Academic Project
This repository is maintained as part of ECNG3020 and is intended to document the development process, design decisions, simulations, implementation, testing and final project outputs.
