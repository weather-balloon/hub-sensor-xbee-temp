# hub-sensor-xbee-temp

Collects weather observations from an XBee device (usually an Arduino)

The `dh11_basic.ino` program needs to be loaded to your Arduino. 

Build the container:

    docker build --rm -f "Dockerfile" -t hub-sensor-xbee-temp:latest .

To run the container:

    docker run --rm -ti --device /dev/ttyUSB0 hub-sensor-xbee-temp:latest

To run and develop:

    docker run --rm -ti --volume $(pwd):/app --device /dev/ttyUSB0 --entrypoint /bin/sh hub-sensor-xbee-temp:latest

## References

* [Digi XBee Python library](https://github.com/digidotcom/python-xbee)
* [XBee®/Arduino Compatible Coding Platform](https://github.com/digidotcom/XBeeArduinoCodingPlatform)
* [XBee API Mode Tutorial Using Python and Arduino](https://serdmanczyk.github.io/XBeeAPI-PythonArduino-Tutorial/)
* [Programming Arduino Wirelessly](https://www.faludi.com/itp_coursework/meshnetworking/XBee/XBee_program_Arduino_wireless.html)
* [http://www.fiz-ix.com/2012/11/low-power-xbee-sleep-mode-with-arduino-and-pin-hibernation/](http://www.fiz-ix.com/2012/11/low-power-xbee-sleep-mode-with-arduino-and-pin-hibernation/)