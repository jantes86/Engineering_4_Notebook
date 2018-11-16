#Denver Riggleman Detector (give me that squatch)
#Jack Riggleman and James Riggleman

from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime

camera = PiCamera()

pir = MotionSensor(17)

while True:
    pir.wait_for_motion()
    print("We got one!")
    camera.start_recording("/home/pi/Documents/Engineering_4_Notebook/Python/Camera/Videos/DadGetOutOfMyRoom.h264")
    pir.wait_for_no_motion()
    print("no motion")
    camera.stop_recording()
print("done")
