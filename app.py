#!/usr/bin/env python3

from datetime import datetime, timezone
from time import sleep
import json
from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice
from digi.xbee.util import utils

from pprint import pprint

PORT = "/dev/ttyUSB0"
BAUD_RATE = 9600

# See https://github.com/winlinvip/SimpleDHT/blob/master/SimpleDHT.h
DHT_ERROR_CODES = {
    0x10: "Error to wait for start low signal",
    0x11: "Error to wait for start high signal",
    0x12: "Error to wait for data start low signal.",
    0x13: "Error to wait for data read signal",
    0x14: "Error to wait for data EOF signal",
    0x15: "Error to validate the checksum",
    0x16: "Error when temperature and humidity are zero, it shouldn't happen",
    0x17: "Error when pin is not initialized"
}


def main():

    xbee_remote_devices = {}

    device = XBeeDevice(PORT, BAUD_RATE)

    def load_remote_device_info():
        xbee_network = device.get_network()
        xbee_network.start_discovery_process()
        
        while xbee_network.is_discovery_running():
            sleep(0.5)

        xbee_devices = xbee_network.get_devices()
        
        for remote_device in xbee_devices:
            try:
                remote_device.read_device_info()
            except:
                continue
            
            xbee_remote_devices[str(remote_device.get_16bit_addr())] = {
                "node_id": remote_device.get_node_id()
            }


    def data_receive_callback(xbee_message):
        
        time_zone = datetime.now(timezone.utc).astimezone().tzinfo
        timestamp = datetime.fromtimestamp(xbee_message.timestamp, tz=time_zone).isoformat()

        addr = xbee_message.remote_device.get_16bit_addr()

        node_id = xbee_remote_devices[str(addr)]["node_id"]

        data = {
            "timestamp": timestamp,
            "device": {
                "node_id": node_id,
                "16bit_addr": utils.hex_to_string(addr.address)
            }
        }

        if xbee_message.data[0]:
            data["error"] = {
                "id": xbee_message.data[1],
                "message": DHT_ERROR_CODES[xbee_message.data[1]]
            }
        else:
            data["observations"] = { 
                "temperature": xbee_message.data[2],
                "humidity": xbee_message.data[3]
            }

        print(json.dumps(data))


    try:
        device.open()

        load_remote_device_info()

        device.add_data_received_callback(data_receive_callback)

        print(f"Node {device.get_node_id()} is waiting for data...\n")
        input()

    finally:
        if device is not None and device.is_open():
            print("Closing device")
            device.close()


if __name__ == '__main__':
    main()