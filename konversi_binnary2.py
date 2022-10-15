import csv

import matplotlib.pyplot as plt
import numpy as np

path ='binary_contoh'
a=[]
file_out= open("out2.txt", "w") 

with open(path, 'rb') as file:
    callable = lambda: file.read()
    sentinel = bytes() # or b''
    for chunk in iter(callable, sentinel): 
        for byte in chunk:
            # print(byte)
            a.append(byte)
            file_out.write(str(byte)+',')
print(max(a),len(a),type(a))
  
x = np.arange(len(a))
y = a
f = open("binary_contoh", "r") 

# for line in a:
#     print(line)
plt.title("plotting")
plt.xlabel('samples')
plt.ylabel('amplitudes')
# plt.yticks(y)
plt.plot(x, y)
  
plt.show()