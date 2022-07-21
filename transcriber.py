import glob

import speech_recognition as sr
from os import path, rename

r = sr.Recognizer()

# get a list of audio files from the juice/wavs directory
wav_files = glob.glob('./wavs/*.wav')

metadata = []

# for each wav file
for fpath in wav_files:
    with sr.AudioFile(fpath) as source:
        print()
        audio = r.record(source)  # read the entire audio file
        transcription = ''
        try:
            transcription = r.recognize_google(audio)
            print(fpath + "|" + transcription)
            metadata.append(fpath + "|" + transcription)
        except:
            print('Skipping ' + fpath)
            new_fpath = './ignore/' + path.basename(fpath)
            # now move the file to the skipped directory
            rename(fpath, new_fpath)
            continue

metadata_txt = '\n'.join(metadata)

with open("metadata.csv", "w") as text_file:
    text_file.write(metadata_txt)
    

