
## Overview

Real-Time Hand Gesture Controlled Rectangles: A project that uses OpenCV to detect hand gestures and allows users to drag rectangles on the screen by moving their fingers.

## Features

- **Real-Time Hand Gesture Recognition**: Uses OpenCV for detecting hand gestures and moving rectangles on the screen.
- **Video Capture**: Accesses the default camera using `cv2.VideoCapture(0)`.
- **Hand Contour Detection**: Detects the largest hand contour in the frame.
- **Draggable Rectangles**: Allows dragging rectangles based on fingertip positions.
- **Drawing and Bounding Box**: Draws rectangles and a transparent overlay.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/Hand-Gesture-Controlled-Rectangles.git
    cd Hand-Gesture-Controlled-Rectangles
    ```

2. **Install the required dependencies**:
    ```bash
    pip install opencv-python numpy
    ```

## Usage

1. **Run the script**:
    ```bash
    python hand_gesture_controlled_rectangles.py
    ```

2. **Interact with the application**:
    - Move your hand in front of the camera.
    - Drag rectangles by moving your finger inside them.

3. **Exit**: Press the 'ESC' key to quit the application.

## Code Explanation

- **Video Capture**: Initializes the video capture with specified width and height.
- **Contour Detection**: Converts the frame to grayscale, applies Gaussian blur, and thresholds the image to find contours.
- **Defect Detection**: Identifies the convexity defects to find the fingertip position.
- **Rectangle Class**: `DragRect` class defines a rectangle that can be dragged based on the cursor position.
- **Transparent Drawing**: Creates a transparent overlay for drawing the rectangles.

## Important Notes

- **Dependencies**: The project requires `opencv-python` and `numpy` packages.
- **Camera Access**: Ensure your default camera is accessible. If you have multiple cameras, you may need to adjust the `cv2.VideoCapture()` index.
- **Performance**: The code processes frames in real-time; ensure your system has enough resources to handle video processing.
- **Fingertip Detection Accuracy**: The accuracy of fingertip detection can vary based on lighting conditions and background. For best results, use the application in a well-lit environment with a clear background.

## Cautions

- **Resource Usage**: The application can be resource-intensive. Close other applications if you experience performance issues.
- **Accuracy**: The hand detection might not be accurate in poor lighting conditions or if the hand is too close to the camera.
- **Safety**: Ensure the surroundings are safe and clear of obstacles when using the application to avoid any physical accidents while interacting with the screen.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any improvements or bug fixes.
