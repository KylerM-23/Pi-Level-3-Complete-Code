import RPi.GPIO as GPIO
import time

buttonPin = 26
press = 0

def setup():
    GPIO.setmode(GPIO.BCM)           # use BCM Numbering
    GPIO.setup(buttonPin, GPIO.IN)   # set the button as an input
    GPIO.add_event_detect(buttonPin, GPIO.RISING, callback=interrupt_func, bouncetime=50)

def interrupt_func(channel):
    global press
    press+=1
    print("Button at pin", channel, "pressed", press, "times")

def loop():
    while(True):
        continue
    
def destroy():
    GPIO.remove_event_detect(buttonPin) #remove the interrupt
    GPIO.cleanup()                      # Release all GPIO
 
if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()