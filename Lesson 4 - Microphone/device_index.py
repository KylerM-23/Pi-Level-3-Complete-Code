import pyaudio

p = pyaudio.PyAudio() #pyaudio object

for device in range (p.get_device_count()):
    print("Index", device, ":", p.get_device_info_by_index(device).get('name'))

    
    