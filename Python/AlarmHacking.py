#Alarm Hacking Big Oil Fracking in Your Mouth English Class is Lacking The Opposite of White Out is Blacking A type of shot that follows is Tracking Withes on Halloween are Cackling The Pavement Outside this School is Cracking Bitches be Shopping and Ducks be Quacking Alechemists be Refracting People tied together are shackling An offspring of Jack is a Jackling football players and ratatas are tackling These weeds need some wacking A gun that fires real quick is gattling I need to leave better start packing Newton's Cradle balls are clacking
#James O'Brien and Jack Antes

import RPi.GPIO as GPIO, time, os

GPIO.setmode(GPIO.BCM)

buzzer = 4

GPIO.setup(buzzer, GPIO.OUT)
def RCtime(RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)
    while(GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading

while True:
    print(RCtime(18))
    if RCtime(18) >> 9:
        GPIO.output(buzzer, GPIO.HIGH)
    else:
        GPIO.output(buzzer, GPIO.LOW)
