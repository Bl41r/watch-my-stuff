# watch-my-stuff
Simple OpenCV Python project to take and save pictures of human faces that come into the field of view of a webcam.


## Background
Every last weekend of the month, some prankster at the office likes to go
around and move everyone's stuff on their desks around.  Well, not anymore!

This is a simple project using Python and OpenCV to run on a small device,
such as a Raspberry Pi with a webcam, to monitor my desk.  It will take a
picture of anyone's face who comes within the field of view of the webcam.

## Installation
- install OpenCV (google how to do this)
- clone the repo
- cd into the project directory
- create and activate a virtual environment (or just use the same one you
are using for OpenCV if you installed it using a virtual environment)
```
python3 -m venv ENV
source ENV/bin/activate
```
- install requirements
```
pip install -r requirements.txt
```
- run the script
```
python3 watcher.py
```
- profit
- pictures will be saved in an IMG directory, with the timestamp as the
filename
