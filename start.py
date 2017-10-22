from sensor_and_data.sensor_data import get_data
from sensor_and_data.time_data import get_time
from time import sleep
import os

def setup():

    print('preparing files...')
    
    f = open('start_time.txt', 'w')
    f.write('')
    f.flush() #prepare starttime file (.txt) file
    os.fsync(f.fileno())
    f.close()
    
    print('files created') #temp


def report_data():
    sens_data = get_data()
    data = get_time()
    for n in sens_data:
        data.append(n)
    return(data)


def record_data(hours):
    sec = hours * 3600
    n = 0
    elapsed_time = get_time()[1]

    #data is taken in separate files and compiled later to avoid data loss
    #on shutdown. The pi doesn't like to write things to its harddisk.
    while elapsed_time < sec:
        f = open(r'data/' + str(n) + '.txt', 'w') #take data
        for data in report_data():
            f.write(str(data) + ',')
        f.flush()
        os.fsync(f.fileno())
        f.close()
        n += 1
        sleep(60)
