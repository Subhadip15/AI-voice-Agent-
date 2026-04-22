# 🎤 Subha Voice AI Agent

A robust Python-based voice assistant designed to automate system power management using natural language processing.

---

## # Project Overview
This AI agent listens to user voice commands and executes system-level operations like shutting down, restarting, or putting the computer to sleep. It features a built-in text-to-speech engine to provide real-time status updates.

---

## # Core Features
* **Voice-Activated Commands:** Control your hardware without touching the keyboard.
* **Smart Feedback:** Verbal confirmation for every action taken.
* **Noise Calibration:** Automatically adjusts for background noise to improve accuracy.
* **System Integration:** Directly interacts with Windows OS power functions.

---

## # Voice Command List
| Action | Phrase to Speak |
| :--- | :--- |
| **Power Off** | "Shut down" or "Shutdown" |
| **Reboot** | "Restart" |
| **Standby** | "Sleep" |
| **Quit App** | "Exit" or "Stop" |

---

## # Installation & Setup

### 1. Install Required Dependencies
Open your terminal and run the following commands to install the necessary Python libraries:
```bash
pip install SpeechRecognition pyttsx3 pyaudio
2. Run the Application
Navigate to your project folder and execute the script:

Bash
python main.py
# Technical Configuration
Language: Python 3.x

Speech Engine: Google Speech Recognition API

TTS Engine: pyttsx3 (SAPI5 for Windows)

Execution Rate: 170 words per minute

# Troubleshooting
Single Line Formatting: Always ensure this file is saved with the .md extension.

Microphone Issues: Check if your default microphone is active in Windows Privacy Settings.

API Errors: If you hear "Internet Issue," verify your Wi-Fi connection as the voice-to-text conversion requires the cloud.

# Credits
Developed by Subha Built for automation and hands-free system control.
