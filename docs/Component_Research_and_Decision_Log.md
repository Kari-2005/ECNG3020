# Component Research and Decision Log
**ECNG 3020 — Robotic Prosthetic Hand with Haptic Tactile Feedback**

**Working document:** 20 October 2026  
**Student:** Ansarah Mohammed  
**Supervisor:** Dr Sean Rocke

This is a simple record of the parts I compared and why. It is not the final Bill of Materials and does not confirm that any items have been bought.

## 1. My project plan
I am combining the Yeah Hand V2 fingers, palm, tendons and spools with the Yeah Hand V1 forearm below the wrist. I want a manually rotating wrist that locks at −90°, 0° and +90°. A camera will help identify objects and choose a grasp. A muscle sensor will tell the hand when to grasp. Fingertip sensors will help control grip pressure and send vibration feedback to the user.

**Computer choice:** Raspberry Pi 5 (4GB) starter kit. I also considered the NVIDIA Jetson Orin, but it was much more expensive for what my first prototype needs. The Raspberry Pi remains on my purchasing request.

## 2. How I compare parts
For each main part, I compare at least three choices, explain my preference and state what still needs checking. I use four labels: chosen for planning, included on a purchase request, still being considered, and already available. These labels do not mean tested or paid for.

## 3. Main computer
**What I need:** Run the object-recognition model, help choose a grasp and communicate with the ESP32-S3.

| Option | Good points | Drawbacks / decision |
|---|---|---|
| Raspberry Pi 4 | Usually cheaper and can run small AI models. | Slower than Pi 5 when running the camera and ROS 2 together. |
| Raspberry Pi 5 (4GB / 8GB) | Faster than Pi 4, well documented, and works with my chosen camera. | 4GB selected to save money; 8GB costs more than I need for a small model. |
| Raspberry Pi 5 AI add-on / heavier compute | Could speed up some AI work if needed later. | Extra cost; not necessary for my planned lightweight model. |
| NVIDIA Jetson Orin | Powerful hardware for running AI models on a device. | Much more expensive; not chosen because Pi 5 can handle my planned first prototype. |

**Current decision:** Raspberry Pi 5 (4GB). The Jetson Orin was considered but was too costly for this stage.

**Still to check:** Set up Ubuntu 24.04 and ROS 2 Jazzy, then test the camera and a small AI model on the Pi 5.

## 4. Camera and position
**What I need:** See objects as the hand moves toward them.

| Option | Good points | Drawbacks / decision |
|---|---|---|
| Camera Module 3 Standard | Clear autofocus image; narrower view. | May miss nearby objects when mounted close to the wrist. |
| Camera Module 3 Wide | Wider view and closer focusing, useful for my angled wrist mount. | More lens distortion; I will test the camera angle on the wrist. |
| Raspberry Pi AI Camera | Can run some AI models directly on the camera. | Costs more and has extra model-conversion steps. |

**Current decision:** Raspberry Pi Camera Module 3 Wide, placed on a small angled mount near the wrist. It is included on the DigiKey purchasing request.

**Still to check:** Test camera connection with the Pi 5, and check the view, finger blockage and cable slack through wrist rotation.

## 5. Muscle-sensing module (EMG)
**What I need:** Measure muscle contraction to trigger the selected grasp.

| Option | Good points | Drawbacks / decision |
|---|---|---|
| AD8232 ECG module | Low price. | Primarily designed for heart signals, not my preferred muscle-sensing approach. |
| DFRobot SEN0240 | Comes with reusable dry electrodes. | Rigid contacts may be less comfortable inside my sleeve. |
| MyoWare 2 (DEV-27924) | Made for measuring muscle signals and has useful guides. | Needs pads, safe power/interface arrangements and optional accessories. |

**Current decision:** MyoWare 2 is on my DigiKey request, with a Cable Shield and three-electrode cable.

**Still to check:** Test the signal with a properly isolated body-safe setup. Check ESP32 connections before wearing electrodes.

## 6. Electrode pads and sleeve
**What I need:** Measure EMG now and later make a reusable sleeve.

| Option | Good points | Drawbacks / decision |
|---|---|---|
| Disposable gel ECG/EMG pads | Simple for first tests and comparing results. | DFRobot FIT0510 has a 4 mm snap stud (checked by student); test physical fit and signal quality when it arrives. |
| Reusable TENS gel pads | Can be used more than once. | Connector, comfort and recording quality still uncertain. |
| Conductive fabric contacts in a sleeve | Reusable and can be made to fit my design. | Needs sewing and testing for signal quality. |
| Rigid dry electrodes | Reusable without sticky pads. | Can move or press uncomfortably on skin. |

**Current decision:** Use suitable disposable pads for early measurements, then try a homemade conductive-fabric sleeve.

**Still to check:** Confirm the pads snap securely onto the SparkFun 12970 cable during assembly, and keep vibration motors away from EMG contacts. The FIT0510 pad snap size was checked as 4 mm (user verification).

## 7. Hand and wrist
**What I need:** Build a working tendon-driven hand without redesigning everything.

| Option | Good points | Drawbacks / decision |
|---|---|---|
| Yeah Hand V2 alone | Has an existing tendon and spool design. | Does not give me the V1 forearm I want. |
| Yeah Hand V2 + V1 forearm | Keeps the V2 moving hand and adds the forearm and custom wrist. | Needs CAD changes at the wrist connection. |
| InMoov / Jensen hands | Useful examples of lower-cost actuation. | Switching hand designs would change my existing CAD and simulation plans. |

**Current decision:** Keep V2 above the wrist and V1 below it. The servos stay in the V2 upper hand.

**Still to check:** Model and test the three-position manual wrist, cable routing and mount strength.

## 8. Servos
**What I need:** Wind the V2 spools enough to fully open and close the fingers.

| Option | Good points | Drawbacks / decision |
|---|---|---|
| Waveshare ST3215 smart servo | Original V2 choice; position feedback and matching motor design. | More expensive; needs a serial-bus interface. |
| 180° ordinary PWM servo | Cheaper and connects to ESP32 PWM. | May not turn far enough to pull all required fishing line. |
| 270° ordinary PWM servo | More possible travel with simpler PWM control. | Size, strength and spool attachment must be tested. |
| 360° continuous rotation servo | Can spin repeatedly. | Usually controls speed rather than exact position; not my preferred spool control. |

**Current decision:** Try one 270° metal-geared positional PWM servo first. No replacement model is fully confirmed yet.

**Still to check:** Measure V2 motor space, required tendon travel, spool radius, torque, power and servo horn before ordering five.

## 9. Tendons and tubing
**What I need:** Pull each finger closed and open.

| Option | Good points | Drawbacks / decision |
|---|---|---|
| Two braided tendon lines | Keeps V2 active opening and closing using the printable dual-action spools. | Requires tensioning and smooth routing. |
| One line plus elastic return | Simpler and may be cheaper. | Changes the chosen V2 mechanism. |
| Move servos into forearm | Creates more palm space. | Tendons passing through my rotating wrist would be harder to route. |

**Current decision:** Keep two opposing braided lines per finger, roughly 0.75 mm / 200 lb eight-strand line, and PTFE guides around 3 mm outer / 1.5 mm inner diameter as previously shortlisted.

**Still to check:** Check actual V2 files and buy the correct length only after measuring. Elastic return is not needed if the dual-tendon design works.

## 10. Fingertip pressure sensors
**What I need:** Feel when the hand touches an object, regulate grip and send feedback.

| Option | Good points | Drawbacks / decision |
|---|---|---|
| FSR 400 Short | Small sensing area; easy to read with ESP32. | Needs good mounting and calibration. |
| FSR 402 | Larger sensing surface. | Might be too wide for V2 fingertips. |
| Capacitive or multi-point tactile sensor | Could show more detail about contact. | More expensive and difficult to fit and program. |

**Current decision:** Start with one FSR 400 Short on a test finger. Plan for five fingertips plus one spare if sizing works.

**Still to check:** Measure fingertip size in Fusion 360. Check sensor response under a soft contact pad.

## 11. Slip sensing
**What I need:** Notice when an object may be moving out of the grip.

| Option | Good points | Drawbacks / decision |
|---|---|---|
| FSR changes only | No extra sensor needed. | Pressure change alone does not prove slip. |
| Piezoelectric film | May pick up vibration during slip. | Requires safe signal conditioning and testing against motor vibration. |
| Optical / sensor array method | Potentially measures movement more directly. | Too much extra development for now. |

**Current decision:** Consider one piezo film on the index finger alongside five FSRs. This is not ordered yet.

**Still to check:** Test real slip versus normal gripping and motor vibration. Protect the ESP32 input.

## 12. Temperature sensing
**What I need:** Warn about unusually hot or cold objects without touching them first.

| Option | Good points | Drawbacks / decision |
|---|---|---|
| 10 kΩ thermistor | Small and cheap. | Must touch the object and can respond slowly. |
| MLX90614 infrared sensor | Can estimate surface temperature from a distance. | Needs correct viewing angle and calibration for different surfaces. |
| Thermal camera | Shows temperature across an image. | More cost and processing work. |

**Current decision:** One MLX90614 breakout is the current preference, but no exact part is finalized.

**Still to check:** Choose a breakout compatible with the controller and test it at the planned wrist distance. Do not present it as guaranteed burn protection.

## 13. Vibration feedback
**What I need:** Let the user feel which finger has touched an object.

| Option | Good points | Drawbacks / decision |
|---|---|---|
| 3V coin vibration motors | Compact and relatively inexpensive. | Need a transistor/MOSFET circuit for each motor. |
| Linear resonant actuators | Can make clear vibration patterns. | Need different driver electronics. |
| Electrical stimulation feedback | Another research approach. | More difficult to make safe and comfortable for this project. |

**Current decision:** Plan for five coin vibration motors in the sleeve and two optional spares.

**Still to check:** Choose the motor rating, five driver circuits and a suitable supply; test one motor first.

## 14. Software
**What I need:** Build the design, simulation and AI control.

| Option | Good points | Drawbacks / decision |
|---|---|---|
| Fusion 360 | Use for printed parts and my wrist/servo changes. | Joints must be checked after export. |
| ROS 2 Jazzy + Gazebo | Supports the proposal’s simulation work. | Simulation will simplify real tendon behavior. |
| Firmware-only control | Simple way to move the physical hand. | Does not meet the simulation part of the project alone. |

**Current decision:** Continue Fusion 360 and ROS 2 Jazzy/Gazebo. Use ESP32-S3 firmware for sensing, servo control and haptics.

**Still to check:** Test ROS 2 Jazzy, the Camera Module 3 Wide and the AI model on the Raspberry Pi 5.

## 15. First purchasing requests — selected, not confirmed received
The October 2026 forms list a TRASKIT Raspberry Pi 5 4GB kit at US$179.99 and DigiKey components at US$105.20, plus US$4.99 shipping and an estimated US$8.65 tariff (DigiKey total US$118.84). Combined estimated amount: **US$298.83**. These are purchasing requests, not proof that the items were delivered.

DigiKey items listed: MyoWare 2 DEV-27924 (1), Cable Shield 18386 (1), electrode cable 12970 (1), DFRobot FIT0510 12-pad pack (2), Raspberry Pi Camera Module 3 Wide SC1224 (1), Raspberry Pi 5 camera cable SC1130 (1).

The Raspberry Pi 5, Camera Module 3 Wide and Pi 5 camera cable remain the selected parts. The Jetson Orin was a more expensive alternative and is not in these purchasing requests.

## 16. Still to buy or confirm
**Compute:** Set up and test Raspberry Pi 5.  
**EMG:** Verify snap connection during assembly and plan a safe isolated sensing setup.  
**Hand:** Test one 270° servo, then choose servo power, fishing line, PTFE tubing, screws and printed parts.  
**Feedback:** Choose FSRs, piezo sensor, IR temperature sensor, vibration motors and drivers.

## 17. Reference links and documents
- Department ECNG 3020 Bill of Materials Template (uploaded): at least three alternatives for each major component and clear reasons for the choice.
- Amazon first purchasing request (uploaded): selected TRASKIT Raspberry Pi 5 4GB kit.
- DigiKey first purchasing request (uploaded): selected MyoWare and Raspberry Pi camera items.
- [Yeah Hand project](https://github.com/opsobot/yeah-hand)
- [Yeah Hand parts list](https://github.com/opsobot/yeah-hand/blob/main/hardware/BOM.md)
- [MyoWare conductive fabric guide](https://myoware.com/project/conductive-fabric-electrodes/)
- [MyoWare sensor listing](https://www.digikey.com/en/products/detail/sparkfun-electronics/DEV-27924/26769978)
- [Camera Module 3 Wide quote](https://www.digikey.com/en/products/detail/raspberry-pi/SC1224/17278644)
