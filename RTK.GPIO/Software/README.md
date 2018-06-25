# RTK.GPIO Python Library

<img src="https://drive.google.com/uc?id=1WCpukpmTQwl-og_CEDyViTiW0BDwfyT4" width="400" height="400">

The RTK GPIO board allows you to connect the world of physical computing to you desktop PC or laptop. The RTK GPIO board emulates the original Raspberry Pi 28-pin GPIO header allowing you to program for the Raspberry Pi on your computer. The board is fully compatible with Windows, Mac OS and Linux and supports a range of programming languages such as Python, Java and also use with Scratch.

The board connects to your computer using a micro USB cable (not supplied), which also provides power to the board.

## Linux

The following guide has been tested to work with Debian Linux, in particular on the Raspberry Pi computer itself. There are a number of dependancies that also need to be installed such as some Python3 modules. To install the RTk.GPIO library there are just 4 simple steps:

1. Permission Change

To begin we are going to first add the user to the "dialout" group. This means after installation you don't have to use sudo to run the python programs.

Open the Linux temrinal and type i the following command:
```bash
sudo usermod -a -G dialout $USER
```

2. Python Requirements

Now we are going to make sure that Python and its libraries are installed. For the RTk.GPIO library we need to use Python3 packages. Open up the terminal and type in the following command:

```bash
sudo apt-get install python3-pip python3-setuptools python3-wheel
```

3. Reboot and Plug in

To make sure everything installed ok and is in sync it is recommended to initialise a reboot. While some aspects will work you may experience issues without a reboot.

After rebooting your Linux OS you can now insert your RTk.GPIO board into your Linux PC or Raspberry Pi. When you insert the USB cable you should see the Red LED light up.

4. Installing the Library

There are a couple of ways you can install the RTk.GPIO library. The easiest way is to use the Python in Package (PIP) management system. To install the RTk.GPIO library use the following command form the terminal:

```bash
sudo -H pip3 install RTk
```

Alterntaviely if you download this GitHub repository you can run the following command:

```bash
sudo python setup.py install
```

## Mac OS

1. Install Drivers

Mac OS does not include the required driver like most Linux operating systems and does not have central driver system like windows, therefore a driver has to be installed to communicate with the UART chipset on the RTk.GPIO board.

The manufacturer of the chipset provides a driver, however it causes issues on the latest version of OS (Sierra). A user on GitHub has a modified fix that has resolved some of those issues. Download the files from https://github.com/adrianmihalko/ch340g-ch34g-ch34x-mac-os-x-driver and install the driver package. Note: A reboot is required

2. Reboot and Plug in

After you have rebooted you Mac you can now plug in your RTk.GPIO board using a micro USB cable. When you connect the board you should see the Red LED light up to indicate it has power to the board.

3. Installing the library

here are a couple of ways you can install the RTk.GPIO library. The easiest way is to use the Python in Package (PIP) management system. To install the RTk.GPIO library use the following command form the terminal:

```bash
sudo -H pip3 install RTk
```

Alterntaviely if you download this GitHub repository you can run the following command from the Software directory:

```bash
sudo python setup.py install
```

## Windows
These instructions should work for Windows 7, 8 and 10.

1. Install Python

You can download the latest Python packages from https://www.python.org/downloads . The RTk.GPIO library was programmed using Python 3.6 but if there is a newer version then please download the latest version. Wait for the download to finish then click on the installer and follow the on-screen instructions to install Python.

A pop up box may appear asking you if you want to  allow the app to make changes. Click Yes to install.

2. Connect your board

Now you can connect the RTk.GPIO board to your computer using a micro USB cable. When you plug it in to your USB port you shoudl see the Red LED light up to indicate it is powered up. When you connect it to a windows computer it should automatically detect and install the drivers automatically for you.

3. Install RTk.GPIO Library

To install the RTk.GPIO library you will need to open the command prompt within Windows and type in the following command:

```bash
pip3 install RTk
```
Note: PIP installs with Python on Windows platform

## Python IDE

There are a number of examples that you can use in the Software > examples folder, however if you wish to program your own Python programs then you will need to either use a text editor from the command line such as nano or a graphical interface such as Atom.

You download the latest version of Atom from http://atom.io

The Python Library requires the following line in your code:

```python
from RTk import GPIO
```
