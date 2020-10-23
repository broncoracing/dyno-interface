import can
import time
from serial.tools import list_ports
import os

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

# Connects to and configures CANable device, dumps frame ID, DLC, and data
def canDump(CANablePort, bitRate):
    bus = can.interface.Bus(bustype='slcan', channel=CANablePort, bitrate=bitRate)
    inMsg = can.Message(data=[0, 0, 0, 0, 0, 0, 0, 0], arbitration_id=0, dlc=8, is_extended_id=False)

    while 1:
        for inMsg in bus:
            IDString = '{:02X}'.format(inMsg.arbitration_id)
            print(f'0x{IDString}\t[{inMsg.dlc}]  ', end='')

            for i in range(inMsg.dlc):
                byteString = '{:02X}'.format(inMsg.data[i])
                print(byteString, end=' ')

            print('')

canDump(selectPort(), 250000)