import time
import numpy as np
from mods.cleaning import clean
from mods.preprocess import preprocessing
from scipy import signal

start = time.time()
# import mods 
# from mods.cleaning import cleaning
# from mods.preorocess import convert_wav
import matplotlib.pyplot as plt
file_name = 'tes12 8kHz 10 bit'
# 
txt = file_name+'.txt'
def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype = "high", analog = False)
    return b, a

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y
def plot(x,y,name):
    plt.plot(x,y)
    plt.xlabel('Sampling')
    plt.ylabel('Value')
    plt.title('Plot Data')
    plt.legend()
    plt.savefig(name)
    plt.show()

file_cleaning = clean(txt)
values = file_cleaning.cleaning()
print(len(values))
data_x = np.arange(len(values))
plot(data_x,values,name=file_name+'(40000)')

file_convert = preprocessing(values,name=file_name+'(40000)',fr=4000.0)
# mods.preprocessing.convert_wav(values,name=file_name+'(40000)',fr=40000)
file_convert.convert_wav()
hasil_stft = file_convert.stft(file_name+'(40000).wav',sr=4000)

# fitering

print(f'waktu eksekusi : {time.time()-start} s')
