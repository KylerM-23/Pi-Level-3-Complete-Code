import RPi.GPIO as GPIO
import time

buttonPin = 26
timePassed = 0

def setup():
    #add the setup function

def loop():
    #add the loop function

#create the interrupt function

def destroy():
    GPIO.cleanup()                      # Release all GPIO
 
if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()
