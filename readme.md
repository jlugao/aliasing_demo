# Aliasing_demo

GUI demonstrating the effect of aliasing in sinusoidal waves. 

This project is part of a series of applets being made to demonstrate important Digital Signal Processing concepts using open source resources. Most of the demonstrations and examples currently avaliable in this area are written for matlab or simulink, this stops the users from 1- being able to run the examples freely and 2- editing the source code to make their own version of the applet.


## How to install
The current implementation is cross-platform because I'm using mainly numpy and pyqt, however there is no self-extractor or anything like that so dependencies must be installed manually in linux and ios.

#### Windows

  * Install [PythonXY](https://code.google.com/p/pythonxy/).
  * download zip file and extract.
  * Go to project folder and run it

#### Linux

  * First install python 2.7 and PyQt4 and pip.

```
sudo apt-get install python2.7 python-pip python-qt4 qt4-dev-tools build-essential git git-core git-doc
```

  * Then, install the dependencies

```
pip install numpy matplotlib scipy
```

  * Get the files.

```
git clone https://github.com/jlugao/aliasing_demo.git
cd aliasing_demo
./pds3.py

```
