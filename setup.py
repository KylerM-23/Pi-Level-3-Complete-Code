import os, sys

print("Enter y in the terminal whenever 'After this operation...' appears.")

os.system("cd /usr/bin && sudo rm python && sudo ln -s python3 python")

failed = []

modules = {
    "Libport Audio": "sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev",
    "Pyaudio Method 1": "sudo apt-get install python-pyaudio",
    "Pyaudio Method 2": "sudo apt-get install python3-pyaudio",
    "Pyaudio Pip Method": "sudo pip3 install pyaudio",
    "Espeak" : "sudo apt install espeak",
    "Pyttsx3": "sudo pip3 install pyttsx3",
    "Matplotlib Pip Method": "sudo pip3 install matplotlib",
    "Matplotlib Method 1": "sudo apt install python-matplotlib",
    "Matplotlib Method 2": "sudo apt install python3-matplotlib",
    "Vosk": "sudo pip3 install vosk",
    "Sounddevice": "sudo pip3 install sounddevice",
    "Numpy": "sudo pip3 install numpy"
    }

def update():
    print("Updating")
    os.system("sudo apt-get update")
    os.system("sudo apt-get upgrade")

def audio(i = 0):
    if (i == 2):
        print("Pyaudio failed to import.")
        failed+=["Libport Audio", "Pyaudio Method 1", "Pyaudio Method 2", "Pyaudio Pip Method"]
        return
    try:
        import pyaudio
    except:
        print("Installing libraries for pyaudio.")
        os.system("sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev")
        os.system("sudo apt-get install python-pyaudio")
        os.system("sudo apt-get install python3-pyaudio")
        os.system("sudo pip3 install pyaudio")
        audio(i+1)
 
def speech_synth(i = 0):
    if (i == 2):
        print("Pyttsx3 failed to import.")
        failed+=["Espeak", "Pyttsx3"]
        return
    try:
        import pyttsx3
    except:
        print("Installing libraries for pyttsx3.")
        os.system("sudo apt install espeak")
        os.system("sudo pip3 install pyttsx3")
        speech_synth(i+1)
        
def graph(i = 0):
    if (i == 2):
        print("Matplotlib failed to import.")
        failed+=["Matplotlib Pip Method", "Matplotlib Method 1","Matplotlib Method 2", "Numpy"]
        return
    try:
        import matplotlib
    except:
        print("Installing libraries for pyttsx3.")
        os.system("sudo pip3 install matplotlib")
        os.system("sudo apt install python-matplotlib")
        os.system("sudo apt install python3-matplotlib")
        os.system("sudo pip3 install numpy")
        graph(i+1)

def speech_rec(i = 0):
    if (i == 2):
        print("Pyttsx3 failed to import.")
        failed+=["Vosk", "Sounddevice"]
        return
    try:
        import vosk
        import sounddevice as sd
    except:
        print("Installing libraries for pyttsx3.")
        os.system("sudo pip3 install vosk")
        os.system("sudo pip3 install sounddevice")
        speech_rec(i+1)
        
def main():
    update()
    print("Module Test")
    audio()
    speech_synth()
    graph()
    speech_rec()
    if len(failed) > 0:
        print("These modules failed, try running the associated command in the terminal or use the Thonny Package Manager.")
        for mod in failed:
            print(mod, modules[mod])
    else:
        print("Module Test Success")
        
main()