import pandas as pd
import os

if not os.path.exists("Kişiler.xlsx"):
    df = pd.DataFrame(columns=["İsim","Soyisim","Yaş"])
    df.to_excel("Kişiler.xlsx", index=False)

df = pd.read_excel("Kişiler.xlsx")

while True:
    print('Excele isim eklemek için "add" exceli temizlemek için "clear" programdan çıkış yapmak istiyorsanız "exit" yazınız :')
    secim = input("Ne yapmak istersiniz lütfen seçiniz: ")
inp
    if secim.lower() == "add":
        isim = input("İsim: ")
        soyisim = input("Soyisim: ")
        yas = input("Yaş: ")

        isim = isim.capitalize()
        soyisim = soyisim.capitalize()

        df = pd.concat([df, pd.DataFrame({"İsim" : [isim], "Soyisim" : [soyisim], "Yaş" : [yas]})], ignore_index=True)

        df.to_excel("Kişiler.xlsx", index=False)
    elif secim.lower() == "clear":
        df = pd.DataFrame(columns=["İsim", "Soyisim","Yaş"])
        df.to_excel("Kişiler.xlsx", index=False)
    elif secim.lower() == "exit":
        break
    else:
        print("Geçersiz seçim lütfen tekrar seçiniz")