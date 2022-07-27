import pyttsx3

class SynthVoice:
    def __init__(self):
        #create engine
        #set speed to 125
    
    def set_speed(self, rate):
        #set voice rate
    
    def set_volume(self, vol):
        #set volume
    
    def set_voice(self, voice_num):
        #get voices
        #set voice
    
    def say(self, term):
        self.engine.say(term)
        self.engine.runAndWait()

    def close(self):
        self.engine.stop()

if __name__ == '__main__':
    #create the synth voice
    #set the gender to Male or Female
    #set the volume
    #say something
    #close the voice
