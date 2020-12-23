#!/usr/bin/env python3
#Written by Colin Twigg, Recognition Designs Ltd, 2020

import anki_vector
import time
import json
import os
from decimal import Decimal, ROUND_DOWN, ROUND_UP

pause = 0.5

os.system('scp root@192.168.0.100:/data/data/com.anki.victor/persistent/jdocs/vic.RobotLifetimeStats.json vic.RobotLifetimeStats.json')

os.system('scp root@192.168.0.100:/data/data/com.anki.victor/persistent/jdocs/vic.RobotSettings.json vic.RobotSettings.json')

with open('vic.RobotSettings.json') as g:
    robotStats = json.load(g)
    
    z = (robotStats['jdoc']['default_location'])
    flag = str((z) + ' flag')
    print(flag)
    print("You are located in {}".format(z))

with open('vic.RobotLifetimeStats.json') as f:
    robotStats = json.load(f)
    
    a = (robotStats['jdoc']['Odom.Body'])
    cms = a / 1000000
    miles = (cms / 160934)
    print("I have driven {:0.2f} miles".format(miles))
    
    b = (robotStats['jdoc']['Pet.ms'])
    seconds = b // 1000
    print("You have petted me for {} seconds".format(seconds))
    
    c = (robotStats['jdoc']['Alive.seconds'])
    days = (c // 3600)//24
    print("I have been alive for {} days".format(days))
    
with anki_vector.Robot() as robot:
    robot.behavior.say_text("Tap my back to hear my stats".format(miles))
    while True:
        if robot.touch.last_sensor_reading.is_being_touched:
            robot.behavior.say_text("I have driven {:0.2f} miles".format(miles))
            time.sleep(pause)
            robot.behavior.say_text("You have petted me for {} seconds".format(seconds))
            time.sleep(pause)
            robot.behavior.say_text("I have been alive for {} days".format(days))
            time.sleep(pause)
            robot.behavior.say_text("I live in {} with my owner".format(z))
            break
