from picamera import PiCamera

camera = PiCamera()

try:
    camera.start_preview(fullscreen = False, window = (25,25,640,480))
    while True:
        continue

except KeyboardInterrupt:
    camera.stop_preview()