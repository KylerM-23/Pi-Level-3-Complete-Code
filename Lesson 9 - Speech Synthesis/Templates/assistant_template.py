import RPi.GPIO as GPIO
from synth_speech_utils import SynthVoice
from speech_detection_utils import SpeechDetection
import predict

class Assistant:
    def __init__(self, name = 'insert name'):
        self.name = 
        
        self.modelID = ""
        predict.set_model_ID(self.modelID)
        
        self.synth_speech = 
        self.detect_speech = 
        
        GPIO.setmode(GPIO.BCM)# use BCM Numbering
        self.ledPin = 21
        GPIO.setup(self.ledPin, GPIO.OUT)
    
    def classify_speech(self):
        text = 

        if text == None or text == "":
            return None   
        
        category, confidence = predict.text_classify(text)
        return category
    
    def loop(self):
        while True:
            #get the command from the mic
            
            #if the command isn't LISTEN
                #continue
            
            #turn on the LED
            #get the command from the mic
            
            #if the command is LISTEN
                #repeat the command
            #else
                #say "Sorry I didn't understant"
            
            #turn off the LED
    
    def close(self):
        GPIO.cleanup()
        self.synth_speech.close()
        
if __name__ == '__main__':
    ai = Assistant()
    
    try:
        ai.loop()
    except KeyboardInterrupt:
        ai.close()

