import pyaudio
import wave

chunk = 2**12

file_name = input("What file do you want to play? ") + ".wav" 

audio_file = wave.open(file_name, 'rb')
audio = pyaudio.PyAudio()

stream = audio.open(
    format = audio.get_format_from_width(audio_file.getsampwidth()),
    channels=audio_file.getnchannels(),
    rate=audio_file.getframerate(),
    output=True)

print("Now playing", file_name)

data = audio_file.readframes(chunk) #read from buffer

while len(data) > 0: #while there is data to read
    stream.write(data)
    data = audio_file.readframes(chunk) #save frames

stream.stop_stream()
stream.close()
audio.terminate()
audio_file.close()

print(file_name, "has been closed")
