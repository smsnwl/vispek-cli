
from subprocess import call
import sys
import time

if __name__ == '__main__':
    text_file = open("seq.txt", "r")
    lines = text_file.read().split(',')
    act = []
    for k in lines:
        act.append(int(k))


    for c in act:
        ts = round(time.time())
        for i in range(1,9):
            call('fswebcam -d /dev/video%d cam%d.jpg -q'%(i*2,i*2), shell=True)
            call('cp cam%d.jpg %d-cam%d.jpg'%((i*2),ts,(i*2)), shell=True)
            call('touch %d-nir.dat'%ts, shell=True)
        call(['ssh', 'pi@192.168.0.112', '/home/pi/conveyor/enqueue.py', '1','%d'%c])
        call(['curl', 'http://192.168.0.110:8080/hello'])
