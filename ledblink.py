import RPi.GPIO as GPIO
import time

LEDPIN = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LEDPIN,GPIO.OUT)

while(1):
    GPIO.output(LEDPIN,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LEDPIN,GPIO.LOW)
    time.sleep(1)
