import glob

import speech_recognition as sr
from os import path

r = sr.Recognizer()

# get a list of audio files from the juice/wavs directory
wav_files = glob.glob('./wavs/*.wav')

metadata = []

# for each wav file
for fpath in wav_files:
    with sr.AudioFile(fpath) as source:
        audio = r.record(source)  # read the entire audio file
        transcription = r.recognize_google(audio)
        print("Transcription: " + transcription)
        # write the transcription to a file
        metadata.append(fpath + "|" + transcription)

metadata_txt = '\n'.join(metadata)

with open("metadata.csv", "w") as text_file:
    text_file.write(metadata_txt)
    

