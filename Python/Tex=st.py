from time import sleep
import RPi.GPIO as GPIO
from gpiozero import Buzzer
GPIO.setmode(GPIO.BCM)
buzzer = Buzzer(17)

while True:
    buzzer.on()
    sleep(1)
    buzzer.off()
    sleep(1)

