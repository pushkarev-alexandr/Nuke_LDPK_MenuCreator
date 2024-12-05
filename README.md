### 📘 Nuke_LDPK_MenuCreator - Installation Guide

This repository helps you integrate Lens Distortion Plugin Kit (LDPK) plugins from 3DEqualizer4 (3DE4) into Nuke. Follow the steps below for a smooth setup.

---

## 🚀 Manual Installation

1. **Copy the 3DE4 folder**  
   Move the `3DE4` folder into your `.nuke` directory.

2. **Copy the `init.py` file**  
   Place the `init.py` file in your `.nuke` directory.

3. **If an `init.py` file already exists:**  
   Add the following line to the end of your existing `init.py` file:
   ```python
   nuke.pluginAddPath('./3DE4')
   ```

---

## 🖥️ Command-Line Installation (Windows)

Run the provided `windows_install.cmd` script to automate the manual installation steps.

---

## 📥 Adding Distortion Plugins

1. **Download the latest plugin version:**  
   Visit [3DEqualizer Tech Docs](https://www.3dequalizer.com/?site=tech_docs) and download the most recent LDPK plugin version.

2. **Copy the plugin folder:**
   - From the downloaded files, navigate to:
     ```
     \compiled\nuke\windows
     ```
   - Locate the folder corresponding to your Nuke version (e.g., for Nuke 15.1v4):
     ```
     \compiled\nuke\windows\Nuke15.1
     ```
   - Copy this folder into your `3DE4` directory at:
     ```
     C:\Users\%USERNAME%\.nuke\3DE4
     ```
   - After copying, the structure should look like:
     ```
     C:\Users\%USERNAME%\.nuke\3DE4\Nuke15.1
     ```

3. **Launch Nuke:**  
   Start Nuke, and the LDPK plugin should appear in the sidebar menu.

---

You're all set! Enjoy enhanced functionality with your distortion plugins in Nuke! 🎥✨