### 21-07-2024

**Setup and First Training of YOLOv7 Model Successfully Completed**

The YOLOv7 model, obtained from the official GitHub repository, was successfully set up and trained. The setup process encountered several challenges due to the specific library requirements needed to run machine learning models on the Jetson Xavier device. These challenges and their solutions are documented in the `yolov7_experiment_1` log.

**Training Details and Adjustments**

The first official training was conducted on fold1 using 60 epochs, starting from the `yolov7.pt` weights, with a batch size of 16. Initially, an image size of 640 was chosen; however, due to errors such as "NMS time limit exceeded," random device crashes, and overall training speed, the image size was reduced to 512.

Despite encountering issues such as device crashes and random stopping of the training process, a solution was found by disabling all power-saving, sleep, or hibernation settings and keeping the monitor on. This significantly reduced the frequency of random stoppages, though it did not completely eliminate device crashes.

**Validation Results on Fold1**

The training on fold1 yielded promising results on the validation set:

| Class      | Images | Labels | Precision (P) | Recall (R) | mAP@0.5 | mAP@0.5:0.95 |
|------------|--------|--------|----------------|------------|---------|--------------|
| all        | 896    | 14121  | 0.878         | 0.876      | 0.898   | 0.679        |
| soy        | 896    | 1198   | 0.930         | 0.912      | 0.937   | 0.832        |
| sunflower  | 896    | 672    | 0.801         | 0.856      | 0.862   | 0.704        |
| wheat      | 896    | 12251  | 0.903         | 0.860      | 0.894   | 0.499        |

Overall training and validation set metrics:

- **metrics/mAP_0.5**: 0.89756
- **metrics/mAP_0.5:0.95**: 0.67859
- **metrics/precision**: 0.87791
- **metrics/recall**: 0.87601
- **train/box_loss**: 0.02784
- **train/cls_loss**: 0.00023
- **train/obj_loss**: 0.02354
- **val/box_loss**: 0.04801
- **val/cls_loss**: 0.00302
- **val/obj_loss**: 0.07142
- **Learning Rates (x/lr0, x/lr1, x/lr2)**: 0.00102

**Testing Results on Fold1**

The best weights were tested on the fold1 test set with a confidence threshold of 0.5 and an IOU threshold of 0.5, producing the following metrics:

| Class      | Images | Labels | Precision (P) | Recall (R) | mAP@0.5 | mAP@0.5:0.95 |
|------------|--------|--------|---------------|------------|---------|--------------|
| all        | 895    | 14481  | 0.903         | 0.886      | 0.872   | 0.678        |
| soy        | 895    | 1175   | 0.968         | 0.937      | 0.937   | 0.850        |
| sunflower  | 895    | 725    | 0.82          | 0.875      | 0.843   | 0.695        |
| wheat      | 895    | 12581  | 0.92          | 0.845      | 0.836   | 0.489        |

The detection results were accurate and are saved in `yolov7/runs/detect/fold1_test_detections_conf0.5`.

**Additional Testing on Random Images**

Detection was performed on random images from Google at varying confidence thresholds:

- **0.5**: Only sunflowers and a few wheats were detected.
- **0.25**: More sunflowers and wheats were detected, with soy beginning to appear.
- **0.15**: All classes were detected, with sunflower being the easiest, followed by wheat, then soy. The need for a lower confidence threshold for detection can be attributed to the lower representation of soy in the dataset and the inherent difficulty in detecting wheat, as indicated by the metrics.

**Next Steps**

Training will continue on fold2 to further improve the model.

