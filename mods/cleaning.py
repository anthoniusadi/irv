import numpy as np
# import librosa
# import pandas as pd
class clean:
    def __init__(self,file_txt):
        self.file_txt = file_txt
        self.temp_arr = []
    def cleaning(self):
        with open(self.file_txt) as f:
            content = f.read()
            for lines in content.replace(',','.').split():
                for data in lines.split(';'):
                    x = data.replace(',','.')
                    self.temp_arr.append(np.float32(x))
        return np.array(self.temp_arr)


# temp_arr = []
# # txt = 'test.txt'
# def cleaning(file_txt):
#     with open(file_txt) as f:
#         content = f.read()
#         for lines in content.replace(',','.').split():
#             for data in lines.split(';'):
#                 x = data.replace(',','.')
#                 temp_arr.append(np.float32(x))
#     return np.array(temp_arr)

