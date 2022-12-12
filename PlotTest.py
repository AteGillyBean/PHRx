import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
from scipy.signal import find_peaks
import numpy as np
logfile = '/home/pi/Downloads/log.txt'

fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(7,1)

times = []
accels = []
xaccels = []
yaccels =[]
zaccels = []
irs = []
xgyros=[]
ygyros=[]
zgyros=[]
def readlog(filename, times, xaccels, yaccels, zaccels, irs, xgyros, ygyros, zgyros):
    with open(filename, 'r') as f:
        content = f.read()
    
    content = content.split('\n')[:-1]
    for line in content:
        split = line.split('_')
        time = split[0][:10]
        time=float(time)
#         print(time)
        accel = split[1]
        ir=split[2]
        gyro=split[3]
        x_accel = float(accel.split(',')[0][1:])
        y_accel = float(accel.split(',')[1][1:])
        z_accel = float(accel.split(',')[2][1:-1])
        ir = float(ir)
        x_gyro = float(gyro.split(',')[0][1:])
        y_gyro = float(gyro.split(',')[1][1:])
        z_gyro = float(gyro.split(',')[2][1:-1])

        if time not in times:
            
            times.append(time)
            xaccels.append(x_accel)
            yaccels.append(y_accel)
            zaccels.append(z_accel)
            irs.append(ir)
            xgyros.append(x_gyro)
            ygyros.append(y_gyro)
            zgyros.append(z_gyro)
            data=[xaccels, yaccels, zaccels, irs, xgyros, ygyros, zgyros]
            
readlog(logfile, times, xaccels, yaccels, zaccels, irs, xgyros, ygyros, zgyros)
data=[xaccels, yaccels, zaccels, irs, xgyros, ygyros, zgyros]
def animate(i, times, data):
    readlog(logfile, times, xaccels, yaccels, zaccels, irs, xgyros, ygyros, zgyros)
    
    times = times[-180:]
    xaccels2 = data[0]
    yaccels2 = data[1]
    zaccels2 = data[2]
    irs2 = data[3]
    xgyros2 = data[4]
    ygyros2 = data[5]
    zgyros2 = data[6]
    xaccels2 = xaccels2[-180:]
    yaccels2 = yaccels2[-180:]
    zaccels2 = zaccels2[-180:]
    irs2 = irs2[-180:]
    xgyros2 = xgyros2[-180:]
    ygyros2 = ygyros2[-180:]
    zgyros2 = zgyros2[-180:]
    peaks = find_peaks(irs2,prominence=300)
#     print(peaks)
    peaks = peaks[0][-5:]
#     print(peaks)
#     print(times[peaks[1]])
    if len(peaks)>=5:
        delta_t1=times[peaks[4]]-times[peaks[3]]
        delta_t2=times[peaks[3]]-times[peaks[2]]
        delta_t3=times[peaks[2]]-times[peaks[1]]
        delta_t4=times[peaks[1]]-times[peaks[0]]
        avg=(delta_t1+delta_t2+delta_t3+delta_t4)/4
        bpm=60/avg
        bpm="%.0f" % bpm
        with open('/home/pi/Downloads/avg.txt', 'w') as a:
            a.write(str(bpm))
    else:
        with open('/home/pi/Downloads/avg.txt', 'w') as a:
            a.write("Please Cover PPG LED")
    ax1.clear()
    ax1.plot(times, xaccels2)
    ax1.set_ylabel("X Accelerations")
    ax1.set_ylim(-15,15)
    ax2.clear()
    ax2.plot(times, yaccels2)
    ax2.set_ylabel("Y Accelerations")
    ax2.set_ylim(-15,15)
    ax3.clear()
    ax3.plot(times, zaccels2)
    ax3.set_ylabel("Z Accelerations")
    ax3.set_ylim(-15,15)
    ax4.clear()
    ax4.plot(times, irs2)
#     ax4.plot(times[peaks[0]],irs2[peaks[0]],"x")
    ax4.set_ylabel("IR Value")
    ax5.clear()
    ax5.plot(times, xgyros2)
    ax5.set_ylabel("X Gyroscope")
    ax5.set_ylim(-5,5)
    ax6.clear()
    ax6.plot(times, ygyros2)
    ax6.set_ylabel("Y Gyroscope")
    ax6.set_ylim(-5,5)
    ax7.clear()
    ax7.plot(times, zgyros2)
    ax7.set_ylabel("Z Gyroscope")
    ax7.set_ylim(-5,5)


ani = animation.FuncAnimation(fig, animate, fargs=(times, data), interval = 1)
plt.show()

def main():
    try:
        ani = animation.FuncAnimation(fig, animate, fargs=(times, data), interval = 1)
        plt.show()
    finally:
        plt.close()
        
if __name__=='__main__':
    main()
