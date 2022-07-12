from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
import numpy as np
import glob

# handle incoming args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--source', type=str, required=True, help='source audio file')
parser.add_argument('--threshold', type=str, required=True, help='threshold')

# get the args
args = parser.parse_args()
source_file = args.source
threshold = float(args.threshold)

spath = Path(source_file)
wav = preprocess_wav(spath)


# get a list of audio files from the juice/wavs directory
wav_files = glob.glob('./wavs/*.wav')

# make a directory at juice/not_speaker
not_speaker_dir = Path('./not_speaker')
not_speaker_dir.mkdir(parents=True, exist_ok=True)

# for each wav file
for fpath in wav_files:

    input_wav = preprocess_wav(fpath)

    encoder = VoiceEncoder()
    embed = encoder.embed_utterance(wav)
    input_embed = encoder.embed_utterance(input_wav)

    np.set_printoptions(precision=5, suppress=True)

    spk_sim_matrix = np.inner(input_embed, embed)
    print(spk_sim_matrix)
    if(spk_sim_matrix < threshold):
        print("Audio is not speaker: " + fpath)
        # move the audio to the juice/not_speaker directory
        Path(fpath).rename('not_speaker/' + Path(fpath).name)