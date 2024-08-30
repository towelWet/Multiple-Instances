# Towel Multiple Instances 🚀

## Overview

**Towel Multiple Instances** is a Python-based GUI application that allows you to open multiple instances of any macOS application. It uses the Tkinter library to provide an easy-to-use graphical interface and generates a temporary bash script to automate the process of opening the desired number of instances.

## Features

- 🖥️ **User-Friendly GUI**: Built with Tkinter for ease of use.
- 🗂️ **Application Selection**: Browse and select the `.app` file you want to run.
- 🔄 **Instance Management**: Specify the number of instances to open.
- 🤖 **Automated Execution**: Automatically generates and executes a bash script.

Either download from 'Releases' or:


## Installation and Usage

### 1. Clone the Repository 🔗

Start by cloning the repository from GitHub:

```bash
git clone https://github.com/towelWet/Multiple-Instances.git
cd Multiple-Instances
```

### 2. Run the Application ▶️

Ensure you have Python installed on your macOS system. You can then run the application with:

```bash
python multipleinstances.py
```

### 3. Using the Application 💻

- **Select Application**: Click "Browse" to navigate and select the `.app` file of the application you want to open.
- **Specify Instances**: Enter the number of instances you wish to open in the "Number of Instances" field.
- **Open Instances**: Click "Open Instances" to execute the action.

## Building a Standalone macOS Application with PyInstaller 📦

To distribute the application as a standalone macOS app, you can bundle it using PyInstaller.

### 1. Install PyInstaller 🛠️

If you haven't already, install PyInstaller:

```bash
pip install pyinstaller
```

### 2. Create the Standalone Application 🏗️

Navigate to the directory where the Python script is located, then run:

```bash
pyinstaller --onefile --windowed --name "Towel Multiple Instances" --icon "/Users/towelwet/Pictures/(Towel Apps)/Towel Multiple Instances/AppIcon.icns" multipleinstances.py
```

### 3. Locate the Output 📁

PyInstaller will create a `dist` directory containing the `Towel Multiple Instances.app`. This is the standalone macOS application.

### 4. Move the Application 🚚

Move the newly created `Towel Multiple Instances.app` to your desired location, such as the `Applications` folder.

### 5. Launch the Application 🚀

Double-click the `Towel Multiple Instances.app` to launch it, and use the GUI to open multiple instances of your selected application.

## License ⚖️

This project is licensed under the MIT License. For more details, see the `LICENSE` file in the repository.

## Contribution 🤝

Contributions are welcome! Please fork this repository and submit a pull request with your improvements.

---
