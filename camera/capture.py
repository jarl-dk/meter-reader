#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from picamera import PiCamera
from datetime import datetime

camera = PiCamera()

camera.sharpness = 100
camera.rotation = 180
camera.zoom = (0.0, 0.0, 1.0, 1.0)
camera.resolution = (1280, 720)
camera.capture('/home/pi/Pictures/billede_{0}.jpg'.format(datetime.utcnow().replace(microsecond=0).isoformat()))
