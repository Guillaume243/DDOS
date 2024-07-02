Z#!/bin/bash

while true; do
    # Récupère la charge CPU
    cpu_load=$(uptime | awk '{print $10}')

    # Affiche la charge CPU
    echo "Charge CPU : $cpu_load"

    # Attends 1 seconde avant de répéter
    sleep 1
done
