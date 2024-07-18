18-07-2024

- Objective:
  Train yolov7 model on fold1, then on fold2 with (different hyperparamters and configurations --evolve --cache-images --name "fold2")

- Configuration:
  - Model: yolov7
  - Hyperparameters:
    hyperparameters: lr0=0.01, lrf=0.1, momentum=0.937, weight_decay=0.0005, warmup_epochs=3.0, warmup_momentum=0.8, warmup_bias_lr=0.1, box=0.05, cls=0.3, cls_pw=1.0, obj=0.7, obj_pw=1.0, iou_t=0.2, anchor_t=4.0, fl_gamma=0.0, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, degrees=0.0, translate=0.2, scale=0.9, shear=0.0, perspective=0.0, flipud=0.0, fliplr=0.5, mosaic=1.0, mixup=0.15, copy_paste=0.0, paste_in=0.15, loss_ota=1
  - Namespace:
    Namespace(adam=False, artifact_alias='latest', batch_size=16, bbox_interval=-1, bucket='', cache_images=False, cfg='cfg/training/yolov7.yaml', data='data/my_data.yaml', device='0', entity=None, epochs=1, evolve=False, exist_ok=False, freeze=[0], global_rank=-1, hyp='data/hyp.scratch.p5.yaml', image_weights=False, img_size=[640, 640], label_smoothing=0.0, linear_lr=False, local_rank=-1, multi_scale=False, name='exp', noautoanchor=False, nosave=False, notest=False, project='runs/train', quad=False, rect=False, resume=False, save_dir='runs/train/exp5', save_period=-1, single_cls=False, sync_bn=False, total_batch_size=16, upload_dataset=False, v5_metric=False, weights='yolov7.pt', workers=8, world_size=1)

- Dataset Used:
  - My cutom dataset
    - 5973 images of wheat, soybean, and sunflower
    - Preprocessing: Augmentations applied , and split into 3 folds each with train, val, test ratio of 70:15:15

- Results:
  - wandb: Run data is saved locally in /home/agx/agro_sky_ai/AgroSkyAI/models/yolov7/wandb/run-20240716_204753-leip73f6
  - 1 epochs completed in 0.422 hours.
  - metrics/mAP_0.5 0.49339
    metrics/mAP_0.5:0.95 0.17343
    metrics/precision 0.54109
	metrics/recall 0.56198
	train/box_loss 0.06677
	train/cls_loss 0.01194
	train/obj_loss 0.0395
	  val/box_loss 0.07447
	  val/cls_loss 0.015
	  val/obj_loss 0.08012
	         x/lr0 0.00261
	         x/lr1 0.00261
	         x/lr2 0.07651

- Observations:
  - Error Encountered: During initial setup, encountered ImportError: /home/agx/agro_sky_ai/AgroSkyAI/agro_venv/lib/python3.8/site-packages/torch/lib/../../torch.libs/libgomp-4dbbc2f2.so.1.0.0: cannot allocate memory in static TLS block.
  - Solution: Resolved the issue by $export LD_PRELOAD=/home/agx/agro_sky_ai/AgroSkyAI/agro_venv/lib/python3.8/site-packages/torch.libs/libgomp-4dbbc2f2.so.1.0.0
  - Error Encountered: To run the yolov7 model on jetson nano device, special pytorch wheel is needed andtypical pytorch from pip3 install cannot be used, giving error to "no cuda device available".
  - Solution: proper pytorch to install can be found from these sources:
  	site: https://elinux.org/Jetson_Zoo#PyTorch_.28Caffe2.29
	forum: https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048
	code used during this test to install pytorch: pip3 install https://developer.download.nvidia.com/compute/redist/jp/v512/pytorch/torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl
	torchvision also needs to be accordingly installed by following the instructions section in the forum - pip install setuptools==69.5.1 might be needed to be run.


- Conclusions:
  - Successful setup of yolov7 model which can train custom dataset
 
