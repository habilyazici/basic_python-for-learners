import matplotlib.pyplot as plt
import numpy as np
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

x = np.linspace(-10,9,20)
y = x ** 3
z = x ** 2
figure = plt.figure(figsize=(8, 6))
# figüre işimize lazım diye oluşturduk, otomatik oluşmaktadır

axes_cube = figure.add_axes([0.1,0.1,0.8,0.8])
# sol, alt, genişlik, yükseklik
axes_cube.plot(x, y, color='blue', label='Cube')
axes_cube.set_title("Cube")
axes_cube.set_xlabel("X Axis")
axes_cube.set_ylabel("Y Axis")
axes_cube.legend(loc=4)

axes_square = figure.add_axes([0.15,0.6,0.25,0.25])
axes_square.plot(x, z, color="yellow", label='Square')
axes_square.set_title("Square")
axes_square.set_xlabel("X Axis")
axes_square.set_ylabel("Y Axis")
axes_square.legend(loc=4)

figure.savefig("figure2.pdf")

plt.show()