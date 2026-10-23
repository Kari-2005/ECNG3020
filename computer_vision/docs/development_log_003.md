# Development Log 003 — YOLO-World Investigation and Grasp Mapping

**Period:** October 2026  
**Status:** Exploratory experiment

## Decisions 7–9: Alternative detector
YOLO-World was investigated for open-vocabulary detection using text prompts such as tennis ball, pen, key, grocery bag and pitcher. The checkpoint downloaded, but calling `set_classes()` initially failed because Ultralytics CLIP was missing and Git was not installed/available on PATH. Git and the CLIP dependency were addressed, permitting webcam tests.

In informal tests YOLO-World continued to confuse the worn tennis ball with an apple and recognized only limited additional test objects (including a pen). This did not justify replacing YOLO26n for the project. This is an **exploratory selection outcome**, not a controlled head-to-head benchmark.

## Decision 10: Grasp mapping
Instead of expecting the detector to issue motor commands, translate class names through a separate object-to-grasp mapping. Proposed examples: bottle → cylindrical; tennis_ball → spherical; pen → tripod; bag → hook/handle; jug → handle/body; medicine_box → palmar. These mappings are provisional: orientation, thumb geometry, reachable force and the user's confirmation will affect safe motion.

**Code:** `../scripts/test_yolo_world.py` and `../configs/grasp_mapping_draft.py`. Both are draft reconstructions; grasp mapping does not actuate the prosthetic.

**References:** https://github.com/AILab-CVC/YOLO-World ; https://docs.ultralytics.com/models/yolo-world/
