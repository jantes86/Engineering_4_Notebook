#Camera Test 2003 (a good year)
#James O'Brien and Jack Antes

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.start_recording('/home/pi/Documents/Engineering_4_Notebook/Python/Camera/Videos/Video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()
