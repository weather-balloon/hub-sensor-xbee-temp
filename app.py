#!/usr/bin/env python3

from datetime import datetime, timezone
from digi.xbee.devices import XBeeDevice

PORT = "/dev/ttyUSB0"
BAUD_RATE = 9600

def main():

    def data_receive_callback(xbee_message):
        time_zone = datetime.now(timezone.utc).astimezone().tzinfo
        print("{}\t{}\t{}".format(datetime.fromtimestamp(xbee_message.timestamp, tz=time_zone).isoformat(),
                                    xbee_message.remote_device.get_node_id(),
                                    xbee_message.data.decode().strip()))

    device = XBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()
        
        device.add_data_received_callback(data_receive_callback)

        print(f"{device.get_node_id()} waiting for data...\n")
        input()

    finally:
        if device is not None and device.is_open():
            print("Closing device")
            device.close()


if __name__ == '__main__':
    main()