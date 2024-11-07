# Install through PyCharm:
# - pandas
# - numpy
# - matplotlib
# Without PyCharm it's `pip install pandas numpy matplotlib`

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7,8,9,10]
y = [1, 4, 9, 16, 25,36,49,64,81,100]

plt.scatter(x,y)

plt.title("A plot showing the square numbers to 10")
plt.xlabel("x values")
plt.ylabel("x^2")
plt.show()