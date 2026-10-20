# Development Progress Log

**ECNG 3020 — Robotic Prosthetic Hand with Haptic Tactile Feedback**  
**Individual project | Student: Ansarah Mohammed**  
**Retrospective log compiled:** 20 October 2026

## How to read this log

This is a record of my project progress from the first weeks of planning through 20 October 2026, based on my earlier project discussions, purchasing documents, GitHub setup notes and the saved ROS 2 work. It is **not** a formal timesheet. Week ranges below are approximate, and some work overlapped.

I separate **completed work** from **research, decisions and work still to be done**. A selected component is not necessarily purchased, delivered or tested. I will add dated entries and actual results as development continues.

---

## Week 1 — Early September 2026: Understanding the project

**Main focus:** Clarify the problem and what my prosthetic hand should do.

**Work recorded:**
- Began planning my individual final-year project: **Design, Simulation, and Development of a Deep-Learning-Assisted Robotic Prosthesis with Haptic Tactile Feedback**.
- Considered why affordable upper-limb prosthetics and sensory feedback matter, with attention to the Trinidad and Tobago / Caribbean context.
- Started gathering background information on prosthetics, myoelectric control, grasping and haptic feedback.
- Began developing the project aim, scope and core functions.

**Early design direction:** Use an open-source printable hand as a starting point, rather than designing every joint from scratch.

**Important note:** The exact day-by-day work in this first week was not recorded in the available notes. This section summarizes the earliest documented planning rather than claiming a completed prototype.

## Week 2 — Approximately 8–14 September: Background and design questions

**Main focus:** Improve the project explanation and investigate feasible technology.

**Work recorded:**
- Continued outlining Chapter 1: background, the local need for prosthetics, existing devices and gaps in tactile feedback.
- Discussed the meaning of surface EMG (sEMG) and how contractions from a remaining muscle could be measured.
- Explored how a camera, deep-learning model, grip selection and a user-triggered movement could fit into one system.
- Considered whether ROS 2 and Gazebo could help test a hand before physical printing.
- Recognized the need to keep the project manageable and prioritize a proof-of-concept demonstration.

**Not yet completed:** A trained object-recognition model, tested on-body sEMG setup and physical hand.

## Week 3 — 15–21 September: Report planning and mechanical references

**Main focus:** Make the project objectives and first mechanical approach more concrete.

**Work recorded:**
- Refined the aim and background structure and worked on notes for Chapter 1.
- Organized the background around upper-limb prosthetics, access and affordability, myoelectric input, grasping and tactile feedback.
- Looked into open-source hands as a practical way to start modeling and printing.
- Considered ways to make the wrist manually adjustable.
- Explored the possibility of using fingertips with force sensors and a separate vibration-feedback sleeve.
- Discussed software and hardware options, including microcontrollers and embedded AI computers.

**Supervisor/project context:** A BIRDLab project meeting was planned for 18 September. These notes do not confirm the exact meeting outcome, so no completed decision is attributed to that meeting here.

**Open question:** Which hand design would offer a reliable tendon-driven mechanism without making the CAD and simulation work too difficult?

## Week 4 — 22–28 September: OpenBionics and early technical planning

**Main focus:** Explore a real downloadable hand model and the design tools needed.

**Work recorded:**
- Investigated the [OpenBionics Prosthetic-Hands repository](https://github.com/OpenBionics/Prosthetic-Hands) for a printable hand design.
- Discussed manually adjustable wrist ideas, including a ball-and-socket or locking mechanism.
- Compared control hardware possibilities, including an ESP32-S3, Raspberry Pi, NVIDIA Jetson and other boards.
- Considered cameras, low-cost electronics and EMG sensor modules.
- Began planning how an existing CAD model could eventually be exported into ROS 2 using URDF/Xacro.

**Status:** Research and planning; the OpenBionics design was not adopted as the final hardware baseline.

## Week 5 — Approximately 29 September–5 October: ROS 2 setup and first model

**Main focus:** Get the software environment running and learn how a robot model moves in simulation.

**Completed and documented in the repository:**
- Set up **WSL2** and **Ubuntu 24.04 LTS** on my Windows HP Pavilion x360.
- Installed **ROS 2 Jazzy**, the ROS/Gazebo integration and common build tools.
- Verified ROS communication with talker/listener messages.
- Started **Gazebo** successfully in the WSL environment.
- Created my ROS workspace, `~/prosthetic_ws`, and a `prosthetic_description` package.
- Wrote a first **Xacro/URDF model** consisting of a simple palm and one index-finger link.
- Corrected an initial XML/Xacro parsing problem.
- Created a launch file using robot_state_publisher, joint_state_publisher_gui and RViz.
- Fixed an RViz visibility issue by choosing the frame/topic and zooming closer to the small model.
- **Displayed the model and moved the test finger's revolute joint** using the slider.

**What this proved:** I could build a basic robot description and control a visible joint in RViz.

**What it did not prove:** Correct tendon physics, complete hand alignment, Gazebo grasping or a working physical finger.

**Difficulties:** Initial Ubuntu setup, missing build tools, XML formatting and RViz camera scale.

**Next steps identified:** Replace the simple shapes with real CAD geometry, check link alignment, and adapt the hand before attempting more complex simulation.

## Week 6 — Approximately 6–12 October: Change to Yeah Hand and reorganize the project

**Main focus:** Reduce unnecessary modeling problems and select a better mechanical starting point.

**Work recorded:**
- Experimented with importing existing hand meshes, including OpenBionics geometry, and encountered alignment/joint-placement problems.
- Compared that route with the open-source **opsobot Yeah Hand / Rebelia** designs.
- Changed the preferred design to a **hybrid**: **Yeah Hand V2 fingers/palm/tendon mechanism** and **V1 forearm below the wrist**.
- Decided to investigate retaining the V2 servos and dual opposing tendons in the upper-hand assembly. This avoids running active finger tendons through a rotating wrist.
- Chose a target **manually rotatable, twist-and-lock wrist** with positions at −90°, 0° and +90° around the forearm axis.
- Prioritized Fusion 360 work on the wrist, hand and forearm ahead of further detailed ROS 2 integration.
- Continued planning Chapter 1 and outlined Chapter 2, the literature review.

**GitHub documentation completed around this stage:**
- Created and organized the [ECNG3020 repository](https://github.com/Kari-2005/ECNG3020).
- Added a README and system overview.
- Organized the ROS notes in `docs/ros2/`.

**Design change to preserve in the report:** An earlier elastic-return and/or forearm-servo approach was considered, but the preferred V2 design uses two opposing tendon paths for active opening and closing.

**Not yet completed:** Finalized V1-to-V2 connection, completed Fusion 360 hybrid assembly, or fully working hand simulation.

## Week 7 — 13–20 October: Detailed component research and first purchasing requests

**Main focus:** Choose practical hardware and document why each choice was made.

**Computing and vision decisions:**
- Compared **Raspberry Pi 4**, **Raspberry Pi 5**, optional Pi AI hardware, and **NVIDIA Jetson Orin**. The Jetson was a much more expensive option.
- Selected a **Raspberry Pi 5, 4GB** starter kit for the planned lightweight object-recognition and grasp-selection work.
- Selected **Raspberry Pi Camera Module 3 Wide (SC1224)** and **Pi 5-compatible 500 mm ribbon cable (SC1130)**.
- Kept the **ESP32-S3 already available** for muscle-signal acquisition, tactile readings, servo PWM commands and haptic feedback.

**EMG decisions:**
- Compared MyoWare against other muscle-/biosignal-sensing modules.
- Selected **MyoWare 2 (DEV-27924)**, **Cable Shield 18386**, three-electrode cable **12970** and **DFRobot FIT0510** electrode pads for initial work.
- Checked that FIT0510 uses a **4 mm snap stud**; physical cable fit and on-body signal quality still need testing.
- Kept reusable conductive-fabric electrodes inside a sleeve as a later experiment.

**Actuation, tactile and temperature research:**
- Investigated replacing the original V2 smart servos with less expensive **270° positional PWM servos**. No replacement model is confirmed until one test motor is checked for fit, torque and tendon movement.
- Shortlisted braided line and PTFE guide tubing based on the Yeah Hand design.
- Shortlisted fingertip FSRs (especially FSR 400 Short), five vibration motors, a possible piezo film slip sensor and an MLX90614 IR temperature module.
- Identified remaining motor-driver, power-distribution, safe EMG isolation, sleeve and wrist-hardware requirements.

**Purchasing documents prepared:**
- **Amazon request:** TRASKIT Raspberry Pi 5 4GB kit, quoted **US$179.99**.
- **DigiKey request:** MyoWare and camera items, **US$105.20** subtotal, plus **US$4.99** shipping and **US$8.65** estimated tariff; estimated DigiKey total **US$118.84**.
- Combined estimate from the two request forms: **US$298.83**.

**Important:** These are documented purchase **requests**, not proof of approval, payment, delivery or successful hardware testing.

**Documentation work completed on 20 October:**
- Added [Component Research and Decision Log](Component_Research_and_Decision_Log.md) with alternatives, reasons and unresolved questions.
- Updated the [README](../README.md) to match the V2/V1 hybrid and selected electronics.
- Updated [System Overview](System_Overview.md), replacing outdated passive elastic return and generic forearm-servo assumptions.
- Created this development progress record.

## 8. Major decisions and why I changed direction

| Earlier idea / problem | Current approach | Reason |
|---|---|---|
| General open-source/OpenBionics hand | Yeah Hand V2 hand + V1 forearm | Reuse a more suitable existing tendon/spool setup and focus effort on integration |
| Passive elastic finger return | Opposing V2 fishing-line tendons | Keep active closing and opening where practical |
| Servos in the forearm | Servos in the V2 upper hand | Avoid complicated tendon routing through the rotatable wrist |
| General adjustable wrist | Manual locked rotation at −90°, 0°, +90° | Keep adjustment useful without adding another powered axis |
| Unspecified AI computer | Raspberry Pi 5 4GB | Lower cost than the considered Jetson Orin for the intended initial model |
| Original smart V2 servos | Investigating cheaper 270° positional PWM servos | Reduce cost, but replacement must pass physical tests |
| General fingertip sensing | Five FSRs, starting with one finger test | Measure contact first; add reliable grip feedback gradually |
| General EMG electrodes | Gel pads initially; conductive-fabric sleeve later | Easier early tests before sewing a reusable wearable arrangement |

## 9. What has actually been completed so far

- Drafted and structured early project background, aim and scope.
- Researched open-source prosthetic designs and control options.
- Installed Ubuntu 24.04, ROS 2 Jazzy and Gazebo tools and verified basic operation.
- Built and displayed a simple Xacro/URDF palm-and-finger model with an adjustable revolute joint in RViz.
- Chosen the V2 upper-hand / V1 forearm hybrid as the mechanical direction.
- Compared major electronics and documented the current preferred parts.
- Prepared two purchasing request forms.
- Organized the GitHub README, ROS notes, system overview and component decision log.

## 10. Work in progress / not yet complete

- Complete Fusion 360 hybrid model, wrist adapter, servo mounts and protected cable routing.
- Confirm suitable 270° PWM servo, spool adapter and tendon travel with one prototype finger.
- Finalize 3D-print requirements, tendon lengths, PTFE tubes and mechanical hardware.
- Measure fingertip space and test one FSR and one vibration motor circuit.
- Finalize haptic motor drivers, temperature module and optional slip sensing.
- Design servo power distribution and an **appropriately isolated, body-safe EMG interface** before on-body testing.
- Train/test the camera-based recognition model and connect Raspberry Pi to ESP32-S3.
- Create a complete V2/V1 URDF and realistic-enough Gazebo simulation.
- Assemble and test the physical prototype; collect results and evaluate performance.

## 11. How I will record future weeks

I will keep future entries short and add actual dates:

```markdown
## Week X — [date range]
**Main focus:**

**Completed:**
-

**Problems found:**
-

**Changes / decisions:**
-

**Tests and results (with evidence):**
-

**Next steps:**
-
```

Where possible I will link to GitHub commits, CAD screenshots, ROS output, part datasheets, circuit drawings and test tables. **I will not list proposed work as completed.**

## Supporting records

- [ROS 2 and Gazebo Setup](ros2/01_Setup.md)
- [First Xacro/URDF Model](ros2/02_First_Xacro_Model.md)
- [System Overview](System_Overview.md)
- [Component Research and Decision Log](Component_Research_and_Decision_Log.md)
- Amazon and DigiKey credit-card purchasing request PDFs prepared in October 2026 (kept outside this public repository because administrative forms contain personal details).

*This retrospective was compiled from the available conversations and project notes on 20 October 2026. The week groupings are approximate and can be corrected using a diary, GitHub history, supervisor records or dated screenshots.*
