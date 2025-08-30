import pandas as pd
import numpy as np

personeller = {
    'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Departman': ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Yaş': [30,25,45,50,23,34,42],
    'Semt': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş': [5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(personeller)
print("personeller:\n", df)
print("Maaş toplamı:", df["Maaş"].sum())
print("\n" + 20 * '-' + "\n")

print("Departman grupları bellek yeri:\n", df.groupby("Departman"))
print("Departman grupları:\n", df.groupby("Departman").groups)
print("\n" + 20 * '-' + "\n")

# Her benzersiz ("Departman", "Semt") kombinasyonu için bir grup oluşturur.
print("Departman ve Semt grupları:\n", df.groupby(["Departman","Semt"]).groups)
print("\n" + 20 * '-' + "\n")

print("Semt grupları:\n", df.groupby("Semt").groups)
print("\n" + 20 * '-' + "\n")

for name, group in df.groupby("Departman"):
    print("adı:", name)
    print("grup:\n", group)
    print()
print("\n" + 20 * '-' + "\n")

print("Muhasebe departmanındaki çalışanlar:")
print(df.groupby("Departman").get_group("Muhasebe"))
print("\n" + 20 * '-' + "\n")

print("Her departmanın toplanmış değerleri:")
print(df.groupby("Departman").sum())
print("\n" + 20 * '-' + "\n")

print("Her departmanın ortalama yaşı:")
print(df.groupby("Departman")["Yaş"].mean())
print("\n" + 20 * '-' + "\n")

print("Her departmanın toplam maaşı:")
result = df.groupby("Departman")
print(result["Maaş"].sum())
print("\n" + 20 * '-' + "\n")

print("Her semtin ortalama maaşı:")
print(df.groupby("Semt")["Maaş"].mean())
print("\n" + 20 * '-' + "\n")

print("Her semtteki çalışan sayısı:")
print(df.groupby("Semt")["Çalışan"].count())
print("\n" + 20 * '-' + "\n")

print("Her departmanın en büyük yaşı:")
print(df.groupby("Departman")["Yaş"].max())
print("\n" + 20 * '-' + "\n")

print("Her departmanın en yüksek maaşı:")
print(df.groupby("Departman")["Maaş"].max())
print("\n" + 20 * '-' + "\n")

print("Muhasebe departmanının en yüksek maaşı:")
print(df.groupby("Departman")["Maaş"].max()["Muhasebe"])
print("\n" + 20 * '-' + "\n")

# her depertmana ait sayısal sutunların ortalaması 
# print(df.groupby("Departman").agg(np.mean))

print("departmanların maaş istatistikleri:")
print(df.groupby("Departman")["Maaş"].agg(["sum", "mean", "max", "min"]))
print("\n" + 20 * '-' + "\n")

print("muhasebe departmanının maaş istatistikleri:")
print(df.groupby("Departman")["Maaş"].agg(["sum", "mean", "max", "min"]).loc["Muhasebe"])