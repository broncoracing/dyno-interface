import can
from serial.tools import list_ports

def selectPort():
    for port in list_ports.comports():
        if port.manufacturer == 'Protofusion Labs':
            print(f'Canable found at {port.device}')
            return port.device


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