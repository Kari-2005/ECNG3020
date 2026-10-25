# Vision Development Decisions and Lessons Learned

**ECNG 3020 — October 2026 development record.** This document connects the original design choices with later experiment outcomes. It distinguishes user-reported observations from formal performance measurements.

## Design goal and boundaries
The camera supplies a **suggested** grasp; it must not autonomously drive the prosthetic. Planned chain: camera → object detector → grasp-selection logic → user/EMG authorization → ESP32-S3 and servos, supported by fingertip FSRs and wearable vibration feedback. ROS 2 testing and Raspberry Pi deployment remain separate, unverified integration tasks.

## Decision timeline

| Stage | Decision and reason | Evidence / limitation |
|---|---|---|
| Initial baseline | Start with pretrained **YOLO26n** to avoid training a detector from scratch and keep eventual Pi inference practical | Webcam trials recognized some COCO objects, but performance depended on viewpoint |
| First error | The worn, faded-green tennis ball was repeatedly labeled **apple** | One reported confusion was ~0.66 confidence; anecdotal, not formal accuracy |
| Alternative | Test **YOLO-World** with text prompts for tennis ball, pen, key, bag, pitcher, etc. | Git/CLIP dependency issue fixed; tests still showed tennis-ball/apple confusion and limited recognition |
| Response | Fine-tune original YOLO26n on tennis-ball and apple annotations | 630-image two-class pilot; 10 CPU epochs; user reported the worn ball subsequently recognized |
| Error analysis | Improving one category does not ensure reliable deployment | Apple class remained weak and a non-target scene region triggered a false-positive tennis-ball label |
| Broader grasp coverage | Assemble datasets for cylindrical, spherical and tripod objects; add bag, jug and medicine box as stretch goals | Labelling work included class-ID remapping, polygon conversion, ambiguous source labels, split review |
| 14-class pilot | Test 14 everyday object categories in one YOLO26n rather than running two detectors concurrently | 3,172-image selected pilot; 10 epochs; validation P=.707, R=.671, mAP50=.706, mAP50–95=.511; practical unstable detections |
| Scope refinement | Move to **five focused classes**: bottle, tennis_ball, pen, bag, phone | 30-epoch run recorded P=.880, R=.778, mAP50=.847, mAP50–95=.657 on a *different* validation dataset |
| Social-interaction extension | Trial MediaPipe Gesture Recognizer for high-five, fist bump and thumbs-up candidate postures | Webcam demonstrations; no evidence of wearer intention or hardware actuation |

### Why the 14-class effort was not wasted
The larger pilot revealed annotation and generalization challenges and supplied a foundation for choosing a smaller, testable set of daily-use objects. Focusing the next experiment was an **engineering scope decision**, not proof that fewer classes always perform better. The mAP scores from different datasets cannot be treated as a controlled model comparison.

### Object identification versus grasping
Originally proposed grasp families: cylindrical (bottle/can/cup/tumbler), spherical (tennis ball/apple), tripod (fork/spoon/pen/pencil/marker), lateral pinch (key; dataset not finalized), hook/handle (bag/jug) and palmar (medicine box). These are **candidate mappings**. Physical reach, thumb opposition, grip force, object dimensions and risk controls must be verified before actuation. Phone appears in the later five-class detector but requires a mechanically validated grasp strategy.

### Social gestures
An open palm, fist or raised thumb is a visible pose, not a guaranteed high-five/fist-bump/approval invitation. MediaPipe labels should be treated as suggestions and require user intent confirmation.

### Next evidence requirements
Preserve the *executed* Python scripts, dataset YAMLs and source manifests from the SSD, model weight identifiers, Ultralytics/PyTorch versions, results.csv, confusion matrices, val/test metrics, annotated failure examples, CPU/Pi frame timing and run configuration. Keep dataset licenses and authorship attribution.

See [experiment index](../experiments/README.md), [dataset preparation](../datasets/preparation.md) and [integration plan](../integration_plan.md).
