# Experiment 06 — MediaPipe Social Gesture Recognition

**Goal:** Recognize simple social gestures using a webcam as an optional extension of the prosthetic hand's interaction capabilities.

**Current demonstrated gestures:**

| MediaPipe category | Displayed interaction | Confidence in captured example |
|---|---|---:|
| `Open_Palm` | HIGH FIVE | 0.70 |
| `Closed_Fist` | FIST BUMP | 0.89 |
| `Thumb_Up` | THUMBS UP | 0.72 |

**Implementation:** MediaPipe Tasks Gesture Recognizer, OpenCV webcam input, up to one detected hand, 21 estimated landmarks displayed, model confidence threshold 0.65, and temporal vote requirement of five matching classifications within a seven-frame window.

**Contribution:** The original two-gesture prototype was extended to recognize `Thumb_Up` and tested successfully. Captured screenshots show each respective label and hand landmarks. They are demonstration frames, not a formal benchmark.

**Limitations:** Hand shape is not the same as social intent. An open palm could be a wave; a closed fist might not be an invitation to fist-bump. Stability across people, environments, angles and lighting has not yet been systematically evaluated.

**Planned prosthetic interaction:** Map recognized gestures to a *candidate* open-hand, closed-fist or thumbs-up posture (subject to mechanics); require safe user/EMG confirmation before motion. No actuation was performed during this experiment.

**Future extension:** Handshake-offer detection remains optional and has not been implemented.

**Local setup:** Put `gesture_recognizer.task` in `models/` under the local computer-vision project, then run the social gesture test via its Python environment.

**Code:** [Original webcam test](../../test_social_gestures.py) and [organized-folder copy](../../scripts/testing/test_social_gestures.py). The three webcam screenshots were captured during testing; the recorded confidence values are individual examples, not overall classification accuracy.
