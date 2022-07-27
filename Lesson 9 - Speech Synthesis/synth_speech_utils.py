import pyttsx3

class SynthVoice:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.set_speed(125)
    
    def set_speed(self, rate):
        #param int rate: voice rate
        self.engine.setProperty('rate', rate)
    
    def set_volume(self, vol):
        #param float vol: values between 0, 1
        self.engine.setProperty('volume', vol)
    
    def set_voice(self, voice_num):
        #param int voice_num: 0 for male, 1 for female
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[voice_num].id)
    
    def say(self, term):
        self.engine.say(term)
        self.engine.runAndWait()

    def close(self):
        self.engine.stop()

if __name__ == '__main__':
    speech = SynthVoice()
    speech.set_voice(1)
    speech.set_volume(.5)
    speech.say('This is a test!')
    speech.close()
