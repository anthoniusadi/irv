# konversi binary raw data audio dan plotting
# save plotting sesuai nama path_file

import matplotlib.pyplot as plt
import numpy as np

def scaling(x,xmax,xmin):
    x_new = np.float64(((2/xmax)*x) + xmin)
    return x_new
path_file = 'data/lebokekenedatane/raw_au/au_1666025655_-7.781549_110.391403'
file_out= open(f"{path_file}.txt", "w",encoding="latin-1")

f = open(f"{path_file}", "rb")
byte = f.read(2)
y = []
while byte:
    byte = f.read(2)
    data_y = int.from_bytes(byte, "big", signed=True) 
    print(data_y)

    tmp = scaling(data_y,xmax=4095 ,xmin=-1) 
    y.append(tmp)

y[-1]=y[-2]
# file_out.write(str(y))
x = np.arange(len(y))
# plotting
plt.title("plotting")
plt.xlabel('samples')
plt.ylabel('amplitudes')
# plt.yticks(y)
plt.plot(x, y)  
# plt.savefig(f'data/{name_file}.png')
plt.show()
