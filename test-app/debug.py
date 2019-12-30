#!/usr/bin/env python3

from datetime import datetime, timezone
from time import sleep
import json
from digi.xbee.devices import XBeeDevice
from digi.xbee.util import utils


PORT = "/dev/ttyUSB0"
BAUD_RATE = 9600

def main():

    def get_parameter(xbee: XBeeDevice, param: str) -> str:
        return utils.hex_to_string(xbee.get_parameter(param))

    local_xbee = XBeeDevice(PORT, BAUD_RATE)

    try:
        local_xbee.open()
        
        xbee_network = local_xbee.get_network()

        print("Cheking network...", end='', flush=True)

        xbee_network.start_discovery_process()
        
        while xbee_network.is_discovery_running():
            sleep(0.5)

        xbee_devices = xbee_network.get_devices()

        print("done")
        
        print(f"""
LOCAL XBEE
  - Node ID: {local_xbee.get_node_id()}
  - PAN ID: {get_parameter(local_xbee, "ID")}
  - Protocol: {local_xbee.get_protocol()}
  - 16-bit address: {local_xbee.get_16bit_addr()}
  - 64-bit address: {local_xbee.get_64bit_addr()}
  - API: {get_parameter(local_xbee, "AP")}
  - Encryption enabled: {get_parameter(local_xbee, "EE")}
  - Hardware version: {local_xbee.get_hardware_version()}
  - Firmware version: {utils.hex_to_string(local_xbee.get_firmware_version())}

NETWORK
  - Remote devices: {len(xbee_devices)}
""")

        for remote_device in xbee_devices:
            if not (remote_device is None):
                try:
                    remote_device.read_device_info()
                except:
                    continue

                print(f"""
REMOTE DEVICE:      
- Node ID: {remote_device.get_node_id()}
- PAN ID: {get_parameter(remote_device, "ID")}
- Protocol: {remote_device.get_protocol()}
- 16-bit address: {remote_device.get_16bit_addr()}
- 64-bit address: {remote_device.get_64bit_addr()}
- API: {get_parameter(remote_device, "AP")}
- Encryption enabled: {get_parameter(remote_device, "EE")}
- Hardware version: {remote_device.get_hardware_version()}
- Firmware version: {utils.hex_to_string(remote_device.get_firmware_version())}
""")

    finally:
        if local_xbee is not None and local_xbee.is_open():
            print("Closing device")
            local_xbee.close()


if __name__ == '__main__':
    main()
