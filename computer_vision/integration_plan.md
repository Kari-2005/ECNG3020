# Computer Vision Integration Plan

## 1. Overview

The computer vision part of the project currently has two experimental functions. The first is a **five-class YOLO26n detector** for everyday objects (bottle, tennis ball, pen, bag and phone). The second is a **MediaPipe gesture recognizer** that has detected an open palm, a closed fist and a thumbs up in webcam tests.

I want to use the vision system to help select hand postures, but not to let it control the servos on its own. The intention is still to use EMG from the user's muscles as the signal that confirms or activates movement.

So far both recognition approaches have worked **separately on a Windows laptop**. I haven't yet tested them together, moved them to the Raspberry Pi 5, connected the Pi to the ESP32-S3 or demonstrated a completed grasp with the physical prosthetic.

## 2. Proposed system

```text
Raspberry Pi Camera Module 3 Wide
                |
                v
          Raspberry Pi 5
           /          \
          v            v
  YOLO26n detector   MediaPipe gesture recognizer
   (5 objects)         (3 gestures)
          \            /
           v          v
        Selection / decision logic
                |
       Suggested grasp or posture
                |
       User confirmation from EMG
                |
                v
              ESP32-S3
       /         |          \
    Servos    Finger FSRs   Haptic motors
       |
   Tendon-driven hand
```

This is a planned architecture rather than an implemented block diagram.

## 3. Vision and grasp/posture selection

For object recognition, the Pi would use the trained YOLO model and map the detected category to a suitable grasp. I still need to work out the final mapping based on the actual tendon-driven hand and how many independent movements the fingers can perform.

For the social gestures, I have these possible responses in mind:

| Camera recognition | Proposed response | What still needs checking |
|---|---|---|
| Open palm / high-five | Open-hand posture | Palm orientation and finger travel |
| Closed fist / fist bump | Closed-hand posture | Safe tendon tension, travel and contact |
| Thumbs up | Curl fingers with thumb extended | Whether the thumb design can make this shape reliably |

These camera detections are only **candidates** for a response. For instance, someone could be waving rather than requesting a high-five. I will need a way to handle low-confidence predictions, multiple objects or hands in view, and cases where the object and social gesture models suggest different actions.

## 4. EMG confirmation and controller roles

The Raspberry Pi would handle the camera and higher-level recognition. The ESP32-S3 would deal with the lower-level hardware, including servo commands, sensing and feedback. The planned MyoWare EMG system would provide an intentional muscle contraction signal for the user to confirm when the hand should move.

This also means I need to design a simple communication format between the Pi and ESP32-S3. Before sending servo commands, I want to test this using messages that only print a selected grasp or posture, with no motors attached.

For the eventual physical tests I would need appropriate servo power, movement limits, fingertip pressure feedback, stopping behaviour and a safe electrical arrangement for body-connected EMG sensing. The gesture system should not cause unexpected movement just because someone briefly appears in the camera.

## 5. Testing still required

1. Run YOLO and MediaPipe together on the laptop and measure the effect on speed.
2. Evaluate the YOLO detector on its held-out test split and conduct repeat webcam tests.
3. Test gesture recognition with different distances, orientations, backgrounds and lighting.
4. Deploy the recognition code on the Raspberry Pi 5 and check latency/frame rate.
5. Send test posture labels from the Pi to the ESP32-S3 without servo actuation.
6. Test the tendon-driven hand's actual movement ranges and FSR readings on the bench.
7. Add user confirmation and motion limits before attempting physical gesture responses.

Handshake recognition remains a possible extra feature if the main integration goes well. It is not something the current MediaPipe test script recognizes.
