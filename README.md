## Setup

You must specify the port for the canable device in the software.

Ensure pip is installed (if the commands fail, try using pip3)

Install python-can:
pip install python-can

Install pyserial:
pip install pyserial

python-can documentation: https://python-can.readthedocs.io/en/master/installation.html

CANable requirements:
Must be flashed with the slcan (default) serial firmware. Use the link below (must use chrome)
Ensure that the "boot" jumper is in the correct position
https://canable.io/updater/

to send a message:
bus.send(outMsg)