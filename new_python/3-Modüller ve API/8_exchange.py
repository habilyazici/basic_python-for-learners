import requests
import json

access_key = "7eb06b60e5377d9969de9c75a2c47bdc" 
# apilayer.com

bozulan_doviz = input("bozulan döviz türü: ").upper()
alinan_doviz = input("alınan döviz türü: ").upper()
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))

url = f"https://api.exchangeratesapi.io/v1/latest?access_key={access_key}"

response = requests.get(url)
print("HTTP Durum Kodu:", response.status_code)
result = response.json()
print(type(result))
# print("JSON Veri:", result)

bozulan_doviz2 = result["rates"][bozulan_doviz]
alinan_doviz2 = result["rates"][alinan_doviz]
döviz_tutari = alinan_doviz2 / bozulan_doviz2

print(f"{miktar} {bozulan_doviz} = {miktar * döviz_tutari} {alinan_doviz}")