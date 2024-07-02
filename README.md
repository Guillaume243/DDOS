# Attack DDOS
Visualisé après un instant T le pourcentage du CPU et le journaliser pour le EC2_1, et lancer le script d'attaque de l'EC2_2  vers EC2_1

# création du fichier script et  pour le EC2_1
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

# voir le CPU en tant réél
tail -f /home/ec2-user/cpu/scriptCpu.sh

--------------------------------------------------------------------------------------------

# creation du fichier SODD.py dans lequel se trouve un script d'une attaque DDOS dans EC2_2
lancer l'attaque avec:
python /home/ec2-user/attaque/SODD.py

