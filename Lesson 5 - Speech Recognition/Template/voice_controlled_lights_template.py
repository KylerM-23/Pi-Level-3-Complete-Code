import RPi.GPIO as GPIO
from speech_detection_utils import SpeechDetection
import predict

LedPin = # define the LedPin
model_ID = "model ID"

def setup():
    global p, audio_recognizer
    GPIO.setmode(GPIO.BOARD)     
    GPIO.setup(LedPin, GPIO.OUT) 
    GPIO.output(LedPin, GPIO.LOW) 
 
    #create the PWM pin
    #start the pin
    #create the speech detection object
    #set the modelID
    
def loop():
    brightness = 0

    while True:
        #change the duty cycle to the value of brightness 
        #get text from the mic
        
        #if text is equal to None or to an empty string
            #continue  
    
        #classify the text and save the category and confidence
        
        #if the confidence is greater than 50
            #print the text
            #if the category is INCREASE
                #if brightness <= 90
                    #increase brightness by 10
                    #print('brighter')
            #else
                #if brightness >= 10
                    #decrease brightness by 10
                    #print('dimmer')

def destroy():
    p.stop() # stop PWM
    GPIO.cleanup() # Release all GPIO
 
if __name__ == '__main__':     # Program entrance
    print ('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy() 