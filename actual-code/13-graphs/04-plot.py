import matplotlib.pyplot as plt
import numpy as np

print(plt.style.available)
plt.style.use("seaborn-v0_8-paper")

x = np.linspace(0,10,100)
y = 1 + 3 * np.sin(2*x)

x1 = np.linspace(0,10, 25)
y1 = 1 + 3 * np.sin(2*x1)
fig, ax =plt.subplots()

ax.plot(x,y)
ax.plot(x1,y1)

plt.show()