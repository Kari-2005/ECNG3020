# Computer Vision — How I Plan to Connect It to the Hand

## Where things stand

I've tested the five-object YOLO model and the MediaPipe gesture recognizer separately on a laptop. MediaPipe has recognized **an open palm (high-five), closed fist (fist bump) and thumbs up**. I haven't tested both models at the same time or connected them to the physical prosthetic yet.

## What I want the system to do

1. Use the Raspberry Pi camera to look at what is in front of the prosthetic.
2. Use my trained YOLO26n model to recognize a bottle, tennis ball, pen, bag or phone and suggest a suitable grasp.
3. Use MediaPipe as another vision option to recognize a high-five, fist bump or thumbs up.
4. Decide which hand posture makes sense, but **not move the motors based only on the camera**.
5. Have the user confirm movement using the EMG signal.
6. Send the intended movement to the ESP32-S3, which will control the servos while checking limits and sensor feedback.

For a high-five the hand could open. For a fist bump it could make a fist. I still have to see if the tendon-driven hand can make a convincing thumbs up with the planned thumb design. These movements are ideas, not completed physical tests.

## Things I still need to work on

- Test both vision approaches together.
- See what frame rate I can get on the Raspberry Pi 5.
- Check performance under different camera angles and lighting.
- Set up communication between the Pi and ESP32-S3.
- Test finger movements and limits without relying on camera input first.
- Keep the EMG confirmation and safety controls in the final system.

If there is time, I may look at handshake detection. For now, the three working social gesture categories are enough for this part of the project.
