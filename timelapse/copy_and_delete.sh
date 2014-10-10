#!/bin/bash

# Kopiert alle Fotos, die älter als eine Minute sind auf einen storage-Rechner und löscht sie vom PI

find ./photos/ -name "*.jpg" -type f -mmin +1 -exec scp {} photos@storage:timelapse \; -exec rm {} \;
