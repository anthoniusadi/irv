import os
import wave
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

class preprocessing:
    def __init__(self,inp_f,name,fr):
        self.inp_f = inp_f
        self.fr = fr
        self.name = name
        self.n_fft = 1024
    def convert_wav(self):
        data = self.inp_f
        with wave.open(self.name+".wav", "wb") as out_f:
            out_f.setnchannels(1)
            out_f.setsampwidth(2) # number of bytes
            out_f.setframerate(self.fr)
            out_f.writeframesraw(data)
            with wave.open(self.name+".wav", "rb") as f:
                print(repr(f.getparams()))
    def stft(self,file_name,sr=22050):
        # fig, ax = plt.subplots()
        y, _ = librosa.load(file_name)
        stft = np.abs(librosa.stft(y, n_fft=self.n_fft))
        librosa.display.specshow(stft, x_axis='time', y_axis='log', sr=sr)
        print(sr)
        plt.savefig(self.name+"_STFT.png")
        # plt.show()
        return y

    def vibration(self):
        path_data = self.inp_f
        folder_csv = 'data/lebokekenedatane/csv_acc/'
        file_name = os.path.basename(path_data)
        base_filename = os.path.splitext(file_name)
        print(base_filename[0])
        file_out= open(f"{folder_csv+base_filename[0]}.txt", "w",encoding="latin-1")
        file = open(f"{path_data}", "rb")
        byte = file.read(2)
        y = []
        while byte:
            byte = file.read(2)
            data_y = int.from_bytes(byte, "big", signed=True) / 100
            y.append(data_y)
        y[-1] = y[-2]
        file_out.write(str(y))
        print(f'raw data vibration saved in {folder_csv}')

        return y

    def audio(self):
        path_data = self.inp_f
        file_name = os.path.basename(path_data)
        base_filename = os.path.splitext(file_name)
        print(base_filename[0])
        folder_csv ='data/lebokekenedatane/csv_au/'
        file_out= open(f"{folder_csv+base_filename[0]}.txt", "w",encoding="latin-1")

        f = open(f"{path_data}", "rb")
        byte = f.read(2)
        y = []
        while byte:
            byte = f.read(2)
            data_y = int.from_bytes(byte, "big", signed=True) 
            tmp = scaling(data_y,xmax=4095 ,xmin=-1) 
            y.append(tmp)
        y[-1]=y[-2]

        file_out.write(str(y))
        print(f'raw data audio saved in {folder_csv}')
        return y
def scaling(x,xmax,xmin):
    x_new = np.float64(((2/xmax)*x) + xmin)
    return x_new

def plot(data_y,save=False,name_save='waveForm'):
    x = np.arange(len(data_y))
    y = data_y
    plt.title("plotting")
    plt.xlabel('samples')
    plt.ylabel('amplitudes')
    plt.plot(x, y)  
    if save:

        if('acc' in name_save):
            plt.savefig(f'data/lebokekenedatane/gambar/vib/{name_save}.png')
            print(f'plot data {name_save}.png saved\n')
        else:
            plt.savefig(f'data/lebokekenedatane/gambar/audio/{name_save}.png')
            print(f'plot data {name_save}.png saved\n')
            
    plt.show()




