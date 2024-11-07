# Install through PyCharm:
# - pandas
# - numpy
# - matplotlib
# Without PyCharm it's `pip install pandas numpy matplotlib`

import matplotlib.pyplot as plt

data = [1,4,4,7,4,7,8,4,3,2,5,6,4,5,7,5,3,4]

plt.hist(data, bins=4)
plt.grid()

plt.title("A plot showing the square numbers to 10")
plt.xlabel("x values")
plt.ylabel("x^2")
plt.show()