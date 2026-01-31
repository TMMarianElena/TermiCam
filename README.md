# TermiCam: Professional Real-Time Terminal Video Engine 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Terminal](https://img.shields.io/badge/interface-ANSI%20Terminal-lightgrey?style=for-the-badge)
![Matrix](https://img.shields.io/badge/vibe-Cyberpunk-green?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)

**TermiCam** is a high-performance computer vision utility that transforms live webcam streams into high-fidelity ASCII art. Utilizing **OpenCV** for frame processing and **ANSI escape sequences** for color rendering, it features a custom **Matrix Shader**, **Motion Blur Accumulation**, and **Audio-Reactive** pulse logic—all running natively in your command line.

## ✨ Features

* **Real-Time ASCII Rendering**: Converts pixel luminance into optimized character glyphs with low latency.
* **TrueColor ANSI Support**: Renders full 24-bit color directly in supported terminal emulators.
* **Digital Rain (Matrix Mode)**: A specialized shader that maps brightness to neon-green gradients for a retro-hacker aesthetic.
* **Motion Blur Accumulation**: Uses weighted frame averaging to create ghostly digital trails during movement.
* **Audio-Reactive Pulse**: (Optional) Integrates with system audio to scale visual brightness based on sound intensity.
* **Snapshot Utility**: Capture and save your terminal's current frame as a `.txt` file with a single keystroke.
* **Global CLI Deployment**: Includes a `termicam.bat` wrapper for instant access from any directory.

---

## 🛠️ Tech Stack

| Layer          | Technology                               |
|:---------------|:-----------------------------------------|
| Core Language  | Python 3.10+                             |
| Vision Engine  | OpenCV (cv2)                             |
| Math & Logic   | NumPy (Matrix Transformations)           |
| Audio Analysis | SoundDevice (Real-time Stream)           |
| UI Rendering   | ANSI Escape Codes & UTF-8 Encoding       |

---

## 📁 Project Structure

```bash
TermiCam/
├── cam.py                # Main Application Logic
├── termicam.bat          # Windows Global CLI Wrapper
├── requirements.txt      # Dependency Manifest
├── snapshot.txt          # Exported ASCII Captures
└── dist/                 # Standalone Executables (.exe)

```
---

## 🎨 Command Reference
### Control your view in real-time:

🟢 [S] - Save a high-resolution text snapshot to snapshot.txt.

🔴 [Q] - Safely terminate the video stream and reset terminal colors.

---

## 🚀 How to Run
Quick Start
**Install Dependencies**:
'pip install -r requirements.txt'

**Launch Application**:
'python cam.py'

Production Build (Standalone EXE)
To create a portable version for Windows: pyinstaller --onefile --name TermiCam cam.py

**Developer Note**: This project demonstrates the intersection of Computer Vision (CV) and Terminal User Interfaces (TUI), specifically focusing on real-time signal processing and buffer management.

---

## 👨‍💻 Author

**Meet Potdar**
*Backend & Creative Technologist*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/meet-potdar-04b12b290?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
[![Portfolio](https://img.shields.io/badge/Portfolio-%23000000.svg?style=flat&logo=firefox&logoColor=white)](https://meet3333333333.wixstudio.com/my-site)

<p align="center"> <img src="snapshot.png" width="600" title="TermiCam Matrix Interface"> </p>

---
*Built with ❤️ using Python & OpenCV*
