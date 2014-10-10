#!/bin/bash
cd photos
raspistill -o %06d.jpg -w 1920 -h 1080 -tl 5000 -t 720000000
