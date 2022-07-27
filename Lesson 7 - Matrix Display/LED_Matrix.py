import RPi.GPIO as GPIO
import time
 
LSBFIRST = 1
MSBFIRST = 2
 
Col_dataPin = 11
Col_latchPin = 13
Col_clockPin = 15

Row_dataPin = 36
Row_latchPin = 38
Row_clockPin = 40

Col = [Col_dataPin, Col_latchPin, Col_clockPin]
Row = [Row_dataPin, Row_latchPin, Row_clockPin]

timeSleep = .5


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Col + Row, GPIO.OUT)
 
def shiftOut(dPin, cPin, order, val):
    for i in range(0,8):
        GPIO.output(cPin, GPIO.LOW)
        if(order == LSBFIRST):
            GPIO.output(dPin, (0x01&(val >>i) == 0x01) and GPIO.HIGH or GPIO.LOW)
        elif(order == MSBFIRST):
            GPIO.output(dPin, (0x80&(val <<i) == 0x80) and GPIO.HIGH or GPIO.LOW)
        GPIO.output(cPin, GPIO.HIGH)

def outputData(value, dataPin, latchPin, clockPin, order = LSBFIRST):
    GPIO.output(latchPin, GPIO.LOW)
    shiftOut(dataPin, clockPin, order, value)
    GPIO.output(latchPin, GPIO.HIGH)

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
        for i in range(8):
            outputData(0xFF, Col[0], Col[1], Col[2], LSBFIRST)
            outputData(2**i, Row[0], Row[1], Row[2], MSBFIRST)
            outputData(picture[i], Col[0], Col[1], Col[2], LSBFIRST)
            time.sleep(.001)
            
def destroy():
    GPIO.cleanup()
 
if __name__ == '__main__':
    print('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

