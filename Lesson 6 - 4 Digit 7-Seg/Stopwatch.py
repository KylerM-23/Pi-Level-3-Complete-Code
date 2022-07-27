import RPi.GPIO as GPIO
import time, datetime
 
LSBFIRST = 1
MSBFIRST = 2
 
dataPin = 11
latchPin = 13
clockPin = 15

pins = [dataPin, latchPin, clockPin]
anodes = [37,36, 38, 40]

buttonPin = 35
stopWatchMode = True

timeSleep= .002
 
num = [0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8,
       0x80, 0x90, 0x88, 0x83, 0xc6, 0xa1, 0x86, 0x8e]

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pins, GPIO.OUT)
    GPIO.setup(anodes, GPIO.OUT)
    GPIO.output(anodes, GPIO.LOW)
    
    GPIO.setup(buttonPin, GPIO.IN)
    GPIO.add_event_detect(buttonPin, GPIO.RISING, callback=changeMode, bouncetime=200)

 
def shiftOut(dPin, cPin, order, val):
    for i in range(0,8):
        GPIO.output(cPin, GPIO.LOW)
        if(order == LSBFIRST):
            GPIO.output(dPin, (0x01&(val >>i) == 0x01) and GPIO.HIGH or GPIO.LOW)
        elif(order == MSBFIRST):
            GPIO.output(dPin, (0x80&(val <<i) == 0x80) and GPIO.HIGH or GPIO.LOW)
        GPIO.output(cPin, GPIO.HIGH)

def output7Seg(number, deci = False):
    GPIO.output(latchPin, GPIO.LOW)
    if (number > 16 or number < 0):
        result = 0xFF #Turn Off Display
    
    elif (deci):
        result = num[number] & 0x7F #Turn On The Decimal Point
    else:
        result = num[number] #Output Number
        
    shiftOut(dataPin, clockPin, MSBFIRST, result)
    GPIO.output(latchPin, GPIO.HIGH)

def display(num, digit, decimal = False):
    GPIO.output(anodes, GPIO.LOW)
    
    GPIO.output(anodes[digit], GPIO.HIGH)
    output7Seg(num, decimal)
    
    time.sleep(timeSleep)
    
    output7Seg(-1)
    GPIO.output(anodes[digit], GPIO.LOW)
    time.sleep(timeSleep)
        
def changeMode(channel):
    global stopWatchMode
    stopWatchMode = not stopWatchMode

def stopWatch():
    minute = 0
    second = 0
    timeRef = time.time()
    
    while stopWatchMode:
        display(minute//10, 0)
        display(minute%10, 1, True)
        display(second//10, 2)
        display(second%10, 3)
        
        if (time.time()-timeRef >= 1):
            second += 1
            timeRef = time.time()
            
        if (second >= 60):
            second = 0
            minute += 1
            
        if minute >= 60:
            minute = 0
        
    while not stopWatchMode:
        display(minute//10, 0)
        display(minute%10, 1, True)
        display(second//10, 2)
        display(second%10, 3)

def loop():
    while True:
        stopWatch()
        
def destroy():
    GPIO.cleanup()
 
if __name__ == '__main__':
    print('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
