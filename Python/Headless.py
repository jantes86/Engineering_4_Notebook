#Headless
#By Tina Antes and Tina O'Brien

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24

lsm303 = Adafruit_LSM303.LSM303()

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

disp.begin()

disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = 2
shape_width = 20
top = padding
x = padding

font = ImageFont.load_default()

while True:
    accel, mag = lsm303.read()
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.rectangle((0,0,128,int(accel_x)/10), outline=0, fill=100)

    disp.image(image)
    disp.display()

    time.sleep(.1)
    disp.clear()
