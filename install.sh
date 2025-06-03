#!/bin/bash

python -m venv venv 
source venv/bin/activate
pip install -r requirements.txt || exit 1
echo ""
echo "venv created"

echo "In your waybar config:"
echo "\"exec\": \"$(pwd)/venv/bin/python $(pwd)/piss_monitor.py\","