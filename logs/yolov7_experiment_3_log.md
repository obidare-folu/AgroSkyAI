22-07-2024

- Objective:
  Train yolov7 model on fold2

- Configuration:
  - Model: yolov7
  - Hyperparameters:
    hyperparameters: lr0=0.001, lrf=0.1, momentum=0.937, weight_decay=0.0005, warmup_epochs=3.0, warmup_momentum=0.8, warmup_bias_lr=0.1, box=0.05, cls=0.3, cls_pw=1.0, obj=0.7, obj_pw=1.0, iou_t=0.2, anchor_t=4.0, fl_gamma=0.0, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, degrees=0.0, translate=0.2, scale=0.9, shear=0.0, perspective=0.0, flipud=0.0, fliplr=0.5, mosaic=1.0, mixup=0.15, copy_paste=0.0, paste_in=0.15, loss_ota=1
  - Namespace(adam=True, artifact_alias='latest', batch_size=16, bbox_interval=-1, bucket='', cache_images=True, cfg='', data='data/fold2.yaml', device='0', entity=None, epochs=30, evolve=False, exist_ok=False, freeze=[0], global_rank=-1, hyp='data/hyp.fold2.yaml', image_weights=False, img_size=[512, 512], label_smoothing=0.0, linear_lr=False, local_rank=-1, multi_scale=False, name='fold2', noautoanchor=False, nosave=False, notest=False, project='runs/train', quad=False, rect=False, resume=True, save_dir='runs/train/fold2', save_period=-1, single_cls=False, sync_bn=False, total_batch_size=16, upload_dataset=False, v5_metric=False, weights='./runs/train/fold2/weights/last.pt', workers=8, world_size=1)

- Dataset Used:
  - fold2

- Results:
  - fold2 was run with command $!python train.py --batch 16 --cfg cfg/training/yolov7.yaml --epochs 30 --data data/fold2.yaml --weights runs/train/fold1/weights/best.pt --device 0 --cache-images --name fold2 --img-size 512 --hyp data/hyp.fold2.yaml --adam .
  - Results and analysis can be seen in yolov7/runs/train/fold2 and yolov7_training_report_20240722
  - Detection on fold2 test set was done by running command $!python detect.py --weights runs/train/fold2/weights/best.pt --source ../fold2/test/images --conf 0.5 --img-size 512 --iou-thres 0.5 --save-txt --save-conf --name fold2_detect_results_conf0.5
  - It shows good results
  - The best weigths from training fold2 was used to test fold2 test set.
  - Results and analysis can be found in yolov7/runs/test/fold2_test_results_metrics and yolov7_training_report_20240722
  - These weights were also used to perform detection on random images from google
  - Results and analysis can be found in yolov7/runs/detect/predict* and yolov7_training_report_20240722

- Observations:


- Conclusions:
  - Successful training of fold2 dataset. Good results shown with room for improvement.
 
