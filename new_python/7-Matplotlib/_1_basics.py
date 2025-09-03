import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# örnek1
x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x, y, color="red", marker="o", markersize=8, linestyle="--", linewidth=2, label="Veri")
plt.axis([0,6,0,20])

font1 = {'family':'serif','color':'blue','size':20}
plt.title("Grafik Başlığı", fontdict = font1)
plt.xlabel("x label")
plt.ylabel("y label")
plt.show() 


# örnek2
x = np.linspace(0,2,100)

plt.plot(x, x, label="linear",color="red")
plt.plot(x, x**2, label="quadratic",color="yellow")
plt.plot(x, x**3, label="cubic",color="green")

plt.title("simple plot")
plt.xlabel("x label")
plt.ylabel("y label")

plt.legend()
plt.show() 


# örnek3
x = np.linspace(0,2,100)
fig, axs =  plt.subplots(nrows=1, ncols=3)
# Hep bir tane figür çıkıyor 3 tane de grafik çıkıyor. 
# Bir satırda 3 tane veya tam tersini yapabilirdik
fig.suptitle("grafik başlığı")

axs[0].plot(x, x, color="red")
axs[0].set_title("linear")

axs[1].plot(x, x**2, color="green")
axs[1].set_title("quadratic")

axs[2].plot(x, x**3, color="yellow")
axs[2].set_title("cubic")

plt.tight_layout()
plt.show() 


# örnek4
x = np.linspace(0,2,100)
fig,axs =  plt.subplots(2,2)
fig.suptitle("grafik başlığı")

axs[0,0].plot(x, x, color="red")
axs[0,1].plot(x, x**2, color="blue")

axs[1,0].plot(x, x**3, color="green")
axs[1,1].plot(x, x**4, color="yellow")
plt.show()


# örnek5
df = pd.read_csv("nba.csv")

df = df.drop(["Number"], axis = 1).groupby("Team").mean(numeric_only=True)
print(df.sample(5))

df.sample(5).plot(subplots=True)
plt.legend()
plt.show() 