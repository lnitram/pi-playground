Zeitraffer mit Raspberry-Pi-Cam


```
#!/bin/bash
cd photos
raspistill -o %06d.jpg -w 1920 -h 1080 -tl 10000 -t 720000000
```
