## NetBinder

**NetBinder** is a simple Python-based application with a graphical interface that allows users to bind an application to a specific network connection using `ForceBindIP`. The tool enables you to easily select an application and a network connection, bind them together, and launch the app with the specified network connection (e.g. Ethernet or Wi-Fi).

## Features

- Select any application to bind it to a specific network connection.
- Automatically detects available network connections and their IP addresses.
- Binds the selected application to the chosen network connection using `ForceBindIP`.
- Option to browse and select the `ForceBindIP` executable manually.
- Installs `ForceBindIP` if not already installed.

## Prerequisites

- Python 3.x
- Git
- `ForceBindIP` (download from [here](https://r1ch.net/projects/forcebindip))

## Installing Python

To run this application, you need to have Python installed on your system. Follow these steps to install Python:

1. **Download Python**:
   - Visit the official Python website: [python.org](https://python.org).
   - Download the latest version of Python for your operating system.

2. **Run the Installer**:
   - Launch the installer you downloaded.
   - Make sure to check the box that says "Add Python to PATH" before clicking **Install Now**.

3. **Verify Installation**:
   - Open a command prompt (Windows) or terminal (macOS/Linux).
   - Type the following command and press Enter:
     ```bash
     python --version
     ```
   - If Python is installed correctly, you will see the version number.


To install Git on your system, follow the steps for your operating system:

# Installing Git

To install Git on your system, follow the steps for your operating system:

### Download Git:
- Visit the official Git website: [git-scm.com](https://git-scm.com).
- Click on "Download" for Windows.

### Run the Installer:
- Open the downloaded `.exe` file.
- Follow the installation prompts. You can use the default settings for most options.

### Verify Installation:
- Open the Command Prompt (search for "cmd" in the Start menu).
- Type the following command and press Enter:
  ```bash
  git --version

## How to Use

### 1. Running the Application

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MobinKhaledi/NetBinder.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd NetBinder
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python NetBinder.py
   ```

### 2. Selecting an Application and Network

- Launch the app and select an application to bind to a network.
- Choose a network connection from the dropdown list.
- Press the **NetBind App** button to bind the app to the selected network.

### 3. ForceBindIP Installation

If `ForceBindIP` is not installed, you have two options:

- **Manual Installation**: Download `ForceBindIP` from the official website [here](https://r1ch.net/projects/forcebindip) and install it manually.
  
- **Automatic Installation**: Use the **Install ForceBindIP** button within the app. This option will download and install `ForceBindIP` to the appropriate location (`C:\Program Files\ForceBindIP` or `C:\Program Files (x86)\ForceBindIP`) automatically. Note: Administrator permission is required.

### 4. ForceBindIP Path Selection

If the app cannot find `ForceBindIP`, you can manually select the executable using the **Select ForceBindIP Path** button.
