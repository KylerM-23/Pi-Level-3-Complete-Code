import pyaudio
import wave

chunk = 2**12

file_name = 

audio_file = 
audio = pyaudio.PyAudio()

#fill in the settings for the audio stream
stream = audio.open(
    format = audio,
    channels=audio_file,
    rate=audio_file,
    output=)

print("Now playing", file_name)

#read from buffer

#while there is data to read
    #write the audio daya to the stream
    #read a new set of data

#close all your files

print(file_name, "has been closed")
