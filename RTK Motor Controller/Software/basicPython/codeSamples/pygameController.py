#RTK-000-001 Pygame Controller
#Licensed under the GNU GPL V3 License
#(C) Ryanteck LTD. 2014
#Contributors: Ryan Walmsley, Michael Horne 
from sys import exit
import time
import pygame
import RPi.GPIO as GPIO

pygame.init()
screen = pygame.display.set_mode((480,480))

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

def forwards():
        GPIO.output(17,1)
        GPIO.output(18,0)
        GPIO.output(22,1)
        GPIO.output(23,0)

def backwards():
        GPIO.output(17,0)
        GPIO.output(18,1)
        GPIO.output(22,0)
        GPIO.output(23,1)

def left():
        GPIO.output(17,0)
        GPIO.output(18,1)
        GPIO.output(22,1)
        GPIO.output(23,0)

def right():
        GPIO.output(17,1)
        GPIO.output(18,0)
        GPIO.output(22,0)
        GPIO.output(23,1)

def stop():
        GPIO.output(17,0)
        GPIO.output(18,0)
        GPIO.output(22,0)
        GPIO.output(23,0)

while True:
        pygame.display.flip()
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_RIGHT]:
                print "right"
                right()

        elif keystate[pygame.K_LEFT]:
                print "left"
                left()

        elif keystate[pygame.K_DOWN]:
                print "back"
                backwards()

        elif keystate[pygame.K_UP]:
                print "up"
                forwards()
        else:
                stop()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        exit(0)

        time.sleep(0.01)

