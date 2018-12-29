# hub-sensor-xbee-temp

Collects weather observations from an XBee device (usually an Arduino)

The `dh11_basic.ino` program needs to be loaded to your Arduino. 

Build the container:

    docker build --rm -f "Dockerfile" -t hub-sensor-xbee-temp:latest .

To run the container:

    docker run --rm -ti --device /dev/ttyUSB0 hub-sensor-xbee-temp:latest

## References

* [Digi XBee Python library](https://github.com/digidotcom/python-xbee)
* [XBee®/Arduino Compatible Coding Platform](https://github.com/digidotcom/XBeeArduinoCodingPlatform)
* [XBee API Mode Tutorial Using Python and Arduino](https://serdmanczyk.github.io/XBeeAPI-PythonArduino-Tutorial/)