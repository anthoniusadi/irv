from datetime import datetime
import os
import numpy as np

def create_dirs(folder,name,fitur_sensor):
    # try:
    # os.mkdir(os.path.join(folder,name))
    os.makedirs(os.path.join(folder,name,fitur_sensor))
    print("folder '{}' created ".format(fitur_sensor+name))
    # except FileExistsError:
    #     pass
    #     print("folder {} already exists".format(name))


folder = 'data/Data Pengukuran 3 Jakarta Bandung Jogja/'
unik = list()
for f in os.listdir(folder):
    nameFile = f.split(sep='_')
    timestamp = nameFile[1]
    date_time = datetime.fromtimestamp(int(timestamp))
    tgl = f'{date_time.year}_{date_time.month}_{date_time.day}'
    waktu = f'{date_time.hour}_{date_time.minute}_{date_time.second}'
    fname = f'{nameFile[0]}#{tgl}#{waktu}#{nameFile[2]}#{nameFile[3]}#{nameFile[4]}'
    unik.append(tgl)
    # os.rename(os.path.join(folder,f),os.path.join(folder,tgl,fname))
# tmp_bulan = np.array(bulan)
m = np.unique(np.array(unik))
sensor = ['au','acc']

for b in m:
    # print(b)
    for s in sensor:
        create_dirs(folder,str(b),s)
        
for f in os.listdir(folder):
    if len(f)>15:
        nameFile = f.split(sep='_')
        timestamp = nameFile[1]
        date_time = datetime.fromtimestamp(int(timestamp))
        tgl = f'{date_time.year}_{date_time.month}_{date_time.day}'
        waktu = f'{date_time.hour}_{date_time.minute}_{date_time.second}'
        fname = f'{nameFile[0]}#{tgl}#{waktu}#{nameFile[2]}#{nameFile[3]}#{nameFile[4]}'
        if tgl in m:
            os.rename(os.path.join(folder,f),os.path.join(folder,tgl,nameFile[0],fname))
            
