# System Overview

**ECNG 3020 — Design, Simulation, and Development of a Deep-Learning-Assisted Robotic Prosthesis with Haptic Tactile Feedback**  
**Working update:** 20 October 2026  
**Project type:** Individual final-year project

## 1. Purpose and current stage

This document describes the system I plan to build, how each part will work and the design choices still to be tested.

I am developing a proof-of-concept upper-limb prosthetic hand with camera-assisted grasp selection, muscle-activation control, fingertip pressure sensing and wearable vibration feedback. My aim is to build and test a practical system rather than a finished clinical prosthesis.

**Current status:** I have selected the main computer, camera and myoelectric sensing components for purchasing requests. I have an ESP32-S3 development board. The hybrid hand, final servos, sensing circuits and complete prototype are **not yet built or verified**.

## 2. Current mechanical design

I intend to adapt the open-source [opsobot Yeah Hand / Rebelia](https://github.com/opsobot/yeah-hand) design:

| Part | My current design |
|---|---|
| Hand and fingers | **Yeah Hand V2** fingers, palm, tendon routing and printable spools |
| Forearm | **Yeah Hand V1** section below the wrist, modified for the prosthetic body, wires and electronics |
| Servo position | Keep the servos in the **V2 upper-hand assembly**, so they rotate with the hand |
| Finger opening and closing | Keep **two opposing fishing-line tendons** per mechanism for active closing and opening, rather than an elastic-return system |
| Wrist | Design a **manual rotating and locking joint** at target positions −90°, 0° and +90° around the forearm axis |
| Camera | Use a small, angled mount near the wrist facing the objects being approached |

The V1 and V2 sections are **not assumed to fit directly together**. I must check their dimensions and design the connecting wrist in Fusion 360. Keeping the servos above the wrist means the tendons should not have to pass through the rotating joint. Electrical wires and the camera ribbon still need clearance and strain relief.

The reference V2 design uses five actuators, but I must check which fingers are linked and how much independent movement the actual model provides before finalizing control.

## 3. System operation

The intended sequence is:

1. The wrist camera captures an image of an object.
2. A small deep-learning model on the Raspberry Pi identifies or classifies it.
3. The software suggests one of a small number of stored grasp patterns, such as power, pinch or precision. I may begin with object-to-grasp rules and extend to a learned grasp predictor.
4. MyoWare measures muscle activity. A calibrated contraction becomes the user's command to start the grasp.
5. The ESP32-S3 commands the servos to pull the V2 tendons.
6. Fingertip FSR sensors detect contact and help the controller limit further closing.
7. The five vibration motors in the sleeve give the user localized contact or pressure feedback.
8. Optional slip and temperature inputs can provide distinct warnings after they have been tested.

**Shared control:** The camera helps decide *which* grasp to use, while the muscle signal tells the hand *when* to perform it. I am not currently planning full 3D autonomous grasp synthesis.

## 4. Main components and status

| Subsystem | Part or approach | Present status |
|---|---|---|
| Main computer | **Raspberry Pi 5, 4GB**, TRASKIT starter kit | Selected in Amazon purchasing request, not confirmed received |
| Camera | **Camera Module 3 Wide (SC1224)** | Selected in DigiKey purchasing request |
| Camera cable | **SC1130**, 500 mm Pi 5-compatible ribbon | Selected in DigiKey purchasing request |
| Microcontroller | **ESP32-S3 development board** | Already available; exact board pinout to check |
| Muscle sensing | **MyoWare 2 (DEV-27924)** | Selected in DigiKey purchasing request |
| EMG electrode connection | **Cable Shield 18386 + three-electrode cable 12970** | Selected in DigiKey purchasing request |
| Initial electrodes | **DFRobot FIT0510** gel pads, two 12-packs | Selected; 4 mm snap size checked by student; actual cable fit must still be tested |
| Reusable electrodes | Sewn conductive-fabric contacts inside compression sleeve | Later design experiment |
| Servos | **270° positional PWM metal-gear servos** preferred | Model, fit, torque and travel not yet confirmed; test one first |
| Tendons | Approximately 0.75 mm, 200 lb, eight-strand braided line | Candidate based on original V2 parts list |
| Tendon guides | PTFE tube, approximately 3 mm outside / 1.5 mm inside diameter | Candidate; length and routing to be measured |
| Finger pressure sensing | **Five fingertip FSRs**; FSR 400 Short is leading candidate | Dimensions and calibration pending |
| Slip sensing | One piezoelectric film sensor for experiments | Optional investigation; conditioning circuit needed |
| Temperature | One **MLX90614** non-contact IR temperature sensor/breakout | Preferred option; exact version and position undecided |
| Feedback | Five coin vibration motors on sleeve | Planned; drivers, power and positions to confirm |
| Power | Separate correctly rated servo supply, power distribution and protective components | Design pending |
| Software | Fusion 360, Ubuntu 24.04, ROS 2 Jazzy, RViz, Gazebo, Python | Early setup and modeling work; integration pending |

The NVIDIA **Jetson Orin** was considered as a more powerful AI computer but was too expensive for this stage. The Raspberry Pi remains my selected board.

## 5. High-level and low-level control

### Raspberry Pi 5 — high-level tasks

- Capture camera images.
- Run lightweight object recognition and grasp selection.
- Run ROS 2 nodes for system communication and monitoring.
- Send the chosen grasp to the ESP32-S3.

The model may be trained or fine-tuned on a separate computer or cloud service and then deployed for inference on the Pi.

### ESP32-S3 — low-level tasks

- Read the conditioned MyoWare muscle signal.
- Read five fingertip FSR channels and, if added, the conditioned piezo sensor.
- Read the IR temperature module.
- Send PWM position commands to the chosen conventional servos.
- Control five vibration motors through **separate driver circuits**.
- Exchange commands and status with the Raspberry Pi.

The ESP32-S3 can generate PWM commands without a separate smart-servo driver board, but **the servos cannot be powered from its GPIO pins**. A suitable high-current servo supply is required. The final pin map depends on the exact development board.

## 6. Finger movement and grasp feedback

The original V2 concept uses opposing tendon paths, so one direction of servo motion closes a finger mechanism and reversing the spool opens it. I plan to reuse the printed V2 spool design where possible.

The **270° servo** is a current preference because it may pull more tendon than a 180° servo without needing a larger spool. This is not a confirmed replacement. I still need to measure:

- space available in the V2 palm;
- output-shaft/horn attachment to the printed spool;
- required tendon movement from open to closed;
- spool size and winding clearance;
- torque, current and reliable operating limits.

I plan to test one finger and one replacement servo before purchasing all five.

For pressure feedback, I will begin with one small FSR on one finger, then expand to all five once its size, wiring, mounting and signal quality are verified. FSRs can help detect contact and changes in grip pressure, but do not directly measure tendon tension or guarantee that objects cannot be crushed. Mechanical travel limits and safe command limits will also be needed.

## 7. Slip, temperature and haptic feedback

**Slip:** Pressure changes alone cannot reliably prove that an object has slipped. I may add one piezoelectric film sensor to an index finger and compare stable holds against intentional sliding and motor vibrations. The piezo requires a protective conditioning circuit before connecting to an ESP32 analog input. A slip alert or automatic correction will only be described as working after tests.

**Temperature:** I prefer a non-contact MLX90614 IR sensor near the wrist camera, pointed toward the grasp area. It could warn of unusually hot or cold objects before contact. The exact field of view, distance, mounting and effects of reflective surfaces need testing. It is **not** a certified burn-prevention feature.

**Haptics:** I plan to use five small vibration motors on the sleeve, one corresponding to each fingertip. The ESP32 will control them through individual motor-driver circuits. I will investigate different vibration patterns for ordinary contact, high pressure and possible slip/temperature warnings, without making the signals confusing.

## 8. Wearable EMG sleeve

For initial EMG experiments, I intend to use the MyoWare sensor and standard gel electrode pads. I will then experiment with reusable conductive-fabric electrodes sewn into an adjustable sleeve, following the [MyoWare fabric electrode guide](https://myoware.com/project/conductive-fabric-electrodes/).

The MyoWare Cable Shield allows the electrode contacts to be positioned away from the MyoWare board. It does not replace the sensor amplifier and **does not provide electrical isolation**.

**Safety requirement:** Any skin-connected electronics need an appropriately isolated, body-safe power and communication setup. I must verify this arrangement before on-body experiments. I will not connect worn electrodes through an unisolated electrical path to a mains-powered computer, charger, Pi or servo supply. I will also investigate vibration-motor interference with the EMG readings.

## 9. CAD and simulation workflow

My intended workflow is:

```text
Review actual Yeah Hand V2 and V1 CAD
    ↓
Adapt hand-to-wrist and wrist-to-forearm fit in Fusion 360
    ↓
Check finger pivots, servos, spools and cable paths
    ↓
Export links, meshes and URDF/Xacro
    ↓
Check joint positions and motion in RViz
    ↓
Test simplified finger motion and grasping in Gazebo
    ↓
Link ROS 2 control to the physical ESP32 system
    ↓
Compare simulation with prototype tests
```

My early ROS 2 Jazzy/Xacro/RViz work is exploratory. I have **not** yet confirmed a complete simulated V2/V1 hybrid. The first simulation may model finger joints and grasping without fully reproducing fishing-line physics. This approximation must be stated clearly in my report.

The manual wrist may initially be represented by selecting one of the three fixed wrist angles for each simulation test.

## 10. Planned testing and measurements

| Test | What I want to find out |
|---|---|
| Camera / vision | Object recognition and grasp-selection accuracy on a small set of objects |
| Muscle sensor | How reliably calibrated contraction signals trigger movement; latency and false triggers |
| One-finger actuation | Full open/close movement, tendon travel, jamming and repeatability |
| Grasping | How consistently the hand grasps and holds different objects |
| FSR sensing | Contact detection, relative force response and ability to stop or limit closing |
| Haptic feedback | Response time and whether the user can distinguish vibration locations/patterns |
| Slip investigation | Whether a piezo sensor distinguishes slip from ordinary movement |
| Temperature | IR sensor behavior with distance, angle and different surfaces |
| Wrist | Whether all three positions lock securely and cables remain protected |
| Power and safety | Servo current demands, voltage stability and safe shutdown/release behavior |
| Simulation | Whether joint directions, ranges and basic grasp motion match the physical design |

Actual test methods and results will be added as the parts are assembled.

## 11. Failure handling and engineering limits

These are planned safety and reliability measures, **not implemented features yet**:

- Stop additional closing when measured pressure exceeds a calibrated limit.
- Set servo position and movement limits; avoid relying on FSRs alone.
- Define a safe response for lost Pi communication or invalid grasp predictions.
- Provide a manual way to stop or release the grasp, subject to the actuator mechanism.
- Check what happens when power fails while the fingers are gripping an object.
- Provide cable strain relief through the manual wrist and removable electronics access.
- Keep electrical isolation and skin safety separate from normal motor power design.

## 12. Build and purchasing stages

**Stage 1 — Initial computing and EMG components:** Purchasing requests prepared for Raspberry Pi 5 kit, camera/cable, MyoWare sensor, Cable Shield, electrode cable and pads. Submission, payment and delivery are not confirmed by these forms.

**Stage 2 — One-finger proof of concept:** Confirm V2 mechanical measurements; test one 270° servo, spool and dual tendons; add one FSR and one vibration motor.

**Stage 3 — Complete hand mechanics:** Finish the V2 upper hand and V1 forearm fit, build the manual wrist and choose the remaining servos, line, PTFE tubes and fasteners.

**Stage 4 — Extra sensing and sleeve:** Develop five-zone haptics, investigate piezo slip and IR temperature, and evaluate the reusable EMG sleeve.

**Stage 5 — Simulation and integration:** Connect ROS 2, object recognition, ESP32 control and physical hand; perform planned tests and document results.

These stages may overlap where practical.

## 13. Design questions still to resolve

1. Which **270° positional PWM servo** fits the V2 mount and provides sufficient torque and tendon travel?
2. What changes are needed to the V2 spool-to-servo horn?
3. How should the V1/V2 wrist adapter lock and protect wiring at ±90°?
4. Can the selected FSR fit the fingertip and give a repeatable signal?
5. Which five vibration motors, drivers and power rails will be used?
6. What is the best IR temperature sensor field of view and mounting angle?
7. Is piezo-based slip sensing reliable enough to justify implementation?
8. How will the safe, electrically isolated MyoWare-to-controller interface be achieved?
9. How will the servos and Pi be powered during bench tests and in a later portable version?
10. What grasp types and household objects make a realistic demonstration and evaluation set?

## 14. Related project documents

- [Component Research and Decision Log](Component_Research_and_Decision_Log.md) — component alternatives and reasons for choosing them.
- [ROS 2 Setup](ros2/01_Setup.md) — earlier setup notes.
- [First Xacro Model](ros2/02_First_Xacro_Model.md) — early modeling work.
- [Yeah Hand repository](https://github.com/opsobot/yeah-hand) and [original parts list](https://github.com/opsobot/yeah-hand/blob/main/hardware/BOM.md).
- [MyoWare conductive-fabric guide](https://myoware.com/project/conductive-fabric-electrodes/).

This is a working overview for my individual project. Items described as **planned, selected, under investigation or requested** have not automatically been built, purchased or tested.
