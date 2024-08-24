# Run App

[![Русский](https://img.shields.io/badge/language-Русский-blue.svg)](README.md)
[![English](https://img.shields.io/badge/language-English-red.svg)](README_EN.md)

Русская версия этого README доступна [здесь](README.md).

**Run App** is a versatile utility designed to make running Python scripts as straightforward as launching any other application on your computer. With this program, you can turn your Python scripts into standalone applications that can be executed with a single click, without needing to manually activate a virtual environment or ensure that Python is installed on the system.

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
 



