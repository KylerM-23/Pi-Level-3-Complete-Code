import RPi.GPIO as GPIO
import time
from ADCDevice import *
import matplotlib.pyplot as plt

buttonPin = 26

time_data = []
voltage_data = []
collect = True

def setup():
    global adc
    
    adc = get_ADC(adc)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buttonPin, GPIO.IN)
    GPIO.add_event_detect(buttonPin, GPIO.RISING, callback=display_data, bouncetime=200)

def display_data(channel):
    global collect
    collect = False
    plt.plot(time_data, voltage_data)
    plt.show()
    destroy()
    
def loop():
    t = 0
    while collect:
        value = adc.analogRead(0)
        voltage = value / 255.0 * 3.3
        time_data.append(t)
        voltage_data.append(voltage)
        t+=.1
        time.sleep(.1)

def destroy():
    GPIO.cleanup()                      # Release all GPIO
    
if __name__ == '__main__':
    print('Program is starting...')
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        destroy()
