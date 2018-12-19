import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((640,640))

pygame.display.set_caption('EXHIBIT CLOSED: FUTURE HOME OF THE MONA LISA')

pess = (205,205,34)
screen.fill(pess)

for i in range(0,64):
    for j in range(0,64):
        pygame.draw.rect(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255))
, (i*10,j*10,10,10), 0) 

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();
