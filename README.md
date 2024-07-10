# AgroSkyAI Project

## Overview
This project aims to develop and deploy crop recognition algorithms using machine learning and computer vision techniques on the NVIDIA Jetson AGX platform.

## Installation

### System Dependencies
Before setting up the Python environment, ensure you have the following system dependencies installed:

- Python 3.x: The programming language used for the project.
- TensorFlow or PyTorch: Deep learning frameworks. You can choose either depending on your preference or project requirements.
- OpenCV: An open-source computer vision and machine learning software library.
- NumPy: A fundamental package for scientific computing with Python.
- NVIDIA JetPack SDK: The software development kit for the NVIDIA Jetson platform.
- TensorRT: A high-performance deep learning inference library from NVIDIA.

On a Linux system, you may need to install the following dependencies before proceeding:

```bash
sudo apt-get update
sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
pip3 install -U pip setuptools wheel


