
"""
Dataset Generation using Carla PythonAPI
- Generates a dataset with Point Cloud (LiDAR), Image (Camera) and GNSS()
- Groundtruth: bouding box 3D of the EGO vehicle and opponents

"""

import os
import sys
import argparse
import numpy as np

# add carla library to system path to import
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                "../simulator/carla/PythonAPI/carla/dist/carla-0.9.6-py3.5-linux-x86_64.egg"))

import carla
import random
import time


INTERVAL = 0.3  # Arbitrary

client = carla.Client('localhost', 2000)
client.set_timeout(2.0)


world = client.get_world()

blueprint_library = world.get_blueprint_library()

bp_ego = random.choice(blueprint_library.filter('vehicle.tesla.*'))
transform = random.choice(world.get_map().get_spawn_points())
vehicle_ego = world.spawn_actor(bp_ego, transform)


# set clear 
weather = world.get_weather()
weather.cloudyness = 0
weather.precipitation = 0
weather.precipitation_deposits = 0
weather.wind_intensity = 0
weather.sun_azimuth_angle = 30
weather.sun_altitude_angle = 100
world.set_weather(weather)


# Let's get a RGB camera and set some attributes
camera_bp = blueprint_library.find('sensor.camera.rgb')
camera_transform = carla.Transform(carla.Location(x=1.5, z=2.4))
camera_bp.set_attribute('image_size_x', '800')
camera_bp.set_attribute('image_size_y', '600')
camera_bp.set_attribute('sensor_tick', str(INTERVAL))

# Spawn the camera and attach it to the vehicle
camera = world.spawn_actor(
    camera_bp,
    camera_transform,
    attach_to=vehicle_ego
)


# Let's also add a GNSS sensor
gnss_bp = blueprint_library.find('sensor.other.gnss')
gnss_transform = carla.Transform(carla.Location(x=1.5, z=2.4))
gnss = world.spawn_actor(
    gnss_bp,
    gnss_transform,
    attach_to=vehicle_ego
)

lidar_bp = blueprint_library.find('sensor.lidar.ray_cast')
lidar_transform = carla.Transform(carla.Location(x=1.5, z=2.4))
lidar_bp.set_attribute('sensor_tick', str(INTERVAL))


# Check how much "out" folders already exists
n_output = len([d for d in os.listdir() if d.startswith('out')])


camera.listen(lambda image: image.save_to_disk(
    'out%02d/%06d' % (n_output, image.frame_number)
))


gnss.listen(
    lambda data: print(
        'timestamp {:0.3f},'
        ' latitude {:0.3f},'
        ' longitude {:0.3f},'
        ' altitude {:0.3f}'.format(
            data.timestamp, data.latitude,
            data.longitude, data.altitude)
        )
)

lidar = world.spawn_actor(
    lidar_bp,
    lidar_transform,
    attach_to=vehicle_ego
)

def save_lidar_to_disk(data):
    print('lidar', data)
    data.save_to_disk('out%02d/%06d' % (n_output, data.frame_number))

lidar.listen(
    lambda  data: save_lidar_to_disk(data)
)


# Driving right and left some times
for _ in range(20):
    vehicle_ego.apply_control(
        carla.VehicleControl(throttle=5.0, steer=0.1)
    )
    time.sleep(0.5)

    vehicle_ego.apply_control(
        carla.VehicleControl(throttle=5.0, steer=-0.1)
    )
    time.sleep(0.5)
