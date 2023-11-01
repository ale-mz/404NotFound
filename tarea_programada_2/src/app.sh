#!/bin/bash

# Check if Python is installed
python3 --version > /dev/null 2>&1

# If Python is not installed, install it
if [ $? -ne 0 ]; then
    echo "Python is not installed. Installing..."
    
    # Install Python using package manager (apt)
    sudo apt update
    sudo apt install python3 -y
fi

# Check if customtkinter is installed
pip3 show customtkinter > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "customtkinter is not installed. Installing..."
    pip3 install customtkinter
fi

# Run your Python app
python3 main.py
