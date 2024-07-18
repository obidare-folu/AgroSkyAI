import random
import numpy as np
import torch
# import tensorflow as tf

def set_seed(seed=2402):
    # Python's built-in random module
    random.seed(seed)
    
    # NumPy
    np.random.seed(seed)
    
    # PyTorch
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)  # if you are using multi-GPU.
    
    # TensorFlow
    # tf.random.set_seed(seed)


def convert_bbox(bboxes, input_format, output_format, image_size):
    """
    Convert bounding boxes from one format to another.

    Parameters:
    - bboxes: List of bounding boxes.
    - input_format: Format of the input bounding boxes (pascal_voc, albumentations, coco, yolo).
    - output_format: Format of the output bounding boxes (pascal_voc, albumentations, coco, yolo).
    - image_size: Tuple of (width, height) of the image.

    Returns:
    - Converted bounding boxes in the desired format.
    """
    def to_pascal_voc(bbox, img_w, img_h, fmt):
        if fmt == 'pascal_voc':
            return bbox
        elif fmt == 'albumentations':
            x_min, y_min, x_max, y_max = bbox
            return [x_min * img_w, y_min * img_h, x_max * img_w, y_max * img_h]
        elif fmt == 'coco':
            x_min, y_min, width, height = bbox
            return [x_min, y_min, x_min + width, y_min + height]
        elif fmt == 'yolo':
            x_center, y_center, width, height = bbox
            x_min = (x_center - width / 2) * img_w
            y_min = (y_center - height / 2) * img_h
            x_max = (x_center + width / 2) * img_w
            y_max = (y_center + height / 2) * img_h
            return [x_min, y_min, x_max, y_max]

    def from_pascal_voc(bbox, img_w, img_h, fmt):
        if fmt == 'pascal_voc':
            return bbox
        elif fmt == 'albumentations':
            x_min, y_min, x_max, y_max = bbox
            return [x_min / img_w, y_min / img_h, x_max / img_w, y_max / img_h]
        elif fmt == 'coco':
            x_min, y_min, x_max, y_max = bbox
            return [x_min, y_min, x_max - x_min, y_max - y_min]
        elif fmt == 'yolo':
            x_min, y_min, x_max, y_max = bbox
            x_center = (x_min + x_max) / 2 / img_w
            y_center = (y_min + y_max) / 2 / img_h
            width = (x_max - x_min) / img_w
            height = (y_max - y_min) / img_h
            return [x_center, y_center, width, height]

    img_w, img_h = image_size
    pascal_voc_bboxes = [to_pascal_voc(bbox, img_w, img_h, input_format) for bbox in bboxes]
    output_bboxes = [from_pascal_voc(bbox, img_w, img_h, output_format) for bbox in pascal_voc_bboxes]
    return output_bboxes
