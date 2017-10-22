import sensor_and_data.time_data
from time import sleep
import picamera

def update_timestamp():
    stamp = sensor_and_data.time_data.get_timestamp()
    return stamp
    

def elapsed_time():
    elapsed_time = sensor_and_data.time_data.get_time()[1]
    return elapsed_time #gets elapsed time from time_data module


def take_picture(n):
    mode = ['auto', 'sunlight', 'horizon'] #change to only 'auto' and 'horizon'
    for i in range(len(mode)):
        with picamera.PiCamera() as camera:
            camera.vflip = 1
            camera.hflip = 1
            camera.resolution = (3280, 2464)
            camera.awb_mode = mode[i]
            camera.start_preview(alpha = 180)
            camera.annotate_text = 'Project 250 Stevens High School AP Physics 2' #omit
            sleep(2)
            filename = 'images/' + str(n) + '_' + str(i) + '.jpeg'
            camera.capture(filename)
            camera.stop_preview()
            sleep(2)
            

def take_video(n):
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.awb_mode = 'auto'
        camera.vflip = 1
        camera.hflip = 1
        
        camera.start_preview(alpha = 180)
        camera.start_recording(r'video/' + str(n) + '.h264')

        camera.wait_recording(300)
    
        camera.stop_recording()
        camera.stop_preview()

    
def capture(runtimeInHours):
    runtimeInSec = runtimeInHours * 3600
    n = 0
    
    while elapsed_time() < runtimeInSec: #loop until runTime is met
        take_video(n)
        sleep(1)
        take_picture(n)
        sleep(1)
        n += 1
