# Dataset Preparation and Quality Assurance

1. Begin with a 14-class pilot assembled from externally sourced labeled object images.
2. Focus the next iteration on five relevant classes: bottle, tennis_ball, pen, bag, phone.
3. Remap source labels to the final class IDs and remove or review labels/classes outside scope to prevent incorrect background labeling.
4. Add the Water Bottle v21, Pen Detection v5 and Phones v1i sources.
5. Inspect matching image/label filenames, expected five YOLO annotation fields, class ID range and normalized coordinate values.
6. Check cross-split duplicate and near-duplicate examples; remove 15 suspected near-duplicate training examples.
7. Preserve the final cleaned counts: train 4,630; val 374; test 184.
8. Keep raw exports, the merged intermediate dataset and cleaned final dataset separate on the SSD.

**Caveat:** Automated QA and removal of 15 suspected near-duplicates do not establish that all labels are correct, that the splits contain no similar scenes, or that the dataset generalizes to an unseen user environment. Record provenance and seed/split details when reproducible.

The production checkpoint from the successful first five-class run resides in `runs/prosthetic_5class_v1-2/weights/best.pt` in the local project workspace.