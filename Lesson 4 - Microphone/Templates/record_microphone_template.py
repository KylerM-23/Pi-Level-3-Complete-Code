import pyaudio
import wave

chunk = # 2^12 samples for buffer
sampling_rate = #44.1kHz
audio_format =  #16 bit resolution
dev_index = # device index for the mic

output_filename = input("Enter the name of your file ")+'.wav' # name of recording
record_secs = int(input("How long do you want the recording to be? ")) # seconds to record

# create pyaudio instantiation

# create pyaudio stream with
#16 bit resolution, 44.1=kHz sampling, mono audio, input = true, with 2^12 samples in buffer


print("recording")
frames = []

for frame in range(0,int((sampling_rate/chunk)*record_secs)):
    #read from the stream
    #add to the frame list

print("finished recording")

#stop sampling data
#close the stream
#stop the pyaudio instance

wavefile = #open the file
wavefile.# set the channels
wavefile.#set the audio format
wavefile.#set the sampling rate
wavefile.#write the frame data
wavefile.#close the file


