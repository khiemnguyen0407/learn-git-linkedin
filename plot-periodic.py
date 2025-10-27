# %%
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 256)
f = np.exp(-np.sin(x) + np.cos(2*x))
plt.plot(x, f)
plt.grid(True)
plt.show()
# %%
