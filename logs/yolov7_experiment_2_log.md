18-07-2024

- Objective:
  Train yolov7 model on fold1

- Configuration:
  - Model: yolov7
  - Hyperparameters:
    hyperparameters: lr0=0.01, lrf=0.1, momentum=0.937, weight_decay=0.0005, warmup_epochs=3.0, warmup_momentum=0.8, warmup_bias_lr=0.1, box=0.05, cls=0.3, cls_pw=1.0, obj=0.7, obj_pw=1.0, iou_t=0.2, anchor_t=4.0, fl_gamma=0.0, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, degrees=0.0, translate=0.2, scale=0.9, shear=0.0, perspective=0.0, flipud=0.0, fliplr=0.5, mosaic=1.0, mixup=0.15, copy_paste=0.0, paste_in=0.15, loss_ota=1
  - Namespace:
    Namespace(adam=False, artifact_alias='latest', batch_size=16, bbox_interval=-1, bucket='', cache_images=True, cfg='', data='data/my_data.yaml', device='0', entity=None, epochs=60, evolve=False, exist_ok=False, freeze=[0], global_rank=-1, hyp='data/hyp.scratch.p5.yaml', image_weights=False, img_size=[500, 500], label_smoothing=0.0, linear_lr=False, local_rank=-1, multi_scale=False, name='fold1', noautoanchor=False, nosave=False, notest=False, project='runs/train', quad=False, rect=False, resume=True, save_dir='runs/train/fold1', save_period=-1, single_cls=False, sync_bn=False, total_batch_size=16, upload_dataset=False, v5_metric=False, weights='./runs/train/fold1/weights/last.pt', workers=8, world_size=1)

- Dataset Used:
  - fold1

- Results:
  - fold1 was run with command $python train.py --batch 16 --cfg cfg/training/yolov7.yaml --epochs 60 --data data/my_data.yaml --weights yolov7.pt --device 0 --cache-images --name fold1 --img-size 512 --resume . --resume due to multiple crashes
  - Results and analysis can be seen in yolov7/runs/train/fold1 and yolov7_training_report_20240721
  - Detection on fold1 test set was done by running command $python detect.py --weights runs/train/fold1/weights/best.pt --source ../fold1/test/images --conf 0.5 --img-size 512 --save-txt --save-conf --name fold1_test_results
  - It shows good results
  - The best weigths from training fold1 was used to test fold1 test set.
  - Results and analysis can be found in yolov7/runs/test/fold1_test_results_metrics and yolov7_training_report_20240721
  - These weights were also used to perform detection on random images from google
  - Results and analysis can be found in yolov7/runs/detect/predict* and yolov7_training_report_20240721

- Observations:
  - Error Encountered: while running $python train.py --batch 16 --cfg cfg/training/yolov7.yaml --epochs 60 --data data/my_data.yaml --weights yolov7.pt --device 0 , a system crash occured after one epoch had been trained and I decided to run again, this time by caching images and with the weights from the 1st epoch but got error wandb.sdk.lib.config_util.ConfigError: Attempted to change value of key "opt" from ... If you really want to do this, pass allow_val_change=True to config.update(). This error was fixed by adding allow_val_change=True on line 100 in the wandb.init function
  - Error Encountered: after previous error, training randomly stopped after one epoch. Decided to avoid all wandb errors by deleting the project from wandb website
  - The project was deleted from wandb and run from scratch


- Conclusions:
  - Successful setup of yolov7 model which can train custom dataset (fold1). Good results shown with room for improvement
 
