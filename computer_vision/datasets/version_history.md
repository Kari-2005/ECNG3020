# Vision Dataset Version History and QA

**Scope:** Source collection and successive experimental datasets. Counts below are recorded from the development process; they do not independently prove absence of leakage or label errors.

| Version | Classes | Train | Validation | Test | Total | Notes |
|---|---:|---:|---:|---:|---:|---|
| Two-class tennis/apple | 2 | 438 | 124 | 68 | 630 | Class IDs normalized; apple polygons converted |
| Cylindrical pilot | 4 | 1,063 | 251 | 106 | 1,420 | bottle/can/cup/tumbler; invalid can-damage categories excluded |
| Updated tripod pilot | 5 | 1,760 | 241 | 330 | 2,331 | fork/spoon/pen/pencil/marker; improved spoon and marker sources |
| Combined 11-class pilot | 11 | 1,524 | 279 | 223 | 2,026 | Selected balanced subset, not sum of all source images |
| Combined 14-class pilot | 14 | 2,288 | 518 | 366 | 3,172 | Adds bag/jug/medicine_box as provisional/stretch categories |
| Focused five-class dataset | 5 | 4,630 | 374 | 184 | 5,188 | bottle/tennis_ball/pen/bag/phone; additional sources; 15 suspected near-duplicates removed |

## Data processing issues encountered
1. **Conflicting class IDs:** Several downloaded datasets labeled their own object as `0`; naïvely concatenating the annotations would merge unrelated categories. Remap every source class to a global class table.
2. **Mixed annotation formats:** Some apple, pen and pencil exports contained segmentation polygons, requiring bounding-box conversion for the detection task. Review resulting boxes visually.
3. **Misleading source semantics:** One can source annotated damage classes rather than whole cans, and an early marker source used the name `Acrylic Plastic`. Those cannot be imported blindly as object classes.
4. **Classification-only apples:** Another apple source had **103 images without detection bounding boxes**. Those images were kept aside for annotation, not counted as supervised detection examples in the original two-class pilot.
5. **Numerically labeled categories:** The bag source had six numbered classes and the medicine-box source had 23 product categories. They were collapsed to bag and medicine_box, respectively, for the 14-class pilot. The interpretation needs human review; medicine_box is not automatically a general box detector.
6. **Unbalanced splits:** Some sources had unusually small/no test sets, e.g. jug. A provisional split is not equivalent to a genuinely independent external evaluation.
7. **Background/false positives:** A two-class webcam test reported a non-target scene region labeled tennis_ball. Include correctly unannotated negative scenes without *any* target-category instances, challenging background views and other curved objects.
8. **Near-duplicate/augmentation leakage:** Check source image families and capture sessions across train, validation and test. The later five-class preparation notes report removing 15 suspected near-duplicate training images; this does not certify the remainder.

## Source/license handling
The dataset sources and candidate versions are recorded in [sources.md](sources.md). Preserve each downloaded `data.yaml`, original ZIP, license, creator/workspace, version and any transformations. **A Roboflow export being downloadable is not itself proof that all underlying image rights permit redistribution.**

## Label and evaluation QA before final report
- Confirm every class ID against the intended canonical list; check normalized box coordinates and corresponding image files.
- Inspect a stratified sample per class (including small/occluded objects and apparent negatives); verify no relevant objects go unlabeled.
- Keep final held-out test images and physical objects independent of training capture sessions.
- Record split seed, source versions, training scripts and package versions.
- Report per-class precision/recall/AP and failure cases, not isolated webcam confidence scores as overall accuracy.

Large ZIPs and weights remain on the SSD rather than in regular Git tracking.
