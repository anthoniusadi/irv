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





# def convert_wav(inp_f,name,fr):
#     data = inp_f
#     with wave.open(name+".wav", "wb") as out_f:
#         out_f.setnchannels(1)
#         out_f.setsampwidth(2) # number of bytes
#         out_f.setframerate(fr)
#         out_f.writeframesraw(data)
#         with wave.open(name+".wav", "rb") as f:
#             print(repr(f.getparams()))
