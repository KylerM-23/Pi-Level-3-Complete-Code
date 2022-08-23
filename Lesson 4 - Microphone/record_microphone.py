import pyaudio, wave

chunk = 2**12 # 2^12 samples for buffer
sampling_rate = 44100 #44.1kHz
audio_format = pyaudio.paInt16 #16 bit resolution
dev_index = 3 # device index for the mic

def recordMic(output_filename, duration):
    audio = pyaudio.PyAudio() # create pyaudio instantiation

    # create pyaudio stream
    #16 bit resolution, 44.1=kHz sampling, mono audio, input, with 2^12 samples in buffer
    stream = audio.open(format = audio_format,rate = sampling_rate,channels = 1,
                        input_device_index = dev_index,input = True, 
                        frames_per_buffer= chunk)

    print("recording")
    frames = []

    # loop through stream and append audio chunks to frame array
    for frame in range(0,int((sampling_rate/chunk)*duration)):
        data = stream.read(chunk, exception_on_overflow = False)
        frames.append(data)

    print("finished recording")

    # stop the stream, close it, and terminate the pyaudio instantiation
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # save the audio frames as .wav file
    wavefile = wave.open(output_filename,'wb')
    wavefile.setnchannels(1)
    wavefile.setsampwidth(audio.get_sample_size(audio_format))
    wavefile.setframerate(sampling_rate)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()

if __name__ == '__main__':
    recordingName = input("Enter the name of your file ")+'.wav' # name of recording
    recordingLen = int(input("How long do you want the recording to be? ")) # seconds to record
    recordMic(recordingName, recordingLen)
