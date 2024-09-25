import py_midicsv as pm

csv_str_list = pm.midi_to_csv(r"C:\Users\letua\Downloads\maestro-v3.0.0-midi\maestro-v3.0.0\2009\MIDI-Unprocessed_06_R1_2009_03-07_ORIG_MID--AUDIO_06_R1_2009_06_R1_2009_06_WAV.midi")

with open("example.csv", 'w') as f:
    f.writelines(csv_str_list)
    
