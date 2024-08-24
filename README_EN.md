# Run App

[![Русский](https://img.shields.io/badge/language-Русский-blue.svg)](README.md)
[![English](https://img.shields.io/badge/language-English-red.svg)](README_EN.md)

Русская версия этого README доступна [здесь](README.md).

**Run App** is a versatile utility designed to make running Python scripts as straightforward as launching any other application on your computer. With this program, you can turn your Python scripts into standalone applications that can be executed with a single click, without needing to manually activate a virtual environment or ensure that Python is installed on the system.

The utility does NOT require converting Python scripts into executable files.

No modifications to the Python application's code are needed. You can simply copy the necessary application's code into a separate folder and run it as a full-fledged Windows or MacOS application.

## Application Scope

**Run App** is a utility designed for use on personal computers, enabling users to create and run Python applications without needing to understand the intricacies of Python execution or configure virtual environments on each device. It is not intended for server use or remote deployment, but is ideal for a wide range of tasks performed on local machines.

The utility does NOT require converting Python scripts into executable files.

**Run App** significantly simplifies working with Python applications on personal computers, making them accessible to a broader range of users, regardless of their technical background. The utility allows Python scripts to be quickly and conveniently launched as full-fledged applications, ensuring their stable operation without the need to delve into the complexities of Python or environment setup.

### Use Cases

1. **Workplace Task Automation**:
    - Create scripts for automated management of documents and spreadsheets hosted on cloud services like Google Drive or OneDrive. These scripts can automatically download, modify, or update files, performing tasks on a schedule or as needed.

2. **Web Scraping**:
    - Develop a scraper that collects data from various websites, such as monitoring prices, gathering news, or analyzing competitors. This scraper can be run from any computer or even from a USB drive, providing mobility and independence from a specific workstation.

3. **Local Data Management**:
    - Use the utility to automate backups of important data, manage files and folders on a local disk or cloud, synchronize data between devices, and more.

4. **Specialized Tasks for Professionals**:
    - Develop utilities for engineers, analysts, designers, and other professionals who need to perform specific tasks with certain data or applications, such as automating data processing, generating reports, converting files into various formats, and more.

5. **Database Management**:
    - The utility can be used to create local applications that connect to remote databases, perform data analysis, generate reports, or import/export data.

6. **Educational Projects**:
    - Ideally suited for students and educators who need to demonstrate or test Python code without the need to install Python on every computer. This simplifies the process of distributing and using educational materials.

7. **Portable Applications**:
    - Create applications that can be run from external media, such as a USB drive. This allows the application to be easily moved between different computers without leaving traces on the systems or requiring Python installation.


## Why is it Useful?

Many developers face the challenge of deploying their Python applications on machines where Python might not be installed, or where the installed version does not match the required one. **Run App** solves this problem by offering a tool that not only creates an executable file for your script but also automatically sets up a virtual environment, installs the necessary dependencies, and ensures that your application runs smoothly without any issues.

This utility is useful for:
- **Developers** who need to deliver their scripts to clients or colleagues who may not be familiar with Python setup and installation.
- **System administrators** who require applications to run reliably on any machine without additional configuration.
- **Education and testing**, where it's important to quickly run scripts on different systems with minimal setup.

## Features

- **Execute Python scripts as applications**: Convert your Python scripts into executable files that can be launched directly from the desktop.
- **Automatic virtual environment setup**: The program automatically creates a virtual environment in the `app` directory if one is not already present.
- **Dependency management**: The program installs all necessary dependencies specified in the `requirements.txt` file into the virtual environment.
- **Cross-platform compatibility**: Works on both Windows and macOS, providing consistent script execution across different operating systems.

## How It Works

The program is designed to execute a Python script named `main.py`, which must be located in the `app` subdirectory. A `requirements.txt` file is also required in the same directory to install all necessary dependencies.

### Project Structure Example:

your_project/ 

├── app/ │ 

├── main.py 

│ └── requirements.txt 

└── run_app.exe


In this structure:

- **`app/`**: The directory containing your main application.
  - **`main.py`**: The primary Python script to be executed.
  - **`requirements.txt`**: The file containing dependencies required for the script to run.
- **`run_app.exe`**: The executable file that launches the application.

### Additional Recommendations

For convenience, you can rename `run_app.exe` to the name of your application. For example, if your application is called "Video Converter," you can rename the file to `VideoConverter.exe`. You can then create a shortcut on the desktop or in the Start menu and run the application like any other standard application. This makes it easier for end users to use your Python script without dealing with the underlying technical details.

### Usage Instructions

1. **Preparation**:
   - Place your entire project in the `app` directory. It is essential that the entry point of your project, which should be the first file executed, is named `main.py`. This requirement is necessary for the program to work correctly. All other files and directories of your project should also be inside the `app` folder.

   - Before placing the project in the `app` directory, you need to create a `requirements.txt` file that lists all the libraries and their versions used in your project. To do this, run the following command in your development environment or command line:

   - pip freeze > requirements.txt

   - This command will generate a `requirements.txt` file with an up-to-date list of dependencies, allowing the program to automatically install all the necessary libraries into the virtual environment when it is launched.

2. **Execution**:
- Rename `run_app.exe` to any name you prefer, such as the name of your application. This will help you and other users easily identify the application.

3. **Running**:
- Run the newly named executable file. The program will automatically check if Python is installed on your computer, create a virtual environment, install all necessary dependencies from `requirements.txt`, and then launch your `main.py` script.

### Important

The program supports running any project that can work within a virtual environment. However, the ability to launch frameworks like Django, Flask, FastAPI, and others that require additional configurations and are not typically run using a `main.py` script will be implemented in future versions of this utility.

## Utility Setup

This section describes how to set up the **Run App** utility and create an executable file (`.exe`) using `PyInstaller`. Follow these steps to prepare and launch your Python project as a standalone application.

### Step 1: Install PyInstaller

First, you need to install `PyInstaller` if it is not already installed. You can do this with the following command:

pip install pyinstaller


### Step 2: Create the Executable File (exe)

Use `PyInstaller` to create an executable file for your application. In the command line, navigate to the directory where your `run_app.py` file is located and run the following command:

pyinstaller --onefile run_app.py


This command will create an executable file in the `dist` folder, which you can rename and use to run your application.

### Step 3: Configure the Executable File

After creating the executable file, move it to the root folder of your future standalone application. You can rename the file to any name you prefer, such as the name of your application. Create a folder named `app` and copy your Python project into it. The main entry point of your project must be named `main.py`.

Don’t forget to create and copy the `requirements.txt` file into the `app` folder.

Now you can run your project using the `run_app` utility.

### Step 4: Testing

Run the newly created executable file and ensure that the application works correctly. The program will automatically create a virtual environment, install all dependencies, and launch the `main.py` script.

Your Python application is now ready to be used as a standalone application that can be run on any machine without additional configuration.

### What to Do If Python Is Not Installed

If Python is not installed on your system, the program will provide instructions on how to install it and will also provide links to download suitable versions for Windows and macOS.

**Recommendations for Choosing a Python Version**:
- It is recommended to install Python version 3.10.11 or later for stable performance.
- Avoid installing the latest Python versions, as they may contain bugs. It is better to choose the latest stable version from the previous series (e.g., 3.11 instead of 3.12).

## Python Download Links

### Python for Windows:
- **Download Page**: [Python Releases for Windows](https://www.python.org/downloads/windows/)
- **Python 3.12.5**: [Download](https://www.python.org/ftp/python/3.12.5/python-3.12.5-amd64.exe)
- **Python 3.11.8**: [Download](https://www.python.org/ftp/python/3.11.8/python-3.11.8-amd64.exe)
- **Python 3.10.11**: [Download](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe)

### Python for macOS:
- **Download Page**: [Python Releases for macOS](https://www.python.org/downloads/macos/)
- **Python 3.12.5**: [Download](https://www.python.org/ftp/python/3.12.5/python-3.12.5-macos11.pkg)
- **Python 3.11.9**: [Download](https://www.python.org/ftp/python/3.11.9/python-3.11.9-macos11.pkg)
- **Python 3.10.11**: [Download](https://www.python.org/ftp/python/3.10.11/python-3.10.11-macos11.pkg)

## License

This project is licensed under the [MIT License](LICENSE).
 



