import RPi.GPIO as GPIO
import time, datetime
 
#Fill in the missing variables
LSBFIRST = 1
MSBFIRST = 2
 
dataPin = 
latchPin = 
clockPin = 

pins = [dataPin, latchPin, clockPin]
anodes = 

timeSleep= 
 
num = [0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8,
       0x80, 0x90, 0x88, 0x83, 0xc6, 0xa1, 0x86, 0x8e]

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    
    #setup the pins as outputs
    #setup the anodes as outputs
    #turn off the anodes
 
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
    #turn off the anodes
    
    #turn on the anode you want
    #output the number to the display
    #sleep 2ms
    
    #clear all LEDs by outputting -1
    #turn off the anode
    #sleep 2ms
          
def loop():
    while True:
        #display 1
        #display 2, with DP
        #display 3
        #display 4
        
def destroy():
    GPIO.cleanup()
 
if __name__ == '__main__':
    print('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
