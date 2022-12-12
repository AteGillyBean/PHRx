from __future__ import print_function
import sys
import time
import board
import busio
import qwiic_max3010x
import qwiic_i2c.circuitpy_i2c
import qwiic_i2c.i2c_driver
import qwiic_i2c.__init__
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX
# print(qwiic_i2c.isDeviceConnected(0x6b))

filename = '/home/pi/Downloads/log.txt'            
i2c = board.I2C()
sensor = LSM6DSOX(i2c)
sensor2 = qwiic_max3010x.QwiicMax3010x()

ledBrightness = 0x1F
sampleAverage = 8
ledMode = 3
sampleRate = 3200
pulseWidth = 411
adcRange = 4096
with open('/home/pi/Downloads/start.txt', 'r') as q:
    start_time = q.read()
    start_time=float(start_time)
sensor2.setup(ledBrightness, sampleAverage, ledMode, sampleRate, pulseWidth, adcRange)



while True:
    time_since_start = time.time() - start_time
    accel = sensor.acceleration
    gyro = sensor.gyro
    ir = sensor2.getIR()
    with open(filename, 'a') as f:
        f.write(str("%.3f" % time_since_start) + '_' + str(accel) + '_' + str("%.3f" % ir) + '_' + str(gyro) + '\n')
    
#     time.sleep(0.01)

