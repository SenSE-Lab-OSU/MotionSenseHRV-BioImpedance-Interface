#!/bin/bash

# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
source ./env/bin/activate

# Print setup message
echo "Setup Complete"

# Install dependencies
python3 -m pip install -r requirements.txt

# Run the Python script
python3 MotionSenseCollection.py