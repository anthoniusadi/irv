'''
samplingrate= 8000
unsigned integer 16 bit
value 0-4095
map to -1 to 1
'''
path_file = 'data/lebokekenedatane/au_1666025645_-7.781504_110.391418'
import soundfile as sf
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

sig, fs = sf.read(path_file, channels=1,dtype='int8', samplerate=24000,
                  format='RAW', subtype='PCM_16')
              
# sd.play(sig, fs)
print(type(sig))
print(fs)
tmp=[]
for i in sig:
    tmp.append(i)
with open('out_au_1666025645_-7781504_110391418.txt','w') as f:
    f.write(str(tmp))

x = np.arange(len(tmp))
y = tmp
plt.title("plotting")
plt.xlabel('samples')
plt.ylabel('amplitudes')
# plt.yticks(y)
plt.plot(x, y)  
# plt.savefig(f'data/{name_file}.png')
plt.show()
