# invent.module143.com/daskal_tutorial/raspberry-pi-3-wireless-pi-to-arduino-communication-with-nrf24l01/

import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev

GPIO.setmode(GPIO.BCM)

pipes=[[0xE7, 0xE7, 0xE7, 0xE7, 0xE7],[0xC2, 0xC2, 0xC2, 0xC2, 0xC2]]

radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0,17)
