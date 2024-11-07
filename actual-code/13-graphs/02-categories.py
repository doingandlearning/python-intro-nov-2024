# Install through PyCharm:
# - pandas
# - numpy
# - matplotlib
# Without PyCharm it's `pip install pandas numpy matplotlib`

import matplotlib.pyplot as plt

x = ["Italy", "Switzerland", "France", "Netherlands", "Poland"]

y = [16.2, 6.5, 12.2, 10.1, 7.5]

plt.bar(x,y, color="red")
plt.grid()

plt.title("A plot showing the square numbers to 10")
plt.xlabel("x values")
plt.ylabel("x^2")
plt.show()