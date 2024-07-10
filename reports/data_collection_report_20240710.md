10-07-2024

Data collection for first round of training complete

500 images were randomly selected frow the gwhd_2021 dataset.

Manually selected 106 healthy soybean images from both the bycbh73438 and soynet dataset. Manually drew the bounding boxes for these images using
LabelImg application (https://github.com/HumanSignal/labelImg/tree/master).

Selected 315 images from the sunflower dataset, transformed masks to bounding boxes were needed. A total of 641 sunflower images which the masks or bounding boxes were
missing were saved to use for prediction.

No barley dataset found, awaiting prepared dataset.

As a result a total of 921 images with bounding boxes have been gathered and prepared for training.
The labels are stored in csv format in the form image_name,class,bboxes_string.
The classes are as follows:
classes = {
    "barley": 0,
    "soy": 1,
    "sunfolwer": 2,
    "wheat": 3
}
1 bounding box is stored in the coco format (xmin, ymin, width, heigth) and all boxes are combined into a string seperated by ";"
The code for collecting the data from the images can be found in the data_collection.ipynb and the code for drawing the bounding boxes can be found in draw_bboxes.ipynb

Challenges faced:
Wne drawing the bboxes, some of them were incorrect or distorted. After a long time of thorough debugging and going through images, it was discovered that the PIL.Image module sometimes orientates images.
This issue was resolved by adding the line of code $fixed_image = ImageOps.exif_transpose(img)
