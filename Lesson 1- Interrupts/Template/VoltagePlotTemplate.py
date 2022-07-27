import RPi.GPIO as GPIO
import time
from ADCDevice import *
import matplotlib.pyplot as plt

buttonPin = #set the pin number

time_data = []
voltage_data = []
collect = True

def setup():
    global adc
    
    adc = get_ADC(adc)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buttonPin, GPIO.IN)
    #add the event

def display_data(channel):
    global collect
    collect = False
    #plot the graph
    #show the graph
    destroy()
    
def loop():
    t = 0
    while collect:
        value = adc.analogRead(0)
        voltage = value / 255.0 * 3.3
        #add time and voltage data to lists
        #increment time by .1
        #sleep for .1 seconds

def destroy():
    GPIO.cleanup()                      # Release all GPIO
    
if __name__ == '__main__':
    print('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
