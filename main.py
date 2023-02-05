import pandas as pd
import os

if not os.path.exists("Kişiler.xlsx"):
    df = pd.DataFrame(columns=["İsim","Soyisim"])
    df.to_excel("Kişiler.xlsx", index=False)

df = pd.read_excel("Kişiler.xlsx")

while True:
    secim = input("add, clear yada exit yazınız: ")

    if secim.lower() == "add":
        isim = input("İsim: ")
        soyisim = input("Soyisim: ")

        isim = isim.capitalize()
        soyisim = soyisim.capitalize()

        df = pd.concat([df, pd.DataFrame({"İsim" : [isim], "Soyisim" : [soyisim]})], ignore_index=True)

        df.to_excel("Kişiler.xlsx", index=False)
    elif secim.lower() == "clear":
        df = pd.DataFrame(columns=["İsim", "Soyisim"])
        df.to_excel("Kişiler.xlsx", index=False)
    elif secim.lower() == "exit":
        break
    else:
        print("Geçersiz seçim")