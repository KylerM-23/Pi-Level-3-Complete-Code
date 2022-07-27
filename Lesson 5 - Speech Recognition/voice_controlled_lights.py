import RPi.GPIO as GPIO
from speech_detection_utils import SpeechDetection
import predict

LedPin = 12     # define the LedPin
model_ID = "44307eb3-b4aa-4d11-9007-d99c00b911f1"

def setup():
    global p, audio_recognizer
    GPIO.setmode(GPIO.BOARD)     
    GPIO.setup(LedPin, GPIO.OUT) 
    GPIO.output(LedPin, GPIO.LOW) 
 
    p = GPIO.PWM(LedPin, 500)  
    p.start(0)                    
    audio_recognizer = SpeechDetection()
    predict.set_model_ID(model_ID)
    
def loop():
    brightness = 0

    while True:
        p.ChangeDutyCycle(brightness)  
        text = audio_recognizer.recognize_speech_from_mic()
        
        if text == None or text == "":
            continue    
    
        category, confidence = predict.text_classify(text)
        
        if confidence > 50:
            print(text)
            if category == "INCREASE":
                if (brightness <= 90):
                    brightness += 10
                print('brighter')
            else:
                if (brightness >= 10):
                    brightness -= 10
                print('dimmer')

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