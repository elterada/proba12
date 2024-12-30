import numpy as np
import matplotlib.pyplot as plt

n = int(input("n = "))

s = np.zeros(n)
s[0] = 0
stop_loss = -2

for i in range(1, n):
    y = np.random.choice([-1, 1])
    s[i] = s[i-1] + y

plt.plot(s)
plt.show()




