# ECNG 3020 — Robotic Prosthetic Hand

**Project title:** Design, Simulation, and Development of a Deep-Learning-Assisted Robotic Prosthesis with Haptic Tactile Feedback

This repository documents my **individual final-year project** in Electrical and Computer Engineering at The University of the West Indies, St. Augustine. It contains my research, component comparisons, CAD and mechanical design work, ROS 2 simulation notes, code, electronics, tests and project documentation as they develop.

> **Current stage (October 2026):** System design, component selection, purchasing requests and early ROS 2 work. The complete physical prosthetic and integrated control system have **not** yet been built or validated.

## Project aim

I am developing an affordable proof-of-concept upper-limb prosthetic hand that combines:

- **Myoelectric control:** detect an intentional muscle contraction to activate a grasp.
- **Vision-assisted grasp selection:** recognize an object and help select a suitable grasp, such as power, pinch or precision.
- **Social gesture recognition (early webcam tests):** recognize an open palm/high-five, closed fist/fist bump and thumbs up using MediaPipe. I still need to connect this to the prosthetic.
- **Tendon-driven fingers:** use servos and fishing-line tendons to open and close the hand.
- **Grip-pressure sensing:** monitor contact at the fingertips to help limit excessive gripping.
- **Wearable haptic feedback:** send touch information back through five vibration locations on a sleeve.
- **Additional sensing investigations:** explore object-slip detection and non-contact temperature warnings.
- **Design and simulation:** develop the mechanical model in CAD and test it with ROS 2 and Gazebo.

The goal is **shared control**: the vision system assists with choosing a grasp, but the user provides the muscle-activation command. I will start with a small set of objects and grasp types rather than full 3D autonomous grasp planning.

## Mechanical design — current direction

I plan to combine parts from the open-source [opsobot Yeah Hand / Rebelia project](https://github.com/opsobot/yeah-hand):

| Section | Planned approach |
|---|---|
| **Hand and fingers** | Yeah Hand **V2** finger, palm and tendon mechanism |
| **Forearm** | Yeah Hand **V1** section below the wrist, adapted as the prosthetic forearm |
| **Actuator location** | Keep the servos in the **V2 upper-hand assembly**, rather than moving them into the forearm |
| **Finger movement** | Keep the V2 **opposing tendon lines** for active closing and opening, using printable spools |
| **Wrist** | Design a **manual twist-and-lock joint** with target positions of −90°, 0° and +90° around the forearm axis |
| **Camera location** | Small, angled raised mount near the wrist, facing the grasping area |

This is a **planned hybrid**, not a confirmed drop-in fit. I still need to check the V1/V2 wrist connection, servo space, tendon travel, mounting strength and cable routing. The wrist will need a protected cable path so movement does not strain the camera, servo or sensor wiring.

The V2 dual-tendon approach avoids relying on elastic cord to reopen the fingers, provided the original routing works with my modifications.

## Planned electronics and control

| Part | Current choice or investigation | Status |
|---|---|---|
| High-level computer | **Raspberry Pi 5, 4GB** (TRASKIT starter kit) | Selected; included in Amazon purchasing request |
| Camera | **Raspberry Pi Camera Module 3 Wide (SC1224)** | Selected; included in DigiKey request |
| Camera connection | **Pi 5-compatible 500 mm ribbon cable (SC1130)** | Selected; included in DigiKey request |
| Low-level controller | **ESP32-S3 development board** | Already available; exact pin allocation pending |
| Muscle sensor | **MyoWare 2 (DEV-27924)** | Selected; included in DigiKey request |
| External EMG electrodes | Cable Shield 18386, three-electrode cable 12970, DFRobot FIT0510 pads | Included in DigiKey request; connector fit and signal testing pending |
| Servos | **270° positional metal-gear PWM servos** preferred over expensive smart servos | Candidate only; exact model/size not finalized |
| Pressure sensing | Five fingertip FSRs; **FSR 400 Short** is a candidate | Size and placement still to be checked |
| Slip sensing | One piezoelectric film sensor on a test finger | Possible extension; not finalized |
| Temperature sensing | **MLX90614 infrared sensor** or suitable breakout | Preferred approach; exact version not finalized |
| Haptic feedback | Five small coin vibration motors in the sleeve, with individual driver circuits | Planned; final parts pending |
| Power | Separate servo supply, regulators/protection and eventual portable battery | Not designed/finalized |

I considered the **NVIDIA Jetson Orin** for AI processing, but it was much more expensive than needed for my initial lightweight model. The Raspberry Pi 5 is the current choice.

I intend to **train or fine-tune the vision model away from the Pi where necessary**, then run lightweight predictions on the Pi. The ESP32-S3 will handle sensor sampling, motor commands and haptic outputs. Ordinary PWM servos can take control signals from the ESP32-S3 without a smart-servo bus board, but **they still require their own suitable power supply**.

### Myoelectric sleeve

For the initial experiments, I plan to use MyoWare with compatible gel electrode pads. Later I want to try **reusable conductive-fabric electrodes sewn into a sleeve**, based on the [MyoWare conductive-fabric tutorial](https://myoware.com/project/conductive-fabric-electrodes/). The same sleeve could hold five separate vibration-feedback zones.

**Electrical safety:** Electrodes placed on skin require an appropriately isolated, body-safe measurement and communication setup. The MyoWare Cable Shield is an electrode connector, **not** an isolation device. I will not treat a direct wired connection to mains-powered equipment as safe for body-connected testing.

## How the system is intended to work

```text
Camera Module 3 Wide
        |
        v
Raspberry Pi 5: object recognition + grasp selection
        |
        v
ESP32-S3 receives selected grasp
        ^
        |  MyoWare muscle-activation signal
        |
        v
ESP32-S3 commands PWM servos -> V2 spools and dual tendons
        |
        v
Fingers move and touch object
        |
        +--> Fingertip FSRs --> grip-pressure control / limits
        |
        +--> Five sleeve vibration motors --> tactile feedback

Optional additions:
  Piezo sensor --> slip investigation / warning
  IR sensor    --> non-contact temperature warning
```

The pressure sensors will provide relative contact measurements, not perfect force measurements. Slip detection and automatic grip adjustment will need controlled testing before being presented as working features. Temperature sensing will be experimental feedback, **not guaranteed burn protection**.

## Computer vision development (October 2026)

I have been working on the camera-based part of the project while the mechanical design and component selection are still ongoing. My main reason for doing this first was to test how well the recognition software would work before depending on it to help control the prosthetic.

### Object recognition

I started by experimenting with pretrained **YOLO26n** and **YOLO-World** through a webcam. After that, I trained a small two-class tennis-ball/apple model to learn the custom training process. I later tried a 14-class model to recognize a wider range of everyday objects.

The 14-class model completed training, but the webcam tests were not as consistent as I wanted. Some objects were difficult to recognize, and I saw incorrect or unstable detections. I decided to narrow the next version to five classes: **bottle, tennis ball, pen, bag and phone**.

I rebuilt and cleaned the dataset, then trained a five-class YOLO26n model for **30 epochs** on **4,630 training images**. The run took approximately eight hours on a CPU. Its validation results were:

| Metric | Five-class model |
|---|---:|
| Precision | 88.0% |
| Recall | 77.8% |
| mAP@50 | 84.7% |
| mAP@50–95 | 65.7% |

I was able to demonstrate detections for all five classes using a webcam. These are useful early results, but I still need to evaluate the held-out test set and check performance under different real-world conditions. The validation metrics should also not be treated as directly comparable to the 14-class model, because the datasets and class sets are different.

### Social gesture recognition

I also wanted to explore whether the prosthetic could recognize a few basic social gestures in addition to objects. For this I used **MediaPipe Gesture Recognizer** with OpenCV, rather than training another object detector.

I first tested an open palm and closed fist, then modified the Python script to include a thumbs-up gesture as well.

| Gesture recognized | Label shown on webcam | Example confidence |
|---|---|---:|
| Open palm | HIGH FIVE | 0.70 |
| Closed fist | FIST BUMP | 0.89 |
| Thumbs up | THUMBS UP | 0.72 |

The code uses a **0.65 confidence threshold** and checks for **five matching predictions within a seven-frame history** to reduce flickering. It also draws hand landmarks on the image. All three gestures were recognized in initial webcam tests, although the scores above come from individual example frames rather than a formal accuracy study.

For the eventual prosthetic, I am considering an open-hand posture for a high-five, a closed fist for a fist bump and a thumbs-up posture if the mechanical design allows it. These remain proposed responses. The camera is not currently connected to the servos, and an **intentional EMG trigger** would still be needed before movement.

I have documented the development stages, training results, dataset work and gesture experiment in the [computer vision folder](computer_vision/README.md). The [original three-gesture Python script](computer_vision/test_social_gestures.py) and [Experiment 06 notes](computer_vision/experiments/06_social_gestures/README.md) are also included. Combining the object and gesture models, testing on the Raspberry Pi 5 and connecting to the ESP32-S3 are still to be done. Handshake recognition is only a possible future extension.

## Software and simulation

My intended workflow is:

1. Adapt the V2 hand and V1 forearm in **Fusion 360**; design the manual wrist and sensor mounts.
2. Check rigid parts, joints and pivot positions before exporting meshes and a **URDF/Xacro** model.
3. Check the assembly in **RViz** and develop a simplified **Gazebo** simulation.
4. Develop camera-based object classification / grasp selection in Python (using suitable OpenCV and deep-learning tools).
5. Program the ESP32-S3 for EMG trigger detection, servo control, tactile readings and feedback.
6. Integrate the subsystems and compare simulation results with the physical prototype where practical.

I have been using **Ubuntu 24.04 and ROS 2 Jazzy** for early experiments. Earlier Xacro and RViz work was exploratory and does **not** yet represent a completed V1/V2 hybrid simulation. Tendon behavior may initially be simplified in ROS 2/Gazebo.

## Repository layout

Some of the main folders and files I've been working on are:

```text
ECNG3020/
├── README.md
├── computer_vision/
│   ├── README.md
│   ├── test_social_gestures.py
│   ├── experiments/
│   └── datasets/
└── docs/
    ├── Component_Research_and_Decision_Log.md
    ├── System_Overview.md
    └── ros2/
        ├── 01_Setup.md
        └── 02_First_Xacro_Model.md
```

The **component decision log** contains the most recent comparisons and choices. **System_Overview.md is an earlier planning document and may contain superseded options**; this README and the decision log reflect the current direction.

Other project areas like CAD, electronics, firmware and testing will be organized as I continue working on them.

## Purchase and development status

**First purchasing requests prepared (not necessarily placed or delivered):**

- **Amazon:** TRASKIT Raspberry Pi 5 4GB starter kit with 64GB microSD card.
- **DigiKey:** MyoWare 2 sensor, Cable Shield, three-electrode cable, gel electrode pads, Camera Module 3 Wide and Pi 5 ribbon cable.

**Next purchases or tests to settle:**

- Measure V2 palm/spool and tendon travel; **test one 270° positional PWM servo** before ordering five.
- Finalize fishing line and PTFE tubing against the actual model.
- Check V2 fingertip dimensions; test an FSR on one finger before buying the whole set.
- Choose the five vibration motors, motor drivers and their power supply.
- Investigate one piezo film slip sensor and one IR temperature sensor.
- Design the rotatable wrist connector and wiring route.
- Complete the isolated EMG testing arrangement and power-distribution plan.
- Continue Fusion 360 modeling, ROS 2 simulation and eventual physical integration.

I will record changes, trade-offs, prices and test results in the [Component Research and Decision Log](docs/Component_Research_and_Decision_Log.md), rather than claiming a part is validated simply because it was selected for purchase.

## Documentation

- [Development Progress Log](docs/Development_Progress_Log.md) — week-by-week history from project planning to current component research, including completed work and challenges.

- [Component Research and Decision Log](docs/Component_Research_and_Decision_Log.md) — comparisons, design choices and parts still under investigation.
- [System Overview](docs/System_Overview.md) — early system-planning notes (some sections predate the current hybrid design).
- [ROS 2 Setup](docs/ros2/01_Setup.md) — setup notes.
- [First Xacro Model](docs/ros2/02_First_Xacro_Model.md) — early Xacro work.
- [Yeah Hand open-source project](https://github.com/opsobot/yeah-hand) — mechanical reference.
- [Yeah Hand bill of materials](https://github.com/opsobot/yeah-hand/blob/main/hardware/BOM.md) — original design parts reference.

## Author

Ansarah Mohammed  
BSc Electrical & Computer Engineering  
The University of the West Indies, St. Augustine

*This README is a living record of an individual engineering project. Planned features and selected purchase items will be updated as they are tested and finalized.*
