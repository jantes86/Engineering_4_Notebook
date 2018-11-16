#Camera Test 1
#By jobrien89 and jantes86

from picamera import PiCamera
from time import sleep

myCam = PiCamera()

myCam.start_preview()
sleep(10)
myCam.stop_preview()
