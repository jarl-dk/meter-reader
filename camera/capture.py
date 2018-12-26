#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from picamera import PiCamera

camera = PiCamera()

camera.capture('/home/pi/Pictures/billed1.jpg')
