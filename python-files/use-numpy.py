# %%
import numpy as np
import matplotlib.pyplot as plt
N = 2**8
a, b = 0, 1
dx = (b - a) / N
x = np.arange(a, b, dx)
f = np.exp(-np.sin(2 * np.pi * x))
plt.subplots(nrows=2, ncols=1, sharex=True)
plt.subplot(211)
plt.plot(x, f)
plt.grid()
plt.show()
# %%
xi = np.concat((np.arange(0, N//2), np.array([0]), np.arange(-N//2+1, 0))) * (2 * np.pi) / (b - a)
df_fft = np.fft.ifft(1j * xi * np.fft.fft(f)).real
df = -2*np.pi*np.cos(2 *np.pi * x) * f
plt.subplot(212)
plt.plot(x, df, 'r-', linewidth=1)
plt.plot(x, df_fft, 'k--', linewidth=3)
plt.grid(True)
# %%
