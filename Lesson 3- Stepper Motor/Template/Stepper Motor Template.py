import RPi.GPIO as GPIO
import time

motorPins = 

Halfstep = 

Fullstep = 

def setup():
    #setup the pins
    #output low
    
def moveOnePeriod(parameters):
    #set sequence based on what the user wants
    
    #loop through each step in the sequence
        #output the correct value to each pin
        #delay
        
def moveSteps():
    #use a for loop to call moveOnePeriod
    
def loop():
    while True:
        #add code to rotate the motor cw and ccw one rev
        
def destroy():
    GPIO.cleanup()
 
if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
