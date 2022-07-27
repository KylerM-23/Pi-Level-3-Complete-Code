import RPi.GPIO as GPIO
import time
 
LSBFIRST = 1
MSBFIRST = 2

#fill in the pin numbers
Col_dataPin = 
Col_latchPin = 
Col_clockPin = 

Row_dataPin = 
Row_latchPin = 
Row_clockPin = 

Col = [Col_dataPin, Col_latchPin, Col_clockPin]
Row = [Row_dataPin, Row_latchPin, Row_clockPin]

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    #setup up the pins as outputs
 
def shiftOut(dPin, cPin, order, val):
    for i in range(0,8):
        GPIO.output(cPin, GPIO.LOW)
        if(order == LSBFIRST):
            GPIO.output(dPin, (0x01&(val >>i) == 0x01) and GPIO.HIGH or GPIO.LOW)
        elif(order == MSBFIRST):
            GPIO.output(dPin, (0x80&(val <<i) == 0x80) and GPIO.HIGH or GPIO.LOW)
        GPIO.output(cPin, GPIO.HIGH)

def outputData(value, dataPin, latchPin, clockPin, order):
    #set the latch pin to low
    #call the shift out function
    #output the latchpin to high

picture = [0b1111_1111,
           0b1101_1011,
           0b1111_1111,
           0b1111_1111,
           0b1011_1101,
           0b1100_0011,
           0b1111_1111,
           0b1111_1111]

def loop():
    while True:
        #for in range(number of rows)
            #output the row to turn on with MSBFIRST
            #output the picture data with LSBFIRST
            #sleep for 1ms
            
def destroy():
    GPIO.cleanup()
 
if __name__ == '__main__':
    print('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()


