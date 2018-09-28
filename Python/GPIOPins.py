#GPIO Pins
#Jack Antes and James O'Brien

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led1 = 22
led2 = 24

counter = 0

GPIO.setup(led1, GPIO.OUT, initial = 0)
GPIO.setup(led2, GPIO.OUT, initial = 1)

while counter <= 10:
    GPIO.output(led1, 1)
    GPIO.output(led2, 0)
    time.sleep(1)
    GPIO.output(led1, 0)
    GPIO.output(led2, 1)
    time.sleep(1)
    counter = counter + 1

GPIO.cleanup()
