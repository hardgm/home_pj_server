import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)

while(True):
    try:
        while 1:
            GPIO.output(23,GPIO.LOW)
            time.sleep(2)
            GPIO.output(23,GPIO.HIGH)
            time.sleep(2)
    finally:
        GPIO.cleanup()