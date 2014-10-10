#!/bin/bash
avconv -threads 2 -f image2 -r 25 -i %06d.jpg -vcodec libx264 time-lapse.mp4
