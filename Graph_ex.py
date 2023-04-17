# Graph with pygame
import math
import pygame
from adafruit_rplidar import RPLidar

# Set up pygame and the display
resolution_x = 1000
resolution_y = 1000
scan_data = [0]*360
pygame.init()
display = pygame.display.set_mode((resolution_x, resolution_y))
pygame.mouse.set_visible(False)
display.fill((0, 0, 0))
pygame.display.update()

# Setup the RPLidar
PORT_NAME = 'COM3'
lidar = RPLidar(None, PORT_NAME, timeout=2)

# Scale data to fit on the screen
max_dist = 100
min_dist = 15
scale = 1  # Trasnform 1 cm to 1 pixel


def process_data(data):
    global max_distance
    display.fill((0, 0, 0))
    for angle in range(360):
        distance = data[angle]
        if distance > 0:                  # ignore initially ungathered data points
            if distance > max_dist or distance < min_dist:
                pass
            radians = math.radians(angle)  # angle * pi / 180.0
            # Parametric equation r(cos(angle)+sin(angle))
            x = distance * math.cos(radians)
            y = distance * math.sin(radians)
            point = (resolution_x//2 + int(x*scale),
                     resolution_y//2 + int(y*scale))
            display.set_at(point, pygame.Color(255, 255, 255))
    pygame.display.update()


try:
    for scan in lidar.iter_scans():
        for (_, angle, distance) in scan:
            scan_data[min([359, math.floor(angle)])] = distance / 10
        process_data(scan_data)

except KeyboardInterrupt:
    print('Stoping.')
lidar.stop()
lidar.disconnect()
