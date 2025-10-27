# %%
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)
f1 = np.exp(-np.sin(2*np.pi*x))
f2 = np.exp(-np.cos(2*np.pi*x))
plt.subplots(nrows=2, ncols=1, sharex=True)
plt.subplot(211)
plt.plot(x, f1)
plt.grid(True)

plt.subplot(212)
plt.plot(x, f2)
plt.grid(True)
plt.show()
# %%
