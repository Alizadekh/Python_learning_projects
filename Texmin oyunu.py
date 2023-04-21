import time
import random
print("""
********************************

            TEXMIN OYUNU

1 VE 48 ARASINDA BIR REQEM TEXMIN EDIN
****************************""")
texmin_haqqi = 7
texmini_sayi = random.randint(1,40)

while True:
    texmin =int(input("Texmininiz:"))

    if (texmin == texmini_sayi):
        print("Eded sorğulanır....")
        time.sleep(1)
        print("Tebrikler!")
        print("Eded",rastgele_sayı)
        break
    elif(texmin < texmini_sayi):
        print("Eded sorğulanır....")
        time.sleep(1)
        texmin_haqqi -= 1
        print("Daha yuksek bir eded deyin.")
        print("Texmin haqqi:",texmin_haqqi)
    else:
        print("Eded sorğulanır....")
        time.sleep(1)
        texmin_haqqi -= 1
        print("Daha aşağı bir eded deyin.")
        print("Texmin haqqi:",texmin_haqqi)
    if (texmin_haqqi == 0 ):
        print("Tessuf, texmin haqqiniz bitti")
        print("Ededimiz: ",texmini_sayi)
        break

