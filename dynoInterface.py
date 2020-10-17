import can
import time

# change this to COMX if on windows
CANABLE_PORT = '/dev/cu.usbmodem14301'

SERVO_FRAME_ID = 0xCD # temp

# Stock slcan firmware on Windows
bus = can.interface.Bus(bustype='slcan', channel=CANABLE_PORT, bitrate=250000)

# make empty can frames
servoMsg = can.Message(data=[0, 0, 0, 0, 0, 0, 0, 0], arbitration_id=SERVO_FRAME_ID, dlc=8, is_extended_id=False)
inMsg = can.Message(data=[0, 0, 0, 0, 0, 0, 0, 0], arbitration_id=0, dlc=8, is_extended_id=False)

# example
servoMsg.data[0] = 1
servoMsg.data[1] = 200


def sendServoFrame():
    bus.send(servoMsg)

while 1:
    time.sleep(1)

    sendServoFrame()

    for inMsg in bus:
        print(f"Message ID: {inMsg.arbitration_id} data byte 0: {inMsg.data[0]}")
