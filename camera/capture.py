#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from picamera import PiCamera
from datetime import datetime

camera = PiCamera()

camera.capture('/home/pi/Pictures/billede_{0}.jpg'.format(datetime.utcnow().replace(microsecond=0).isoformat()))
