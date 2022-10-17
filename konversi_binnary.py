# int 16bit   2byte
# dibagi 100
from os import sep
from numpy import size

import matplotlib.pyplot as plt
import numpy as np
name_file = 'binary_contoh'
file_out= open(f"{name_file}.txt", "w",encoding="latin-1")
def decode_tostring(payload):
    return payload.decode('latin-1').encode('ascii', errors='xmlcharrefreplace').decode('ascii')

file = open(f"{name_file}", "rb")
lines = []
byte = file.read(2)
y = []
while byte:
    # print(byte)
    byte = file.read(2)
    data_y = int.from_bytes(byte, "big", signed=True) / 100

    y.append(data_y)

    # data = file_out.write(str(data_y)+' ')
y[-1] = y[-2]
file_out.write(str(y))

print(f'last : {y}')

print(f'max data y : {max(y)}, PANJANG DATA : {len(y)}')
# print(x)
# print(len(x))
x = np.arange(len(y))
plt.title("plotting")
plt.xlabel('samples')
plt.ylabel('amplitudes')
# plt.yticks(y)
plt.plot(x, y)  
# plt.savefig(f'data/{name_file}.png')
# plt.show()
