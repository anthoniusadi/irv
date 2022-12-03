import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
def sg_filter(sgn,window_length=5,orde=3):
    y_smooth_value = signal.savgol_filter(sgn, window_length=window_length, polyorder=orde, mode="nearest")
    return y_smooth_value

def show(x,sgn):
    ig, ax = plt.subplots(4, figsize=(8, 14))
    i = 0
    # define window sizes 5, 11, 21, 31
    for w_size in [ 5,7,9,11]:    
        y_fit = signal.savgol_filter(sgn, w_size, 3, mode="nearest")
        ax[i].plot(x, sgn, label="y_signal", color="blue")
        ax[i].plot(x, y_fit, label="y_smoothed", color="red")
        ax[i].set_title("Window size: " + str(w_size))
        ax[i].legend()
        ax[i].grid(True)
        i+=1

    plt.tight_layout()        
    plt.show()