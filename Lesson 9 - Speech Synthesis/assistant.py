import RPi.GPIO as GPIO
from synth_speech_utils import SynthVoice
from speech_detection_utils import SpeechDetection
import predict

class Assistant:
    def __init__(self, name = 'assistant'):
        self.name = name
        
        self.modelID = ""
        predict.set_model_ID(self.modelID)
        
        self.synth_speech = SynthVoice()
        self.detect_speech = SpeechDetection()
        
        GPIO.setmode(GPIO.BCM)# use BCM Numbering
        self.ledPin = 21
        GPIO.setup(self.ledPin, GPIO.OUT)
    
    def classify_speech(self, contains = None):
        text = self.detect_speech.recognize_speech_from_mic()

        if text == None or text == "" or (contains != None and contains not in text):
            return None   
        
        category, confidence = predict.text_classify(text)
        return category
    
    def say(self, word):
        self.synth_speech.say(word)
        
    def loop(self):
        while True:
            command = self.classify_speech(self.name)
            if (command != 'LISTEN'):
                continue
            GPIO.output(self.ledPin, GPIO.HIGH)
            
            command = self.classify_speech()
            if command == 'LISTEN':
                self.say("Command recieved " + command)
            else:
                self.say("Sorry, I didn't get that.") 
            GPIO.output(self.ledPin, GPIO.LOW)
        
    
    def close(self):
        GPIO.cleanup()
        self.synth_speech.close()
        
if __name__ == '__main__':
    ai = Assistant()
    
    try:
        ai.loop()
    except KeyboardInterrupt:
        ai.close()

