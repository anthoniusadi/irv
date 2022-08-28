import time
import numpy as np
from mods.cleaning import clean
from mods.preprocess import preprocessing
start = time.time()
# import mods 
# from mods.cleaning import cleaning
# from mods.preorocess import convert_wav
import matplotlib.pyplot as plt
file_name = 'tes11 8khz 12 bit gain dibawah 0 suara orang'
# 
txt = file_name+'.txt'

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

file_convert = preprocessing(values,name=file_name+'(40000)',fr=16000)
# mods.preprocessing.convert_wav(values,name=file_name+'(40000)',fr=40000)
file_convert.convert_wav()
hasil_stft = file_convert.stft(file_name+'(40000).wav',sr=35000)
print(f'waktu eksekusi : {time.time()-start} s')
