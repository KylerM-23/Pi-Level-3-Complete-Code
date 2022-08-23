import RPi.GPIO as GPIO
import time

buttonPin = 26
press = 0

def setup():
    GPIO.setmode(GPIO.BCM)           # use BCM Numbering
    GPIO.setup(buttonPin, GPIO.IN)   # set the buttonPin to OUTPUT mode
    GPIO.add_event_detect(buttonPin, GPIO.RISING, callback=interrupt_func, bouncetime=30)

def interrupt_func(channel):
    global press
    press+=1

def loop():
    print("Get ready to mash the button for ten seconds.")
    time.sleep(1)
    print("Go")
    time.sleep(10)
    print("You pressed the button", press,"times in 10 seconds.")

def destroy():
    GPIO.remove_event_detect(buttonPin) #remove the interrupt
    GPIO.cleanup()                      # Release all GPIO
 
if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
        destroy()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()