# konversi binary raw data audio dan plotting
# save plotting sesuai nama path_file
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
import os
import plotly.graph_objects as go
from scipy.fft import fft, fftfreq
import pandas as pd
from scipy import fftpack

def stft_au(file_raw,sr=16000):
        n_fft=1024
        # fig, ax = plt.subplots()
        # y, _ = librosa.load(file_name)
        stft = np.abs(librosa.stft(file_raw, n_fft=n_fft))
        librosa.display.specshow(stft, x_axis='time', y_axis='log', sr=sr)
        print(sr)
        plt.savefig("acc_STFT.png")
        # plt.show()
        return y
def stft_acc(file_raw,sr=600):
        n_fft=1024
        # fig, ax = plt.subplots()
        # y, _ = librosa.load(file_name)
        stft = np.abs(librosa.stft(file_raw, n_fft=n_fft))
        librosa.display.specshow(stft, x_axis='time', y_axis='log', sr=sr)
        print(sr)
        plt.savefig("acc_STFT.png")
        # plt.show()
        return y

def acc_fft(sgn, fs=400):
    N = sgn.shape[0]
    T = 1.0 / fs
    x = np.linspace(0, N*T, N)
    y = sgn
    tmp = fft(sgn)    
    # f_s = fs
    power = ((np.abs(tmp) ) / N  )  # type: ignore
    # xtime = np.linspace(0, 1 / (2.0*T), N)
    xtime = fftpack.fftfreq(len(sgn)) * fs
    fig, ax = plt.subplots()
    plt.title('acc')
    ax.set_xlim(0, fs / 2)
    ax.plot(xtime,power)
    plt.show()
def au_fft(sgn, fs=8000):
    N = sgn.shape[0]
    T = 1.0 / fs
    # print(T)
    x = np.linspace(0, N*T, N)
    y = sgn
    tmp = fft(sgn)    
    # f_s = fs
    power = ((np.abs(tmp) ) / N  )   # type: ignore
    # xtime = np.linspace(0, 1 / (2.0*T), N)
    xtime = fftpack.fftfreq(len(sgn)) * fs
    print(xtime)
    fig, ax = plt.subplots()
    plt.title('au')
    ax.set_xlim(0, fs / 2)
    ax.plot(xtime,power)
    plt.show()

def scaling(x,xmax,xmin):
    x_new = np.float64(((2/xmax)*x) + xmin)
    return x_new

folder = 'data/ega/'
for path_file in os.listdir(folder):
    
# path_file = '/home/epiphany/dev_irv/irv/data/3 detik/acc#2022_11_13#12_9_9#-777616#11035985#920'
    name_file = path_file
    file_out= open(f"{folder+path_file}.txt", "w",encoding="latin-1")
    f = open(f"{folder+path_file}", "rb")
    byte = f.read(2)
    y = []
    
    nameFile = path_file.split(sep='_')
    timestamp = nameFile[1]
    date_time = datetime.fromtimestamp(int(timestamp))
    tgl = f'{date_time.year}_{date_time.month}_{date_time.day}'
    waktu = f'{date_time.hour}_{date_time.minute}_{date_time.second}'
    fname = f'{nameFile[0]}#{name_file[1]}#{tgl}#{waktu}#{nameFile[2]}#{nameFile[3]}#{nameFile[4]}'
    
    while byte:
        if 'au' in name_file:
            pass
            # print('audio')
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
    print(f'max value : {max(y)} filename_value : {nameFile[4]}')
    y[-1]=y[-2]
    x = np.arange(len(y))
    del y
    # plt.title("plotting")
    # plt.xlabel('samples')
    # plt.ylabel('amplitudes')
    # plt.plot(x, y)  
    # acc_fft(np.array(y) )
    # plt.savefig(f'out_data_pengukuran/{name_file}.png')
    # plt.show()
