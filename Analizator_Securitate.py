from importlib.resources import as_file
import re
from collections import Counter

def analiza_loguri(cale_fisier):
    print(f"Incepem analiza :{cale_fisier} \n ")
    ip_suspect=[]
    regex_ip=r'[0-9]+(?:\.[0-9]+){3}'

    try:
      with open(cale_fisier,'r') as fisier:
          cautare_fisier=fisier.readlines()

          for linie in cautare_fisier:
              if "Failed password" in linie:
                  ip_gasit=re.findall(regex_ip,linie)

                  if ip_gasit:
                      ip_suspect.append(ip_gasit[0])

             
          numaratoare_ip = Counter(ip_suspect)

          print("____RAPORT DE SECURITATE: ATACURI BRUTE-FORCE___\n")
          print(f"Total încercări eșuate: {len(ip_suspect)} \n")
          print("Top IP-uri atacatoare:\n")

          for ip, numar_incercari in numaratoare_ip.most_common(3):
            print(f"IP -  {ip}  Incercari: {numar_incercari} \n" )

    except FileNotFoundError:
        print("Eroare.Verificati calea sau numele ")



#analiza_loguri('test_auth.log')
