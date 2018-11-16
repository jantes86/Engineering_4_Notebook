#Camera Test 2
#By @JackToTheLeft and ________
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    sleep(5)
    if effect == 'colorswap':
        camera.capture('/home/pi/Documents/Engineering_4_Notebook/Python/Camera/Pics/effect%s.jpg' % effect)
    
    if effect == 'emboss':
        camera.capture('/home/pi/Documents/Engineering_4_Notebook/Python/Camera/Pics/effect%s.jpg' % effect)
    
    if effect == 'gpen':
        camera.capture('/home/pi/Documents/Engineering_4_Notebook/Python/Camera/Pics/effect%s.jpg' % effect)
    
    if effect == 'solarize':
        camera.capture('/home/pi/Documents/Engineering_4_Notebook/Python/Camera/Pics/effect%s.jpg' % effect)
    
    if effect == 'cartoon':
        camera.capture('/home/pi/Documents/Engineering_4_Notebook/Python/Camera/Pics/effect%s.jpg' % effect)


camera.stop_preview()
