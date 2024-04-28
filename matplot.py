import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title('Simple Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
y3 = [3, 6, 9, 12, 15]
plt.plot(x, y1, label='Line 1')
plt.plot(x, y2, label='Line 2')
plt.plot(x, y3, label='Line 3')
plt.title('Multiple Lines Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.show()
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y, marker='*', color='red', label='Data Points')
plt.title('Customized Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.show()
