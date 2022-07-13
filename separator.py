from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
import numpy as np
import glob
# import os
import os

# handle incoming args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--threshold', type=str, required=True, help='threshold')

# get the args
args = parser.parse_args()
threshold = float(args.threshold)

source_files = 'target'
ignore_files = 'ignore'

encoder = VoiceEncoder()

wavs = []
ignore_wavs = []

for source_file in glob.glob(os.path.join(source_files, '*.wav')):
    spath = Path(source_file)
    print("spath is" + str(spath))
    wav = preprocess_wav(spath)
    print("spath is" + source_file)
    embed = encoder.embed_utterance(wav)
    wavs.append(embed)

for ignore_file in glob.glob(os.path.join(ignore_files, '*.wav')):
    spath = Path(ignore_file)
    print("spath is" + str(spath))
    wav = preprocess_wav(spath)
    print("spath is" + ignore_file)
    embed = encoder.embed_utterance(wav)
    ignore_wavs.append(embed)


# get a list of audio files from the juice/wavs directory
wav_path = 'wavs/*.wav'
wav_files = glob.glob(wav_path)

# make a directory at juice/not_speaker
not_speaker_dir = Path('not_speaker')
not_speaker_dir.mkdir(parents=True, exist_ok=True)

# for each wav file
for fpath in wav_files:
    input_wav = preprocess_wav(fpath)
    threshold_reached = False
    for embed in wavs:
        input_embed = encoder.embed_utterance(input_wav)

        np.set_printoptions(precision=5, suppress=True)

        spk_sim_matrix = np.inner(input_embed, embed)
        if(spk_sim_matrix >= threshold):
            threshold_reached = True
            print("Ignore file, threshold not met" + str(fpath))
            break

    if(threshold_reached == True):
        for embed in ignore_wavs:
            input_embed = encoder.embed_utterance(input_wav)

            spk_sim_matrix = np.inner(input_embed, embed)
            if(spk_sim_matrix >= threshold):
                threshold_reached = False
                print("Ignore file, other speaker heard" + str(fpath))
                break

    if(threshold_reached == False):
        print("Audio is not speaker: " + fpath)
        Path(fpath).rename('not_speaker/' + Path(fpath).name)
print("Finished")