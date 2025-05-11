# Smart Security Motion Detection System 🎥🔐

A real-time motion detection and recording system using Python, OpenCV, and Tkinter. This smart surveillance tool can detect motion from a **webcam or a video file**, automatically records 10-second clips when motion is detected, and saves them with timestamps.

---

## ✨ Features

- 🟢 Live webcam motion detection
- 📂 Detect motion from pre-recorded video files
- 🔳 Bounding boxes highlight motion zones
- 🕒 Timestamps and motion area displayed on screen
- 🎞️ Automatically records 10-second video clips when motion is detected
- 💾 Saves recordings in `smart-security/` folder with timestamps
- 🖥️ Simple GUI with buttons for live or file-based detection

---

## 🛠️ Tech Stack

- **Python 3**
- **OpenCV** for computer vision and motion detection
- **Tkinter** for GUI
- **NumPy** for image processing

---

## 📂 Folder Structure

motion-detector/
├── motion_detector.py
├── smart-security/
│ └── intrusion_YYYYMMDD_HHMMSS.mp4


---

## ⚙️ How to Run

1. Install dependencies:

```bash
pip install opencv-python numpy

python motion_detector.py
Use the GUI:


Click "Live Motion Detection" to use webcam

Click "Recorded File Motion" to select a saved video

