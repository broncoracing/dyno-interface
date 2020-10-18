import can

def canDump(CANablePort):
    bus = can.interface.Bus(bustype='slcan', channel=CANablePort, bitrate=250000)
    inMsg = can.Message(data=[0, 0, 0, 0, 0, 0, 0, 0], arbitration_id=0, dlc=8, is_extended_id=False)

    print("ID    DLC \tDATA")

    while 1:
        for inMsg in bus:
            IDString = '{:02X}'.format(inMsg.arbitration_id)
            print('\033[96m' + f'0x{IDString}  [{inMsg.dlc}]  ' + '\033[0m', end='')

            for i in range(inMsg.dlc):
                byteString = '{:02X}'.format(inMsg.data[i])
                print(byteString, end=' ')

            print('')


canDump('/dev/cu.usbmodem14101')