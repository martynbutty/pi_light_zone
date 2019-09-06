#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) # Ignore warnings for now
GPIO.setmode(GPIO.BOARD)

# setup every channel we want to use as an input or output
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP) # gpio pin 7 as input with pull up resistor

led_state = False

def button_callback(channel):
    global led_state
    led_state = not led_state
    GPIO.output(11, led_state)
    print("Button was pressed\n\n")
    # time.sleep(1) # debounce switch
    
    
GPIO.add_event_detect(13, GPIO.FALLING,callback=button_callback)

message = input("Press any key to quit\n\n")
GPIO.cleanup()

'''
while True:
  GPIO.output(11, GPIO.HIGH)
  # print('high')
  time.sleep(1)
  GPIO.output(11, GPIO.LOW)
  # print('low')
  time.sleep(1)
'''

