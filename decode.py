import py_midicsv as pm

csv_str_list = pm.midi_to_csv(r"C:\Users\letua\Downloads\maestro-v3.0.0-midi\maestro-v3.0.0\2018\MIDI-Unprocessed_Chamber2_MID--AUDIO_09_R3_2018_wav--1.midi")

with open("example2.csv", 'w') as f:
    f.writelines(csv_str_list)
    
