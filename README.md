# What this is:

This is a Python program compatible with any os that is capable of downloading the file and have Python 3+ installed.

It is made to calculate hyperoperations until Hexation. It can calculate:

- Addition
- Multiplication
- Exponentiation
- Tetration
- Pentation
- Hexation

# System requirements

Super High end Gaming Computer OR a Super Computer.
If you run this program on a Home PC, there is a chance that the process is going to be killed because of taking too long to repond, freeze or even over-heat the CPU.

In general, it requires a very beefy and fast Processor. If you are not sure about if this is going to run on your PC, just try. If it takes too long, then just kill it.

# License:

You can modify this or use this for any purpose, except for illegal ones or re-selling the program without my own permission. I am not responsible for any misuse or damage caused by this program.

# How to run:

## On Windows >10
```
python path_to_hyperoperations_py
```
## On Ubuntu/Other Debian-based Linux distributions:
```
python3 path_to_hyperoperations_py
```
# How to build

## 1. Install PyInstaller

You can also use other tools, but I recommend this one.

### On Windows

(Make sure pip is in system PATH)
 ```
pip install pyinstaller
```

### On Debian-based Linux distributions

```
sudo apt update
sudo apt install python3-pip
pip install pyinstaller
```

If you encounter an error, then you may need to use a virtual environment. Execute the following commands one by one without modifying them. Ignore the commands that have a "#":

```
# Install the required package
sudo apt install python3-venv

# Prepare the directory
mkdir ~/python-environments
cd ~/python-environments

# Create the environment
python3 -m venv pyinstaller_virtual_enviroment

# Activate the environment
source my-project-env/bin/activate
```

## 2. Build it

### Windows

```
# Replace ABC with the path to the directory where you have the main .py file.
cd ABC

pyinstaller hyperoperations.py
```

If you want to customize the options, such as the name of the final program, icon, etc, please check the official PyInstaller [Documentation](https://pyinstaller.org/en/stable/index.html).

### Debian-based Linux distros

Activate the virtual environment, as mentioned [before](https://github.com/UserName-None/HyperOperation-Calculator/edit/main/README.md#on-debian-based-linux-distributions).

Use `cd` to navigate to the place where you have the .py file, and do:

```
pyinstaller hyperoperations.py
```

# For MacOS users, you may do some research on how to run Python files and create virtual environments on your Mac, because I do NOT have a Mac and I have NO idea of how it is or how to use it.
