import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

GPIO.output(26, GPIO.LOW)
GPIO.output(19, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(6, GPIO.LOW)

timeOn = 10

try:
    GPIO.output(26, GPIO.HIGH)
    print('One On')
    GPIO.output(19, GPIO.HIGH)
    print('Two On')
    GPIO.output(13, GPIO.HIGH)
    print('Three On')
    GPIO.output(6, GPIO.HIGH)
    print('Four On')
    time.sleep(timeOn)
    GPIO.cleanup()
    print('All Off')

except KeyboardInterrupt:
    print('User Quit')
    GPIO.cleanup()
    