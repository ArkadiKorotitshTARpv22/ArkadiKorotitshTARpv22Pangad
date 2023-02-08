from omamodulepanga import *

palgad=[]
inimesed=[]

while True:
    print(inimesed)
    print(palgad)
    menu=int(input("Valik:\n1-Lisa andmed \n2-Kustuta andmed\n3-Suurim palk\n4-Vaiksem palk\n5-Soorteerimine\n"))
    if menu==0:
        break
    elif menu==1:
        inimised,palgad=Lisa_andmed(inimesed,palgad)
    elif menu==2:
        inimesed,palgad=kustutamine(inimesed,palgad)
    elif menu==3:
        palk,nimi=Suurim_palk(inimesed,palgad)
        print(f"Suurim palk on {palk} {nimi}´l")
    elif menu==4:
        palk,nimi=Vaiksem_palk(inimesed,palgad)
        print(f"Vaiksem palk on {palk} {nimi}´l")
    elif menu==5:
        inimesed,palgad=Sorteerimine(inimesed,palgad)
         
