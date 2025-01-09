import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1500, 1100, 1200, 1800]
plt.plot(x, y)
plt.show()

legend = ['January', 'February', 'March', 'April']
plt.xticks(x, legend)

plt.plot(x, y)
plt.show()

plt.bar(x, y)
plt.ylabel('Sales in US$')
plt.title('monthly Sales')
plt.show()