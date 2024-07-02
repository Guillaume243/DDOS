import socket
import time
import threading

def canal(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connecter le socket au serveur
    server_addr = ('54.160.225.253', port)
    sock.connect(server_addr)
    print(f"Connexion au port {port}")

    # Envoyer une requête au serveur
    request = b'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n'
    sock.sendall(request)

    # Recevoir la réponse du serveur avec une latence de 50 millisecondes
    reponse = b''
    while True:
        data = sock.recv(1024)
        if not data:
            break
        time.sleep(0.05)  # 50 millisecondes
        reponse += data
    print(reponse.decode())
    sock.close()

# Liste des ports à ouvrir
ports_to_open = [80, 443, 22, 21]

# Créer des threads pour chaque port à ouvrir
threads = []
for port in ports_to_open:
    t = threading.Thread(target=canal, args=(port,))
    t.start()
    threads.append(t)

# Attendre que tous les threads se terminent
for t in threads:
    t.join()