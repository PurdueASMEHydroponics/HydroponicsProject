#!/usr/bin/python
import sys
import Adafruit_DHT

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 16)
    tempF = temperature * (9.0/5.0) + 32

    print(tempF, 'Degrees Fahrenheit', humidity,'% Humidity')
