# System Overview

## 1. Purpose

This document provides a working overview of the proposed robotic upper-limb prosthesis. It is intended to track the main system features, how they are expected to work, the main components involved, and design decisions that are still under investigation.

The project is a proof-of-concept system combining myoelectric user intent, vision-assisted grasp selection, tendon-driven actuation, tactile sensing and haptic feedback.

## 2. Overall Operating Concept

The planned operating sequence is:

1. A camera observes an object in the user's environment.
2. A deep-learning model identifies or classifies the object.
3. The system selects or suggests a suitable predefined grasp.
4. The user intentionally contracts a residual muscle.
5. The sEMG subsystem detects the contraction and triggers the selected grasp.
6. The embedded controller commands the hand actuators.
7. Tendons close the required fingers around the object.
8. Fingertip sensors detect contact and estimate grip force.
9. Vibrotactile actuators return contact/force information to the user.
10. A temperature-sensing subsystem monitors for potentially unsafe thermal conditions.

The vision system is intended to **assist** the user rather than fully control the prosthesis.

## 3. Feature Overview

| System Feature | Planned Function | Main Components / Parts | How It Is Intended to Work | Current Status / Notes |
|---|---|---|---|---|
| Open-source hand base | Provide the main hand geometry and mechanical starting point | Open-source CAD/3D-printable hand | Existing design will be adapted instead of developing every hand component from scratch | **Under investigation.** Rebelia V1 is a strong candidate. Original proposal referenced OpenBionics, so final platform should be confirmed with supervisor |
| Forearm structure | House actuation and electronics | 3D-printed forearm, mounting features, covers | Custom forearm will hold servos, controller, drivers, wiring and other electronics | **Planned** |
| Adjustable wrist | Allow the hand orientation to be changed for different tasks | Mechanical wrist joint, locking/positioning mechanism | User adjusts the hand to selected positions before/during use | **Under investigation.** Exact mechanism and number of positions/DOF not yet fixed |
| Finger actuation | Open and close fingers to produce grasp patterns | Servos, tendons, finger joints | Servos pull tendons routed through the fingers to generate flexion | **Planned / under investigation** |
| Passive finger return | Re-open fingers after tendon tension is released | Elastic cord / elastic return element | Elastic element provides restoring force to extend the fingers | **Under investigation** |
| sEMG input | Detect intentional muscle activation from the user | Surface electrodes / sEMG module, signal-conditioning electronics | Muscle activity is processed and compared with a calibrated threshold to determine intentional activation | **Planned** |
| EMG calibration | Adapt the trigger level to the individual user and signal conditions | Calibration software/interface, sEMG hardware | User records relaxed and contracted states and the system determines a suitable operating threshold | **Planned** |
| Vision input | Observe objects for grasp assistance | Camera module | Camera supplies images to the high-level processor | **Planned.** Final camera position not yet selected |
| Object recognition | Identify or classify objects | Embedded Linux processor, deep-learning model, camera | Model processes camera images and assigns an object class | **Planned** |
| Grasp selection | Choose a suitable stored grasp pattern | Deep-learning / decision logic, grasp library | Object class is mapped to a predefined grip such as power, pinch or precision | **Planned** |
| User-triggered grasp | Keep the user in control of when movement occurs | sEMG subsystem + grasp-selection output | Vision selects/suggests the grasp, but the movement only occurs when the user intentionally activates sEMG | **Planned** |
| Fingertip tactile sensing | Detect contact and estimate grip force | Approximately five fingertip FSR channels or equivalent sensors | Sensors change output as contact force increases | **Planned.** Exact sensor model to be selected |
| Slip investigation | Investigate whether object instability can be detected | Tactile sensors and/or additional sensing | Changes in force or other tactile signals may be used to infer slip | **Investigation only at this stage** |
| Vibrotactile feedback | Return tactile information to the user | Vibration motors/tactors, drivers, sleeve/socket | Different vibration locations can represent different fingers; vibration intensity may represent force | **Planned** |
| Temperature safety sensing | Warn of potentially unsafe hot/cold objects or environments | Non-contact IR temperature sensor or similar, buzzer | Temperature is monitored and an alert is generated when a safety threshold is exceeded | **Under investigation** |
| Low-level controller | Handle real-time sensing and actuation | ESP32-S3 or compatible microcontroller | Reads sensors, controls haptic actuators, communicates with servos and exchanges commands with high-level processor | **Candidate selected: ESP32-S3; integration still to be verified** |
| High-level processor | Run vision, deep learning and ROS 2 functions | Raspberry Pi / Jetson-class embedded Linux board | Processes images, performs grasp prediction and communicates with low-level controller | **TBD** |
| Power system | Supply electronics and motors | Battery, regulators, protection, distribution wiring | Provides required voltage rails for processors, sensors, servos and feedback devices | **TBD** |
| ROS 2 integration | Connect software subsystems | ROS 2 nodes/topics/services | Nodes exchange vision, grasp, sensor and controller information | **In development** |
| Gazebo simulation | Test the digital prosthetic system before physical integration | Gazebo, URDF/Xacro, meshes | Simulates joints, movement, contact and grasping | **In development** |
| Physical prototype | Validate the integrated concept | 3D-printed components + electronics | Mechanical and electronic subsystems will be assembled and tested progressively | **Planned** |

## 4. Controller Architecture

The system is expected to use a two-level control structure.

### High-Level Processing
Likely responsibilities:
- camera acquisition
- object recognition
- deep-learning inference
- grasp selection
- ROS 2 integration
- communication with low-level controller

Candidate hardware:
- Raspberry Pi
- NVIDIA Jetson-class platform

Final selection is still to be made.

### Low-Level Processing
Likely responsibilities:
- sEMG acquisition / trigger handling
- fingertip sensor acquisition
- servo commands
- vibrotactile actuator control
- temperature input
- buzzer / safety warning
- communication with high-level processor

Current candidate:
- ESP32-S3

## 5. Mechanical Architecture

The mechanical system is expected to consist of:
- open-source prosthetic hand base
- tendon-driven finger mechanism
- passive elastic finger return
- servo-based actuation
- adjustable wrist
- custom forearm enclosure

The final tendon material, routing method, return mechanism, wrist design and actuator sizing will be supported by literature review, calculations and prototype testing.

## 6. Simulation Workflow

Planned modelling workflow:

```text
CAD Model
   ↓
Separate Rigid Links
   ↓
Define Joint Origins and Axes
   ↓
Export Meshes
   ↓
URDF / Xacro
   ↓
RViz Verification
   ↓
Gazebo Simulation
   ↓
ROS 2 Control / Grasp Testing
```

Where practical, tendon behaviour will also be investigated in simulation. A simplified representation may be used initially if full tendon physics becomes too complex for the first model.

## 7. Planned Evaluation

Possible technical evaluation includes:
- object-recognition accuracy
- correct grasp-selection rate
- sEMG response latency
- controller/actuation latency
- grip force
- tactile sensor response
- haptic feedback latency
- repeated grasp success
- object drop rate
- excessive-force / object-crush events
- repeatability of finger motion
- thermal warning response
- simulation vs physical behaviour where comparable

The final test set will depend on the features successfully implemented within the project timeline.

## 8. Open Design Decisions

The following items are intentionally not fixed yet:

- final open-source hand platform
- final wrist mechanism
- number of wrist positions / DOF
- exact tendon material and routing
- elastic return material
- exact servo model
- camera location
- exact camera module
- high-level embedded processor
- exact fingertip sensor model
- method used for slip detection
- exact haptic actuator type and placement
- exact temperature sensor
- communication method between processors
- battery and power-distribution design

## 9. Current Priority

The immediate development priority is to complete the mechanical hand, wrist and forearm design, establish correct joint geometry for ROS 2/URDF export, and continue documenting the design decisions before full system integration.
