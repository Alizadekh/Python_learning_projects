import time

print(
      """
******************************************
*     AYKHAN BANK MUSTERI XIDMETLERI      *
******************************************
      """
"""
Xahis edirik xitmet novunu secin...
"""
"""
1) Kart balansi

2) Pul kocurmeleri (card-to-card / cash-to-card) 

3) Vesait yatirimi

4) Pul cekimi

***SISTEMDEN CIXMAQ UCUN a-ya BASIN...***
*****************************************
"""
)

sys_card_number="123456789"
sys_security_key="1234"
sys_card_balance=1000
sys_accepted_card2="987654321"
sys_security_key2="4321"
sys_card2_balance=500
while True:
    entered_card_number= input("Kart nomrenizi daxil edin: ")
    entered_security_key= input("Tehlukesizlik kodunu daxil edin: ")
    print("Melumatlariniz analiz edilir...")
    time.sleep(1)
    if entered_card_number=="a":
        print("Sistemden cixilir...")
    if sys_card_number==entered_card_number and sys_security_key==entered_security_key:
        print(" {} nomreli kart tanimlanmisdir! ".format(entered_card_number))
    else:
        print("Yanlis kart nomresi ve ya parol...!")
        continue
    while True:
        xidmet_novu= input("Emeliyyat novunu secin: ")
        if xidmet_novu=="a":
            print("Tesekkurler, hesabinizdan cixilir...")
            break
        if xidmet_novu=="1":
            print("Kartinizin hazirki balansi: {} AZN".format(sys_card_balance))
            continue
        elif xidmet_novu=="2":
            print(
                """               
                            1) CARD-TO-CARD
            Kocurme novleri:   
                            2) CASH-TO-CARD
                """
            )
            kocurme_novu=input("Kocurme novunu seciniz: ")
            if kocurme_novu=="1":
                accepted_card= input("Qebul edecek karti daxil edin: ")
                if accepted_card==sys_accepted_card2:
                    kocurme_meblegi= float(input("Kocurme meblegini yazin: "))
                    if kocurme_meblegi>sys_card_balance:
                        print("Kartda kifayet qeder balans yoxdur!")
                        continue
                    else:
                        sys_card_balance=sys_card_balance-kocurme_meblegi
                        print("{} nomreli karta {} AZN kocuruldu.".format(accepted_card,kocurme_meblegi))
                        continue
                else:
                    print("Daxil etdiyiniz kart nomresi yanlisdir...")
                    continue
            elif kocurme_novu=="2":
                accepted_card= input("Qebul edecek karti daxil edin: ")
                if accepted_card==sys_accepted_card2:
                    kocurme_meblegi= float(input("Meblegi terminala daxil edin: "))
                    if kocurme_meblegi>sys_card_balance:
                        print("Kartda kifayət qədər balans yoxdur!")
                    else:
                        sys_card_balance = sys_card_balance - kocurme_meblegi
                        print("{} nomreli karta {} AZN elave edildi.".format(accepted_card,kocurme_meblegi))
                        continue
        elif xidmet_novu=="3":
            yatirim_meblegi=float(input("Yatiracaginiz meblegi yazin: "))
            sys_card_balance=sys_card_balance+yatirim_meblegi
            print(
                """
            Balansiniza {} AZN elave edildi.
            Hazirki balansiniz {} AZN-dir.
            
                """
            .format(yatirim_meblegi,sys_card_balance))
            print("Cixmaq ucun a-ya basin!")
            continue
        while True:
            if xidmet_novu=="4":
                cekim_meblegi=float(input("Ne qeder mebleg cixarmaq isteyirsiz? "))
                if cekim_meblegi>sys_card_balance:
                    print("Yeterli balans yoxdur!")
                else:
                    sys_card_balance=sys_card_balance-cekim_meblegi
                    print(
                    """
                    Kartinizdan {} AZN cixilmisdir.
                    Kartinizin hazirki balansi: {} AZN
                    """
                    .format(cekim_meblegi,sys_card_balance))
                    break









12