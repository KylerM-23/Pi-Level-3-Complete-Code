import RPi.GPIO as GPIO
import time

motorPins = [12, 16, 18, 22]

Halfstep = [[0,0,0,1], [0,0,1,1], [0,0,1,0],[0,1,1,0],
            [0,1,0,0], [1,1,0,0], [1,0,0,0], [1,0,0,1]]

Fullstep = [[0,0,0,1], [0,0,1,0], [0,1,0,0], [1,0,0,0]]

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motorPins, GPIO.OUT)
    GPIO.output(motorPins, GPIO.LOW)
    
def moveOnePeriod(stepType, direction, ms):
    if stepType == 'Half':
        Sequence = Halfstep
    else:
        Sequence = Fullstep
    
    for j in range(len(Sequence)):
        for i in range(len(motorPins)):
            if direction == 'CW':
                GPIO.output(motorPins[i], Sequence[j][i])
            else:
                GPIO.output(motorPins[i], Sequence[3-j][i])
            
        if (ms < 3):
            ms = 3
        time.sleep(ms * .001)
        
def moveSteps(steps, stepType = 'Half', direction = 'CW', ms = 3):
    for i in range(steps):
        moveOnePeriod(stepType, direction, ms)
    
def loop():
    while True:
        moveSteps(512, 'Half', 'CW')
        time.sleep(0.5)
        moveSteps(512, 'Half', 'CCW')
        time.sleep(0.5)
        
def destroy():
    GPIO.cleanup()
 
if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
