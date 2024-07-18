#!/bin/bash

# Uninstall conflicting packages
pip uninstall -y numpy typing-extensions

# Install specific versions of the required packages
pip install numpy==1.24.3 typing-extensions==4.5.0 tensorflow-cpu-aws==2.13.1 albumentations==1.4.0 pydantic==1.10.5

# Verify the installations
pip list

# Test if imports work without errors
python - <<END
import albumentations as A
import tensorflow as tf

print("albumentations version:", A.version)
print("tensorflow version:", tf.version)
END
