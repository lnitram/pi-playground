Zeitraffer mit Raspberry-Pi-Cam


timelapse.sh
```
#!/bin/bash

# Nutzt raspistill, um alle 5 Sekunden ein Foto in 
# Full-HD-Auflösung (1920x1080) zu machen und im 
# Ordner ./photos zu speichern

cd photos
raspistill -o %06d.jpg -w 1920 -h 1080 -tl 10000 -t 720000000
```


generate_timelapse.sh
```
#!/bin/bash

# Setzt die von timelapse.sh generierten Fotos zu einem Full-HD-Video 
# mit 25 Frames / Sekunde zusammen

avconv -threads 2 -f image2 -r 25 -i %06d.jpg -vcodec libx264 time-lapse.mp4
```
