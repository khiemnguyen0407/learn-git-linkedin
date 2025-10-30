# %%
import numpy as np
import matplotlib.pyplot as plt
f = lambda x: np.exp(-np.sin(x))

x = np.linspace(0, 2*np.pi, 100)
plt.plot(x, f(x))
plt.grid(True)
plt.show()
# %%
