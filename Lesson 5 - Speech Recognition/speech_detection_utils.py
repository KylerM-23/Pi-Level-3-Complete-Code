import os
import queue
import sounddevice as sd
import vosk
import sys
import json

class SpeechDetection:
    def __init__(self, model_path='model'):
        self.q = queue.Queue()
        self.device = None
        self.samplerate = 44100
        self.model = vosk.Model(model_path)

    def callback(self, indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(indata))

    def recognize_speech_from_mic(self):
        with sd.RawInputStream(samplerate=self.samplerate,
                blocksize = 8000, device=self.device, dtype='int16',
                channels=1, callback=self.callback):

            rec = vosk.KaldiRecognizer(self.model, self.samplerate)
            
            transcribed = {}
            full_sentence = False
            while not full_sentence:
                data = self.q.get()
                if rec.AcceptWaveform(data):
                    transcribed = rec.Result()
                    full_sentence = True
                else:
                    transcribed = rec.PartialResult()
            
            transcribed_text = self.parse_result(transcribed)
            return transcribed_text
    
    def parse_result(self, transcribed):
        transcribed = json.loads(transcribed)
        return transcribed['text']
'''
param str transcribed: result from recognition
return str: text, if no speech input return ''
example: {"result" : [{
            "conf" : 0.437097,
            "end" : 0.420000,
            "start" : 0.000000,
            "word" : "these"
            }, {
            "conf" : 1.000000,
            "end" : 1.500000,
            "start" : 0.870000,
            "word" : "test"
            }],
            "text" : "these test"}
'''

if __name__ == '__main__':
    detect_speech = SpeechDetection()
    try:
        while True:
            transcribed_text = detect_speech.recognize_speech_from_mic()
            print(transcribed_text)
    except KeyboardInterrupt:
        print('\nDone')
    except Exception as e:
        print(e)

