import RPi.GPIO as GPIO
import time
from picamera import PiCamera
import random

camera = PiCamera()
buttons = [6,13,19,26]
ledPin = 21

picture_path = "picture/"
video_path = "video/"

picture = 0
video = 0

capturing = False
recording = False

filter_on = False
filters = ['negative', 'sketch', 'oilpaint','pastel', 'film', 'blur']

def setup():
    GPIO.setmode(GPIO.BCM)         # use BCM Numbering
    GPIO.setup(buttons, GPIO.IN)   # set the button to INPUT mode
    GPIO.setup(ledPin, GPIO.OUT)   # set the ledPin to OUTPUT mod
    GPIO.output(ledPin, GPIO.LOW)
    
    GPIO.add_event_detect(buttons[0], GPIO.RISING, callback=start_recording, bouncetime=200)
    GPIO.add_event_detect(buttons[1], GPIO.RISING, callback=stop_recording, bouncetime=200)
    GPIO.add_event_detect(buttons[2], GPIO.RISING, callback=take_picture, bouncetime=200)
    GPIO.add_event_detect(buttons[3], GPIO.RISING, callback=toggle_filter, bouncetime=200)
    
    camera.resolution = (500, 500)
    camera.framerate = 15
    camera.start_preview(fullscreen=False, window = (50, 50, 250, 250))

def take_picture(channel):
    global picture, capturing
    
    if not capturing:
        capturing = True
        time.sleep(2)
        camera.capture(picture_path + str(picture) + '.jpeg')
        picture += 1
        print("Picture saved.")
        capturing = False

def start_recording(channel):
    global recording, video
    
    if not recording:
        recording = True
        camera.start_recording(video_path + str(video)+".h264")
        video += 1
        GPIO.output(ledPin, GPIO.HIGH)

def stop_recording(channel):
    global recording
    
    if recording:
        recording = False
        camera.stop_recording()
        GPIO.output(ledPin, GPIO.LOW)
        print("Video saved.")

def toggle_filter(channel):
    global filter_on
    
    if not filter_on:
        filter_on = True
        camera.image_effect = random.choice(filters)
    else:
        filter_on = False
        camera.image_effect = 'none'

def destroy():
    if recording:
        camera.stop_recording()
    camera.stop_preview()
    GPIO.cleanup()                      # Release all GPIO
 
if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        while(True):
            continue
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()
