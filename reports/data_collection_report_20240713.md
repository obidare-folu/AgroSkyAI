13-07-2024

Augmented images from collected data were made.

Augmentation types were taken from this list of augmentations with the helb of albumentations library:

RandomFog(p=1),
RandomBrightnessContrast(p=1, contrast_limit=0.5),
RandomCrop(p=1, height=448, width=448),
Rotate(p=1, limit=90),
RGBShift(p=1),
RandomSnow(p=1),
VerticalFlip(p=1),
HorizontalFlip(p=1),
HueSaturationValue(p=1),
GaussianBlur(p=1),
GaussNoise(p=1),
ElasticTransform(p=1),
Resize(height=512, width=512, p=1),
RandomResizedCrop(height=512, width=512, scale=(0.5, 1.0), p=1),
GridDistortion(p=1),
RandomGridShuffle(),
Flip()


106 soy images were randomly chosen with 17 random augmentations applied to each

250 sunflower images were randomly chosen with 7 random augmentations applied to each

500 wheat images were randomly chosen with 2 random augmentations applied to each

Total number of augmented images generated - 4552
Total number of original images collected - 1421
Total number of images to be used for training - 5973

Visualization of augmentations and code for this process can be found in "data_preprocessing.ipynb" notebook.

Since there are no barley images the class indexes have been renamed by subtracting 1.
classes = {
    "soy": 0,
    "sunfolwer": 1,
    "wheat": 2
}

Help and guides were taken from:
https://www.kaggle.com/code/ankursingh12/data-augmentation-for-object-detection
https://huggingface.co/spaces/IliaLarchenko/albumentations-demo
