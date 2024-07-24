### 22-07-2024

**Second Training of YOLOv7 Model Successfully Completed**

The YOLOv7 model, was successfully trained on a different fold of data with differenrt configurations and parameters. The configurations and parameters can be found in the `yolov7_experiment_3` log.

**Training Details and Adjustments**

The training was conducted on fold2 using 30 epochs, starting from the fold1 best weights, with a batch size of 16 and image size 512.

**Training Results on Fold2**

The training on fold2 yielded promising results on the validation set, less acccurate than that of fold1 but providing the first chance of generalizability of the model:

| Class      | Images | Labels | Precision (P) | Recall (R) | mAP@0.5 | mAP@0.5:0.95 |
|------------|--------|--------|---------------|------------|---------|--------------|
| all        | 896    | 14622  | 0.854         | 0.801      | 0.85    | 0.61         |
| soy        | 896    | 1358   | 0.926         | 0.881      | 0.923   | 0.783        |
| sunflower  | 896    | 666    | 0.749         | 0.758      | 0.805   | 0.631        |
| wheat      | 896    | 12598  | 0.886         | 0.765      | 0.822   | 0.417        |

Overall training and validation set metrics:

- **metrics/mAP_0.5**: 0.84974
- **metrics/mAP_0.5:0.95**: 0.61017
- **metrics/precision**: 0.85386
- **metrics/recall**: 0.80139
- **train/box_loss**: 0.03031
- **train/cls_loss**: 0.00043
- **train/obj_loss**: 0.02551
- **val/box_loss**: 0.04925
- **val/cls_loss**: 0.00375
- **val/obj_loss**: 0.08192
- **Learning Rates (x/lr0, x/lr1, x/lr2)**: 0.00011

**Testing Results on Fold2**

The best weights were tested on the fold2 test set with a confidence threshold of 0.5 and an IOU threshold of 0.5, producing the following metrics:

| Class      | Images | Labels | Precision (P) | Recall (R) | mAP@0.5 | mAP@0.5:0.95 |
|------------|--------|--------|---------------|------------|---------|--------------|
| all        | 896    | 14712  | 0.892         | 0.787      | 0.764   | 0.576        |
| soy        | 896    | 1131   | 0.944         | 0.908      | 0.9     | 0.787        |
| sunflower  | 896    | 740    | 0.826         | 0.64       | 0.597   | 0.495        |
| wheat      | 896    | 12841  | 0.907         | 0.795      | 0.795   | 0.446        |

The detection results were accurate and are saved in `yolov7/runs/detect/fold2_test_detections_conf0.5`.

**Additional Testing on Random Images**

Detection was performed on random images from Google at varying confidence thresholds:

- **0.5**: Sunflowers and soy detected, 2 wheat plants detected.
- **0.25**: Sunflowers are easily detected. Soys are also detected to some extent, and only a specific looking type of wheat was detected.
- **0.15**: All classes were detected, with sunflower being the easiest, followed by soy, then wheat.
Fold2 weights showcases a  significant improvement in detecting soy. 

**Next Steps**

Training will continue on fold3 to further improve the model, using tuned paramters and weighted images with also larger image size.

