23-07-2024

- Objective:
  Integrate model with Jetson Xavier device to perform real time object detection

- Configuration:
  - Model: yolov7
  - Weights: fold1 weights

- Camera Used:
  - Logitech c270 webcam

- Results:
  - the live detection was successfully launched using command $ python detect.py --weights runs/train/fold1/weights/best.pt --source 0 --conf 0.5 --img-size 512 --save-txt --save-conf --name fold1_camera_trial*
  - there were no physical representations of the dataset available, therefore there is no way to evaluate the live detection.
  - model successfully exported to onnx format
 
- Observations:
  - The live detection was launched directly with the yolov7 which resulted in slow functioning and lagging of videos from the camera. The step to try to resolve this was to convert the model to onnx format.
  - All necessary libraries for detection can be found in 'export_requirements.txt' file, with unsuccessful attempt of installing onnxsim on the jetson xavier device.
  - specific opencv library needs to be downloaded to run real time detection on the jetson xavier device. commands to do this are as following:
$sudo apt-get update
$sudo apt-get install -y build-essential cmake git
$sudo apt-get install -y libjpeg-dev libtiff-dev libpng-dev
$sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev
$sudo apt-get install -y libv4l-dev v4l-utils
$sudo apt-get install -y libxvidcore-dev libx264-dev
$sudo apt-get install -y libgtk-3-dev libcanberra-gtk-module libcanberra-gtk3-module
$sudo apt-get install -y libatlas-base-dev gfortran
$cd ~
$git clone https://github.com/opencv/opencv.git
$git clone https://github.com/opencv/opencv_contrib.git
$cd opencv
$mkdir build
$cd build
$cmake -D CMAKE_BUILD_TYPE=Release \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
      -D BUILD_EXAMPLES=ON ..
$make -j$(nproc)
$sudo make install
$sudo ldconfig
$cp -r /usr/lib/python3.8/dist-packages/cv2 /home/agx/agro_sky_ai/AgroSkyAI/agro_venv/lib/python3.8/site-packages/

- Conclusions:
  - The model was successfully launched to perform real time detection. The model was converted to onnx format but is yet to be tested. More efforts will be performed to speedup real time detection. Evaluation of real time detection will be performed once physical data is provided.
 
