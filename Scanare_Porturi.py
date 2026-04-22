import socket
import concurrent.futures
import time



def scanare_porturi(ip,port):
    try:
       s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       s.settimeout(1)
       rezultat = s.connect_ex((ip, port))

       if rezultat==0:
           print(f"Portul {port} este deschis ")

       s.close()

    except:
        pass


def pornire_scanare():
    tinta="scanme.nmap.org"
    print(f"\nScanare tinta:{tinta}")
    timp_start=time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
       for port in range(1, 1025):
          executor.submit(scanare_porturi, tinta, port)

    timp_final = time.time() - timp_start
    print(f"\nScanare finalizata in: {timp_final:.2f} secunde")