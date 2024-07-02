# Script-pour-voir-la-charge-du-CPU
Visualisé après un instant T le pourcentage du CPU et le journaliser

# création du fichier script et log
touch /home/ec2-user/cpu/scriptCpu.sh
touch /home/ec2-user/cpu/scriptLog.log

# insertion script dans scriptCpu.sh
nano /home/ec2-user/cpu/scriptCpu.sh

#!/bin/bash

while true; do
    # Récupère la charge CPU
    cpu_load=$(uptime | awk '{print $10}')

    # Affiche la charge CPU
    echo "Charge CPU : $cpu_load"

    # Attends 1 seconde avant de répéter
    sleep 1
done

# creation du cron
crontab -e

*/1 * * * *  /home/ec2-user/cpu/scriptCpu.sh >> /home/ec2-user/cpu/scriptLog.log

