Zeitraffer mit Raspberry-Pi-Cam


timelapse.sh

Nimmt alle 5 Sekunden ein Foto mit "raspistill" auf und speichert es im Ordner photos


copy_and_delete.sh

Da die Speicherkarte im Raspberry PI nicht unendlich groß ist, müssen die Fotos bei längeren Sessions woanders gespeichert werden. Dieses Script kopiert alle Fotos, die älter als eine Minute sind, per SSH auf einen storage-Rechner und löscht sie anschließend vom PI. So kann man wieder Platz schaffen.


generate_timelapse.sh

Setzt die von timelapse.sh erzeugten Fotos zu einem Video zusammen


