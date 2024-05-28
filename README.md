# Screen Mirroring Application

This repository contains a Python application for mirroring the screen of one PC (PC01) and streaming it live to another PC (laptop) over a network. The implementation uses `pyautogui` for capturing screenshots and `OpenCV` for streaming these frames as a video.

## Features

- Live screen mirroring from PC01 to a laptop
- Adjustable frame rate for optimized performance
- Resizing of frames to reduce data size and improve transmission speed
- Error handling and connection management

## Requirements

- Python 3.6+
- Libraries:
  - `pyautogui`
  - `opencv-python`
  - `numpy`

You can install the required libraries using pip:
```bash
pip install pyautogui opencv-python numpy
