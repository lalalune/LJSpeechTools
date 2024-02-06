import os
import glob
import shutil
from audiosplitter import split_all_audios, split_long_audios, filter_short_audios
import argparse

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




def main():
    parser = argparse.ArgumentParser(
        prog='LJ Speech Toolset',
        description='chops up wav files and adds transcription, outputs in LJ Speech format')
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--provider',  help='Set transcription provider (google or whisper) default is whisper', default="whisper")
    parser.add_argument('-k', '--speech_key',  help='Google Speech API Key')
    parser.add_argument('-m', '--model',   help='Open AI Whisper model (tiny, base, small, medium, large, large-v2, or large-v3) to use, default large-v3', default="large-v3")
#    parser.add_argument('--help',  action='store_true', help='show help')
    args = parser.parse_args()

    if args.provider == "google" and args.speech_key == None:
        print("Error: you must provide a google speech api key to use google transcriber")
        return

 #   if args.help:
#        parser.print_help()
#        return


    clear_wavs();
    copy_wavs();

    # 1. split audio files with audiosplitter

#    split_all_audios();
    split_long_audios();
    filter_short_audios();

    # 2. transcribe audio files with transcriber

    from transcriber import transcribe

    transcribe(provider=args.provider, google_speech_api_key=args.speech_key, model_name=args.model);

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


if __name__ == "__main__":
    main()