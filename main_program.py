from mods.proc import preprocessing
from mods.proc import plot
import os

# audio_raw = 'data/lebokekenedatane/raw_au/au_1666025655_-7.781549_110.391403'
# vibration_raw = 'data/lebokekenedatane/raw_acc/acc_1666025645_-7.781504_110.391418'
# # proses audio
# audio_preprocessing = preprocessing(audio_raw,'output_audio',8000)
# y = audio_preprocessing.audio()
# plot(y,save=True,name_save='audio_wave')

# # proses getaran
# vib_preprocessing = preprocessing(vibration_raw,'output_vib',400)
# y = vib_preprocessing.vibration()
# plot(y,save=True,name_save='vibration_wave')

# process each file in folder
folderName_audio = 'data/lebokekenedatane/raw_au'
for f in os.listdir(folderName_audio):
    p_file = os.path.join(folderName_audio,f)
    print(p_file)
    audio_preprocessing = preprocessing(p_file,'output_audio',8000)
    y = audio_preprocessing.audio()
    plot(y,save=True,name_save=f)

    print(f'{f} is process')

folderName_acel = 'data/lebokekenedatane/raw_acc/'
for f in os.listdir(folderName_acel):
    p_file = os.path.join(folderName_acel,f)
    print(p_file)
    vib_preprocessing = preprocessing(p_file,'output_vib',400)
    y=vib_preprocessing.vibration()
    plot(y,save=True,name_save=f)
    print(f'{f} is process')
