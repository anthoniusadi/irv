from mods.proc import preprocessing
from mods.proc import plot
audio_raw = 'data/lebokekenedatane/raw_au/au_1666025655_-7.781549_110.391403'
vibration_raw = 'data/lebokekenedatane/raw_acc/acc_1666025645_-7.781504_110.391418'
# proses audio
audio_preprocessing = preprocessing(audio_raw,'output_audio',8000)
y = audio_preprocessing.audio()
plot(y,save=True,name_save='audio_wave')

# proses getaran
vib_preprocessing = preprocessing(vibration_raw,'output_vib',400)
y = vib_preprocessing.vibration()
plot(y,save=True,name_save='vibration_wave')