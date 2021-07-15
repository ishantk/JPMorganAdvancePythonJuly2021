"""
    Matplotlib
    Also Explore -> https://seaborn.pydata.org/
"""
import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
# plt.plot(x)
# plt.show()

y1 = [n for n in x]
y2 = [n*n for n in x]
y3 = [n*n*n for n in x]

plt.plot(x, y1, '*', label='linear')
plt.plot(x, y2, '^', label='square')
plt.plot(x, y3, 'D', label='cube')
# plt.axis([-1, 5, -1, 10]) # apply limits
# plt.xlim(-1, 5)
# plt.ylim(-1, 10)

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.title("Polynomial Graphs")

plt.grid(True)

plt.legend()

plt.savefig("PolynomialGraph.png")

plt.show()
