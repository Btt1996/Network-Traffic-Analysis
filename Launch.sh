#!/bin/bash

# run main script in background
nohup python3 main.py &

# give execute permissions to the script
chmod +x launch.sh

# add execute permissions to the main script
chmod +x main.py
