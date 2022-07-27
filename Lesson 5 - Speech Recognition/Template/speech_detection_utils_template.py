import os
import queue
import sounddevice as sd
import vosk
import sys
import json

class SpeechDetection:
    def __init__(self, model_path='model'):
        #create the properties for the class

    def callback(self, indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        #add the data to the queue

    def recognize_speech_from_mic(self):
        with sd.RawInputStream(samplerate=self.samplerate,
                blocksize = 8000, device=self.device, dtype='int16',
                channels=1, callback=self.callback):

            #create an instance of the kaldi recognizer
            #create a dictionary for transcribed words
            #create a variable to store if we reached a full sentence
            
            #while we do not have a full sentence
                #get data from the queue
                #if the waveform is accepted by kaldi
                    #set transcribed to the kaldi result
                    #set full sentence to true
                #else
                    #trancribed is set to the partial result
            
            #call the parse_result function and save the result to transcribed_text
            return transcribed_text
    
    def parse_result(self, transcribed):
        #load the transcribed parameter into a JSON object
        #return the transcribed text

if __name__ == '__main__':
    #create the speech detection object
    try:
        while True:
            #save the transcribed text by calling recognize_speech_from_mic()
            print(transcribed_text)
    except KeyboardInterrupt:
        print('\nDone')
    except Exception as e:
        print(e)

