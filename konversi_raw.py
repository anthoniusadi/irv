# konversi binary raw data audio dan plotting
# save plotting sesuai nama path_file

import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display

import plotly.graph_objects as go

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
from scipy.fft import fft, fftfreq
import pandas as pd
from scipy import fftpack

def convert(f):
    time=[]
    for i in range(len(f)):
        time.append(i*0.00252)
    data = {'time':time,'acc':f}
    df = pd.DataFrame(data)
    return df

def fig_from_df(df):
    fig = go.Figure()
    for col in df.columns:
      fig.add_trace(go.Scatter(x=df.index,y=df[col],name=col))
    return fig
def acc_fft(sgn, fs=400):
    N = sgn.shape[0]
    T = 1.0 / fs
    # print(T)
    x = np.linspace(0, N*T, N)
    y = sgn
    tmp = fft(sgn)    
    # f_s = fs
    
    power = ((np.abs(tmp) ) / N  )  # type: ignore
    # xtime = np.linspace(0, 1 / (2.0*T), N)
    xtime = fftpack.fftfreq(len(sgn)) * fs
    
    # print(xtime)
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
def get_fft_acc(df):
    N=len(df)
    
    fs = len(df)/(df.index[-1]-df.index[0])
    print(f'fs : {fs}')
    
    x_plot= fftfreq(N, 1/8000)[:N//2]
    
    df_fft = pd.DataFrame()
    df_phase = pd.DataFrame()
    for name in df.columns:
        yf = fft(df[name].values) 
        y_plot= 2.0/N * np.abs(yf[0:(N//2)])  # type: ignore
        
        '''
        phase = np.unwrap(2 * np.angle(yf)) / 2 * 180/np.pi
        df_phase = pd.concat([df_phase,
                            pd.DataFrame({'Frequency (Hz)':x_plot[1:],
                                          name:phase[1:n]}).set_index('Frequency (Hz)')],axis=1)
        '''
        df_fft = pd.concat([df_fft,
                            pd.DataFrame({'Frequency (Hz)':x_plot[1:],
                                          name:y_plot[1:]}).set_index('Frequency (Hz)')],axis=1)
    return df_fft

def scaling(x,xmax,xmin):
    x_new = np.float64(((2/xmax)*x) + xmin)
    return x_new
# path_file = '/home/epiphany/dev_irv/irv/Data Pengukuran/au_1668572486_3568204_13976852_1221'
path_file = '/home/epiphany/dev_irv/irv/data/3 detik/acc#2022_11_13#12_9_9#-777616#11035985#920'
# 
name_file = path_file[42:]

file_out= open(f"{path_file}.txt", "w",encoding="latin-1")

f = open(f"{path_file}", "rb")
byte = f.read(2)
print(f)
y = []
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
        # print('acc')
        
        y.append(data_y/100)
print(y)
        # acc_fft(np.array(y) )

y[-1]=y[-2]
# print(y)
# file_out.write(str(y))
x = np.arange(len(y))

# frames = convert(y)
# print(frames.head())
# t = get_fft_acc(frames)
# t = get_fft_acc(frames)
# fig_from_df(t).show()
# print(t)
# stft_acc(y)
# plotting
plt.title("plotting")
plt.xlabel('samples')
plt.ylabel('amplitudes')
# plt.yticks(y)
plt.plot(x, y)  
plt.savefig(f'out_data_pengukuran/{name_file}.png')
# au_fft(np.array(y))
acc_fft(np.array(y) )
plt.show()
