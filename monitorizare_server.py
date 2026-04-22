import platform
import shutil

 
def verificare_stare_server():

    print("\n___STATUS SERVER___")

    sistem = platform.system()
    versiune=platform.version()

    print(f"\nSistem de operare: {sistem}\nVersiune: {versiune}")
    
    if sistem=="Windows" :
        partitie="C:\\"
    else:
         partitie="/"

    total,folosit,liber =shutil.disk_usage(partitie)

    gb_total=total/1024**3
    gb_liber=liber/1024**3
    gb_folosit = folosit / 1024**3

    print(f"\nValora GB total: {gb_total:.2f}\nValoare GB liber: {gb_liber:.2f}\nValoare GB folosit: {gb_folosit:.2f}")

    if gb_liber<10.0 :
       print("\nSTARE ALERTA - spatiu critic sub 10GB ")
    else:
       print("STARE OK - totul funcționează perfect, spațiu suficient")

#verificare_stare_server()    