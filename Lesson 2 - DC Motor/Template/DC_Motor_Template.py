import RPi.GPIO as GPIO
import time
from ADCDevice import *

direction1 = 
direction2 = 
enable = 
motorPins = [direction1, direction2, enable]

def setup():
    global adc, dp1, dp2
    
    adc = get_ADC(adc)
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motorPins, GPIO.OUT)
    
    #create two PWM pins dp1 & dp2
    #output GPIO.HIGH to the enable
    
def mapNum( value, fromLow, fromHigh, toLow, toHigh):  # map a value from one range to another range
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow
 
def motor(ADC):
    #calculate the value
    #set the max speed
        
    if (value > 0):
        #change the speeds
    
    elif (value < 0):
        #change the speeds
    
    else:
        #turn both off

    print("The speed is",value, "ADC is: ", ADC)
    
def loop():
    while True:
        value = adc.analogRead(0)
        motor(value)
        time.sleep(0.1)
        
def destroy():
    #stop the motors
    GPIO.cleanup()
 
if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
