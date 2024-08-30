# Towel Multiple Instances 🚀

## Overview

**Towel Multiple Instances** is a Python-based GUI application that allows you to open multiple instances of any application on both macOS and Windows. It uses the Tkinter library to provide an easy-to-use graphical interface and automates the process of opening the desired number of instances.

## Features

- 🖥️ **User-Friendly GUI**: Built with Tkinter for ease of use.
- 🗂️ **Application Selection**: Browse and select the application you want to run.
- 🔄 **Instance Management**: Specify the number of instances to open.
- 🤖 **Automated Execution**: Automatically handles the execution for both macOS and Windows.

Either download from 'Releases' or:

## Installation and Usage

### macOS

#### 1. Clone the Repository 🔗

Start by cloning the repository from GitHub:

```bash
git clone https://github.com/towelWet/Multiple-Instances.git
cd Multiple-Instances
```

#### 2. Run the Application ▶️

Ensure you have Python installed on your macOS system. You can then run the application with:

```bash
python multipleinstances-mac.py
```

#### 3. Using the Application 💻

- **Select Application**: Click "Browse" to navigate and select the `.app` file of the application you want to open.
- **Specify Instances**: Enter the number of instances you wish to open in the "Number of Instances" field.
- **Open Instances**: Click "Open Instances" to execute the action.

### Windows

#### 1. Clone the Repository 🔗

Start by cloning the repository from GitHub:

```bash
git clone https://github.com/towelWet/Multiple-Instances.git
cd Multiple-Instances
```

#### 2. Run the Application ▶️

Ensure you have Python installed on your Windows system. You can then run the application with:

```bash
python multipleinstances-win.py
```

#### 3. Using the Application 💻

- **Select Application**: Click "Browse" to navigate and select the `.exe` file of the application you want to open.
- **Specify Instances**: Enter the number of instances you wish to open in the "Number of Instances" field.
- **Open Instances**: Click "Open Instances" to execute the action.

## Building a Standalone Application with PyInstaller 📦

### macOS

#### 1. Install PyInstaller 🛠️

If you haven't already, install PyInstaller:

```bash
pip install pyinstaller
```

#### 2. Create the Standalone Application 🏗️

Navigate to the directory where the Python script is located, then run:

```bash
pyinstaller --onefile --windowed --name "Towel Multiple Instances" --icon "/path/to/your/icon/AppIcon.icns" multipleinstances-mac.py
```

#### 3. Locate the Output 📁

PyInstaller will create a `dist` directory containing the `Towel Multiple Instances.app`. This is the standalone macOS application.

#### 4. Move the Application 🚚

Move the newly created `Towel Multiple Instances.app` to your desired location, such as the `Applications` folder.

#### 5. Launch the Application 🚀

Double-click the `Towel Multiple Instances.app` to launch it, and use the GUI to open multiple instances of your selected application.

### Windows

#### 1. Install PyInstaller 🛠️

If you haven't already, install PyInstaller:

```bash
pip install pyinstaller
```

#### 2. Create the Standalone Application 🏗️

Navigate to the directory where the Python script is located, then run:

```bash
pyinstaller --onefile --icon="C:\path\to\your\icon\towelmultipleinstances.jpg" C:\path\to\your\script\multipleinstances-win.py
```

#### 3. Locate the Output 📁

PyInstaller will create a `dist` directory containing the `multipleinstances-win.exe` file. This is the standalone Windows executable.

#### 4. Move the Application 🚚

Move the newly created executable to your desired location.

#### 5. Launch the Application 🚀

Double-click the `multipleinstances-win.exe` to launch it, and use the GUI to open multiple instances of your selected application.

## Creating an Installer with Inno Setup for Windows 🛠️

### 1. Install Inno Setup

Download and install Inno Setup from the [official website](https://jrsoftware.org/isinfo.php).

### 2. Prepare the Inno Setup Script

Create an Inno Setup script using the following template:

```iss
[Setup]
AppName=Towel Multiple Instances
AppVersion=1.0
DefaultDirName={pf}\Towel Multiple Instances
DefaultGroupName=Towel Multiple Instances
OutputBaseFilename=TowelMultipleInstancesInstaller
SetupIconFile=C:\path\to\your\icon\towelmultipleinstances.jpg
Compression=lzma
SolidCompression=yes

[Files]
Source: "C:\path\to\your\dist\multipleinstances-win.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Towel Multiple Instances"; Filename: "{app}\multipleinstances-win.exe"; IconFilename: "{app}\towelmultipleinstances.jpg"
Name: "{group}\{cm:UninstallProgram,Towel Multiple Instances}"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\multipleinstances-win.exe"; Description: "{cm:LaunchProgram,Towel Multiple Instances}"; Flags: nowait postinstall skipifsilent
```

### 3. Compile the Script

Open the script in Inno Setup and click "Compile" to generate the installer.

### 4. Test the Installer

Run the installer to ensure everything works as expected.

## License ⚖️

This project is licensed under the MIT License. For more details, see the `LICENSE` file in the repository.

## Contribution 🤝

Contributions are welcome! Please fork this repository and submit a pull request with your improvements.
