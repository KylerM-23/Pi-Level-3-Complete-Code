import RPi.GPIO as GPIO
import time

buttonPin = 26
timePassed = 0

def setup():
    GPIO.setmode(GPIO.BCM)       # use BCM Numbering
    GPIO.setup(buttonPin, GPIO.IN)   # set the ledPin to OUTPUT mode
    GPIO.add_event_detect(buttonPin, GPIO.RISING, callback=interrupt_func, bouncetime=200)

def loop():
    global timePassed
    while(True):
        timePassed += 0.5
        time.sleep(0.5)

def interrupt_func(channel):
    while(GPIO.input(channel)):
          print(timePassed)

def destroy():
    GPIO.cleanup()                      # Release all GPIO
 
if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()
