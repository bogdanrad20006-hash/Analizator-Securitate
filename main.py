import Analizator_Securitate
import Scanare_Porturi
import monitorizare_server

def afiseaza_meniu():
    while True:
        print("\n" + "="*45)
        print("   TOOLKIT DE SECURITATE ȘI DEVOPS")
        print("="*45)
        print("[1] Analizează log-urile de securitate")
        print("[2] Verifică starea serverului (Disk, OS)")
        print("[3] Scanare porturi ")
        print("[4] Ieșire")
        print("="*45)
        
        optiune = input("Alege o opțiune (1/2/3/4): ")
        
        if optiune == '1':
            Analizator_Securitate.analiza_loguri('test_auth.log')

        elif optiune == '2':
            monitorizare_server.verificare_stare_server()

        elif optiune == '3':
            Scanare_Porturi.pornire_scanare()

        elif optiune == '4':
            Scanare_Porturi.pornire_scanare
            
        else:
            print("\n Eroare: Opțiune invalidă. Te rog să alegi 1, 2 sau 3.")
            break

afiseaza_meniu()