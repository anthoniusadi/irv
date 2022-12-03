import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

x = np.arange(-2, 2, 0.01)
y = np.array(x**2+2*np.sin(x*np.pi)) 
y = y + np.array(np.random.random(len(x))*2.3)

plt.figure(figsize=(12, 9))

plt.plot(x, y, label="y_signal")
plt.legend()
plt.grid(True)
plt.show()
signal.fftconvolve
y_smooth = signal.savgol_filter(y, window_length=11, polyorder=3, mode="nearest")
    
plt.figure(figsize=(12, 9))
plt.plot(x, y, label="y_signal")
plt.plot(x, y_smooth, linewidth=3, label="y_smoothed")
plt.legend()
plt.grid(True)
plt.show()


ig, ax = plt.subplots(4, figsize=(8, 14))
i = 0

# define window sizes 5, 11, 21, 31
for w_size in [ 5,7,9,11]:    
    
    y_fit = signal.savgol_filter(y, w_size, 3, mode="nearest")
    ax[i].plot(x, y, label="y_signal", color="blue")
    ax[i].plot(x, y_fit, label="y_smoothed", color="red")
    ax[i].set_title("Window size: " + str(w_size))
    ax[i].legend()
    ax[i].grid(True)
    i+=1
    print(y_fit.shape,len(x),len(y))

plt.tight_layout()        
plt.show()