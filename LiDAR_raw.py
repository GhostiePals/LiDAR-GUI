# Get the list of data from the LiDAR
import os
from math import floor
from adafruit_rplidar import RPLidar


# Setup the RPLidar
PORT_NAME = 'COM3'
lidar = RPLidar(None, PORT_NAME, timeout=2)
scan_data = [0]*360


def process_data(data):
    print_data(data)
    for x in range(len(data)):
        pass


def print_data(data):
    print(data)
    print("----" + "Number of list: ", len(data))
    print("----" + "0 Grados ", data[360-1])
    print("----" + "90 Grados ", data[90-1])
    print("----" + "180 Grados ", data[180-1])
    print("----" + "270 Grados ", data[270-1])


try:
    for scan in lidar.iter_scans():
        for (_, angle, distance) in scan:
            scan_data[min([359, floor(angle)])] = distance / 10
        process_data(scan_data)

except KeyboardInterrupt:
    print('Stopping.')
lidar.stop()
lidar.disconnect()
