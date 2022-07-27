import RPi.GPIO as GPIO
import time
from ADCDevice import *

direction1 = 11
direction2 = 13
enable = 15
motorPins = [direction1, direction2, enable]

buttonPin = 37
running = True

def setup():
    global adc, dp1, dp2
    
    adc = get_ADC(adc)
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motorPins, GPIO.OUT)
    
    dp1 = GPIO.PWM(direction1, 1000)
    dp1.start(0)
    
    dp2 = GPIO.PWM(direction2, 1000)
    dp2.start(0)
    
    GPIO.output(enable, running)
    
    GPIO.setup(buttonPin, GPIO.IN)
    GPIO.add_event_detect(buttonPin, GPIO.RISING, callback=start_stop, bouncetime=200)

def start_stop(channel):
    global running
    running = not running
    GPIO.output(enable, running)

def mapNum( value, fromLow, fromHigh, toLow, toHigh):  # map a value from one range to another range
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow
 
def motor(ADC):
    value = ADC-128
    maxSpeed = 128
        
    if (value > 0):
        dp1.ChangeDutyCycle(mapNum(abs(value), 0, maxSpeed, 0, 100))
        dp2.ChangeDutyCycle(0)
    
    elif (value < 0):
        dp1.ChangeDutyCycle(0)
        dp2.ChangeDutyCycle(mapNum(abs(value), 0, maxSpeed, 0, 100))
    
    else:
        dp1.ChangeDutyCycle(0)
        dp2.ChangeDutyCycle(0)

    print("The speed is",value, "ADC is: ", ADC)
    
def loop():
    while True:
        value = adc.analogRead(0)
        motor(value)
        time.sleep(0.1)
        
def destroy():
    dp1.stop()
    dp2.stop()
    GPIO.cleanup()
 
if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()

