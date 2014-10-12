#!/usr/bin/python
import urllib2
import RPi.GPIO as GPIO

URL="www.dwd.de/dyn/app/ws/html/reports/HHX_warning_de.html" # Hamburg

LEDS = {"red":14,"green":15}

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for color in LEDS:
        GPIO.setup(LEDS[color],GPIO.OUT)


def displayWarnLevel(isWarning):
    for led in LEDS:
        GPIO.output(LEDS[led],GPIO.LOW)
    color = "red" if isWarning else "green"
    GPIO.output(LEDS[color],GPIO.HIGH)


def getWarnLevel():
    response = urllib2.urlopen(URL)
    html = response.read()
    return "ws_warning_content" in html

init()
isWarning = getWarnLevel()
displayWarnLevel(isWarning)
