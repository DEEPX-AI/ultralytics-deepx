#!/usr/bin/env python3
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

"""
Ultralytics package command-line interface (CLI) entry point.

This module provides the CLI entry point for the Ultralytics package when run as a module.

Usage:
    python -m ultralytics predict model=yolo11n.pt source='https://youtu.be/LNwODJXcvt4'
    python -m ultralytics train data=coco8.yaml model=yolo11n.pt epochs=10 lr0=0.01
    python -m ultralytics val model=yolo11n.pt data=coco8.yaml batch=1 imgsz=640
    python -m ultralytics export model=yolo11n.pt format=onnx imgsz=640
"""

import sys
from ultralytics.cfg import entrypoint


if __name__ == "__main__":
    # Convert command line arguments to a single string for entrypoint function
    # Skip the first argument (script name) and join the rest
    debug_args = " ".join(sys.argv[1:])
    entrypoint(debug=debug_args)