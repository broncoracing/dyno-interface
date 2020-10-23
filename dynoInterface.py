import can
import time
import struct
from serial.tools import list_ports

SERVO_FRAME_ID = 0xCD # temp
# Searches USB serial ports for a device with "Protofusion Labs" as the manufacturer name.
def selectPort():
    portFound = False
    retries = 10
    while(portFound == False and retries >= 0):
        for port in list_ports.comports():
            if port.manufacturer == 'Protofusion Labs':
                print(f'Canable found at {port.device}')
                portFound = True
                return port.device
        retries = retries - 1;
        time.sleep(1)
        print('CANable not found, retrying...')

    exit(1)

# Stock slcan firmware on Windows
bus = can.interface.Bus(bustype='slcan', channel=selectPort(), bitrate=250000)

# make empty can frames
servoMsg = can.Message(data=[0, 0, 0, 0, 0, 0, 0, 0], arbitration_id=SERVO_FRAME_ID, dlc=8, is_extended_id=False)
inMsg = can.Message(data=[0, 0, 0, 0, 0, 0, 0, 0], arbitration_id=0, dlc=8, is_extended_id=False)

# example
servoMsg.data[0] = 1
servoMsg.data[1] = 200


def sendServoFrame(angle):
    servoMsg.data[0] = angle
    bus.send(servoMsg)

while 1:
    time.sleep(1)
    pidWantsThisAngle = 5
    sendServoFrame(pidWantsThisAngle)

    for inMsg in bus:
        print(f"Message ID: {inMsg.arbitration_id} data byte 0: {inMsg.data[0]}")
