import os
import glob
import shutil
from audiosplitter import split_all_audios, split_long_audios, filter_short_audios

# clear out the wavs folder using python

# if wavs folder doesn't exist, create it
if not os.path.exists('./wavs'):
    os.makedirs('./wavs')

def clear_wavs():
    for wav in glob.glob('./wavs/*.wav'):
        os.remove(wav)

# copy all wavs from put_audio_files_here into wavs
def copy_wavs():
    for wav in glob.glob('./put_audio_files_here/*.wav'):
        shutil.copy(wav, './wavs/')

clear_wavs();
copy_wavs();

# 1. split audio files with audiosplitter

split_all_audios();
split_long_audios();
filter_short_audios();

# 2. transcribe audio files with transcriber

from transcriber import transcribe

transcribe();

# 3. swearing

from swearing import replace_censored_words

replace_censored_words();

print('replace_censored_words')

# 4. prepare dataset

from make_dataset import make_dataset

make_dataset();

print('ok')

# delete wavs_split_temp

shutil.rmtree('wavs_split_temp')

# delete wavs_split_final
shutil.rmtree('wavs_split_final')

# delete wavs
clear_wavs();