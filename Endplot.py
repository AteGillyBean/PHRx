import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
from scipy.signal import find_peaks
import numpy as np
from array import *
filename = '/home/pi/Downloads/log.txt'

fig, (ax5, ax6, ax7, ax4, ax1, ax2, ax3) = plt.subplots(7,1)

times = []
accels = []
xaccels = []
yaccels =[]
zaccels = []
xgyros=[]
ygyros=[]
zgyros=[]
irs = []

with open('/home/pi/Documents/Accelerometer Tests/Roll/data.txt', 'w') as f:
        pass

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
    with open('/home/pi/Documents/Accelerometer Tests/Roll/data.txt', 'a') as f:
        f.write(str(time) + ',' + str(x_accel) + ',' + str(y_accel) + ',' + str(z_accel) + ',' + str(ir) + '\n')
    if time not in times:
        
        times.append(time)
        xaccels.append(x_accel)
        yaccels.append(y_accel)
        zaccels.append(z_accel)
        irs.append(ir)
        xgyros.append(x_gyro)
        ygyros.append(y_gyro)
        zgyros.append(z_gyro)

peaks=find_peaks(irs,prominence=300)
peak_vals=[]
peak_times=[]
xmove_times=[]
xmove_vals=[]
xmove_times1=[]
xmove_vals1=[]
ymove_times=[]
ymove_vals=[]
ymove_times1=[]
ymove_vals1=[]
zmove_times=[]
zmove_vals=[]
zmove_times1=[]
zmove_vals1=[]
for element in peaks[0]:
    peak_time = times[element]
    peak_val = irs[element]
    peak_times.append(peak_time)
    peak_vals.append(peak_val)
# for i, item in enumerate(xaccels):
#     if xaccels[i]<=-1.2 and xaccels[i-4]>-1.2:
#         xmove_times.append(times[i])
#         xmove_vals.append(xaccels[i])
#     elif xaccels[i]>=1 and xaccels[i-4]<1:
#         xmove_times1.append(times[i])
#         xmove_vals1.append(xaccels[i])
#     else:
#         pass
for i, item in enumerate(xgyros):
    if xgyros[i]<=-0.1 and xgyros[i-1]>-0.1:
        xmove_times.append(times[i])
        xmove_vals.append(xgyros[i])
    elif xgyros[i]>=0.1 and xgyros[i-1]<0.1:
        xmove_times1.append(times[i])
        xmove_vals1.append(xgyros[i])
    else:
        pass
for i, item in enumerate(ygyros):
    if ygyros[i]<=-0.17 and ygyros[i-1]>-0.17:
        ymove_times.append(times[i])
        ymove_vals.append(ygyros[i])
    elif ygyros[i]>=0.17 and ygyros[i-1]<0.17:
        ymove_times1.append(times[i])
        ymove_vals1.append(ygyros[i])
    else:
        pass
for i, item in enumerate(zgyros):
    if zgyros[i]<=-0.1 and zgyros[i-1]>-0.1:
        zmove_times.append(times[i])
        zmove_vals.append(zgyros[i])
    elif zgyros[i]>=0.1 and zgyros[i-1]<0.1:
        zmove_times1.append(times[i])
        zmove_vals1.append(zgyros[i])
    else:
        pass
# for i, item in enumerate(zaccels):
#     if zaccels[i]<=3 and zaccels[i-4]>3:
#         if times[i-100:i] not in zmove_times[-100:i]:
#             zmove_times.append(times[i])
#             zmove_vals.append(zaccels[i])
# #             print(times[i-100:i])
#     elif zaccels[i]>=3.6 and zaccels[i-4]<3.6:
#         zmove_times1.append(times[i])
#         zmove_vals1.append(zaccels[i])
#     else:
#         pass
# print(peak_times)
# print(len(peak_vals))
# print(peak_vals)
# print(type(new_peaks))
# n=len(peaks)
# print(new_peaks)

ax1.plot(times,xaccels)
ax1.set_ylabel("X Accelerations")
ax1.set_ylim(-15,15)
ax2.plot(times, yaccels)
ax2.set_ylabel("Y Accelerations")
ax2.set_ylim(-15,15)
ax3.plot(times, zaccels)
ax3.set_ylabel("Z Accelerations")
ax3.set_ylim(-15,15)
ax4.plot(times, irs)
ax4.set_ylabel("IR Value")
ax4.plot(peak_times, peak_vals,"x")
ax4.set_ylim(110000)
ax5.plot(times, xgyros)
ax5.set_ylabel("x Gyroscope")
ax5.plot(xmove_times, xmove_vals,"x",color="black",label="+ Pitch")
ax5.plot(xmove_times1, xmove_vals1,"x", color="yellow",label="- Pitch")
ax5.legend()
ax5.set_ylim(-5,5)
ax6.plot(times, ygyros)
ax6.set_ylabel("y Gyroscope")
ax6.plot(ymove_times, ymove_vals,"x", color="orange", label="+ Yaw")
ax6.plot(ymove_times1, ymove_vals1,"x", color="red", label="- Yaw")
ax6.legend()
ax6.set_ylim(-5,5)
ax7.plot(times, zgyros)
ax7.set_ylabel("z Gyroscope")
ax7.plot(zmove_times, zmove_vals,"x", color="green",label="- Roll")
ax7.plot(zmove_times1, zmove_vals1,"x", color="purple",label="+ Roll")
ax7.legend()
ax7.set_ylim(-5,5)
plt.show()