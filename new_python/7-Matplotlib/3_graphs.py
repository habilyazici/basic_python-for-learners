import matplotlib.pyplot as plt
import pandas as pd

# Stack Plot
data = {
    "yil": [2011, 2012, 2013, 2014, 2015],
    "oyuncu1": [8, 10, 12, 7, 9],
    "oyuncu2": [7, 12, 5, 15, 21],
    "oyuncu3": [18, 20, 22, 25, 19]
}

df = pd.DataFrame(data)

# bunları label verebilmek için yazdık
plt.plot([],[],color="y",label="oyuncu1")
plt.plot([],[],color="r",label="oyuncu2")
plt.plot([],[],color="b",label="oyuncu3")

plt.stackplot(df["yil"], df["oyuncu1"], df["oyuncu2"], df["oyuncu3"], colors=["y","r","b"])
plt.title("Yıllara göre atılan goller")
plt.xlabel("yil")
plt.ylabel("Gol Sayısı")
plt.legend()
plt.show()



# Pie Grafiği
goal_types = 'Penaltı','Kaleye Atılan Şut','Serbest Vuruş'

goals = [12,35,7]
colors = ['y','r','b']

plt.pie(goals, labels=goal_types, colors=colors, shadow=True, explode=(0.05,0.05,0.05), autopct="%1.1f%%")
plt.show()


# Bar Grafiği
plt.bar([0.25,1.25,2.25,3.25,4.25], [50,40,70,80,20], label="BMW", width=.5, edgecolor='black')
plt.bar([0.75,1.75,2.75,3.75,4.75], [80,20,20,50,60], label="Audi", width=.5, edgecolor='black')
plt.title("Araç Bilgileri", fontsize=14)
plt.xlabel("Gün")
plt.ylabel("Mesafe (km)")
plt.legend()
plt.grid(True)
plt.show()


# Histogram 
yaslar = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(yaslar, yas_gruplari, histtype="bar", rwidth=0.8, edgecolor='black')
plt.title("Histogram Grafiği")
plt.xlabel("yaş grupları")
plt.ylabel("Kişi Sayısı")
plt.grid(True)
plt.ylabel("Kişi Sayısı")
plt.show()