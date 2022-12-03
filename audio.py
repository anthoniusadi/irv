import numpy as np
import matplotlib.pyplot as plt
import librosa.display
import wave
import os
from konversi_raw import au_fft
import librosa
import scipy as sp
###############################################################################
def scaling(x,xmax,xmin):
    x_new = np.float64(((2/xmax)*x) + xmin)
    return x_new

def translate(byte):
    # status = True
 


    # byte = f.read(2)
    data_y = int.from_bytes(byte, "big", signed=True) 

    tmp = scaling(data_y,xmax=4095 ,xmin=-1) 
    return tmp # type:ignore
        # au_fft(np.array(y) )
###############################################################################
def fft_scipy(file):
    pass

def openfile(inputName):
    myfile = open(inputName, 'rb')
    x = myfile.read()
    y = list(x)
    return y

def swab(input):
    output = b''
    for i in range(24000):
        a = input[i*2]
        b = input[(i*2)+1]
        output += b.to_bytes(1, 'big')
        output += a.to_bytes(1, 'big')

    return output

def toWav(input,folder,fname):
    with wave.open(f"{folder}{fname}.wav", "wb") as out_f:
        out_f.setnchannels(1)
        out_f.setsampwidth(2) # number of bytes
        out_f.setframerate(8000)
        out_f.writeframesraw((input))
        out_f.close()

def get_fft(path):
    audio_path = path
    x , sr = librosa.load(audio_path,sr=8000)
    ft = sp.fft.fft(x)
    mag = np.absolute(ft) # type: ignore
    freq = np.linspace(0,sr,len(mag))

    fig, ax = plt.subplots()
    # plt.figure(figsize=(10,5))
    # plt.plot(freq,mag)
    plt.xlabel('freq(Hz)')
    plt.ylabel('Magnitude')
    plt.title('fft audio')
    ax.plot(freq,mag)
    ax.set_xlim(0, sr / 2)
    ax.set_ylim(0,10)
    # plt.savefig(path[:-4]+'_fft'+".png")
    # plt.show()


# folder = 'data/3 detik/'
folder = 'data/temp_data/'
# listdata = openfile('data/3 detik/au_1665556707_-778290_11036705_1125')
# data = swab(listdata)
# toWav(data)
num=0

for f in os.listdir(folder):
    if f[:2]=='au':
        num+=1
        convert = openfile(folder+f)
        data = swab(convert)
        toWav(data,folder,f)

for i in os.listdir(folder):
    if i[-4:]=='.wav':
        print(f'{i} is processed')
        get_fft(os.path.join(folder,i))

# get_fft('data/3 detik/au_1665556707_-778290_11036705_1125.wav')