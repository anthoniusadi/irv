import os
import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
from scipy.fft import fft, fftfreq
import pandas as pd
from scipy import fftpack
import json
import filter 

def scaling(x,xmax,xmin):
    x_new = np.float64(((2/xmax)*x) + xmin)
    return x_new

def stft(file_wav,sr=400):
    pass
    
def au_fft(sgn, fs=8000):
    N = sgn.shape[0]
    T = 1.0 / fs
    x = np.linspace(0, N*T, N)
    y = sgn
    tmp = fft(sgn)    
    power = ((np.abs(tmp) ) / N  )   # type: ignore
    # xtime = np.linspace(0, 1 / (2.0*T), N)
    xtime = fftpack.fftfreq(len(sgn)) * fs
    # print(xtime)
    # fig, ax = plt.subplots()
    # plt.title('au')
    # ax.set_xlim(0, fs / 2)
    # ax.plot(xtime,power)
    # plt.show()
    
def acc_fft(sgn, fs=400):
    N = sgn.shape[0]
    T = 1.0 / fs
    x = np.linspace(0, N*T, N)
    y = sgn
    tmp = fft(sgn)    
    power = ((np.abs(tmp) ) / N  )  # type: ignore
    xtime = fftpack.fftfreq(len(sgn)) * fs
    power[0]= 0
    fig, ax = plt.subplots()
    plt.title('acc')
    ax.set_xlim(0, fs / 2)
    ax.plot(np.arange(len(y)),power,label = 'freq',color='blue')
    
    # plt.savefig(f'cnth.png')
    plt.show()
    return power
    
def encode(folder,path_file):
    name_file = path_file
    file_out= open(f"{folder+path_file}.txt", "w",encoding="latin-1")
    f = open(f"{folder+path_file}", "rb")
    byte = f.read(2)

    y = []
    while byte:
        byte = f.read(2)
        data_y = int.from_bytes(byte, "big", signed=True) 
        if 'au' in name_file:
            print('audio')    
        # scaling ini pakai untuk audio
            tmp = scaling(data_y,xmax=4095 ,xmin=-1) 
            y.append(tmp)
            # au_fft(np.array(y) )
        else:
            # acc
            y.append(data_y/100)
            # acc_fft(np.array(y))

    y[-1]=y[-2]
    # pow = acc_fft(np.array(y) )
    # file_out.write(str(y))
    x = np.arange(len(y))
    plt.title("plotting")
    plt.xlabel('samples')
    plt.ylabel('amplitudes')
    plt.plot(x, y)  
    # plt.savefig(f'{folder+name_file}.png')
    plt.show()
    return np.array(y),x,y

path_folder = './data/temp_data/2022_11_15/acc/'

# fitur fft
# for i in os.listdir(path_folder):
#     enc,_,_ = encode(path_folder,i)
#     f_fft = acc_fft(enc)
#     with open(f"{path_folder+'fft_'+i}.txt", 'w') as filehandle:
#         for i in f_fft:
#             filehandle.write(f'{str(i)+" "}')


# fitur stft
# for i in os.listdir(path_folder):
#     # fitur stft
#     enc,_,_ = encode(path_folder,i)
#     f_stft = stft(enc)

# filter sg
for i in os.listdir(path_folder):
    enc,x,y = encode(path_folder,i)
    filt = filter.sg_filter(enc,window_length=15,orde=3)
    # filter.show(x,enc)
    acc_fft(filt)
    

