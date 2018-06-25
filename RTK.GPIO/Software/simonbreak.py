import time

TIME = 0.1
import RTk.GPIO as GPIO
from threading import Thread
BUTTON = 25

RED =24
YEL =23
GRN=22

GPIO.setmode(GPIO.BCM)

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YEL, GPIO.OUT)
GPIO.setup(GRN, GPIO.OUT)

GPIO.setup(BUTTON, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.output(GRN, True)

def pinread():
    while True:
        time.sleep(TIME)
        b = GPIO.input(BUTTON)
        if not b:
            print("pressed")
        else:
            print("released")

def pinwrite():
    while True:
        GPIO.output(GRN, False)
        GPIO.output(YEL, True)
        time.sleep(TIME * 10)
        GPIO.output(YEL, False)
        GPIO.output(RED, True)
        time.sleep(TIME * 10)
        GPIO.output(YEL, True)
        time.sleep(TIME * 10)
        GPIO.output(RED, False)
        GPIO.output(YEL, False)
        GPIO.output(GRN, True)
        time.sleep(TIME * 10)

try:
    i = Thread(target=pinread)
    i.start()
    o = Thread(target=pinwrite)
    o.start()
finally:
    GPIO.cleanup()
