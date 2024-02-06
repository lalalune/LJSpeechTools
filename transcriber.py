import glob

import speech_recognition as sr
from os import path, rename
from whisper_transcribe import Whisper_Transcriber

def transcribe(provider = "google", google_speech_api_key = None, model_name="large-v3"):
    r = None
    whisper_transcriber = None

    if provider == "google":
        if google_speech_api_key == None:
            print("Error: Google speech api key is required to use google transcription option")
            return

        r = sr.Recognizer()

    elif provider == "whisper":
        whisper_transcriber = Whisper_Transcriber()
        whisper_transcriber.init(model_name)
    else:
        print('Unknown transcription source')
        return

    wav_files = glob.glob('./wavs/*.wav')

    metadata = []

    # for each wav file
    for fpath in wav_files:
            print()
            transcription = ''
            try:
                print(f"Transcribing : {fpath}")
                if provider == "google":
                    with sr.AudioFile(fpath) as source:
                        audio = r.record(source.filename_or_fileobject)  # read the entire audio file
                        transcription = r.recognize_google(audio, key=google_speech_api_key)
                elif provider == "whisper":
                    transcription = whisper_transcriber.transcribe(audio_file_name=fpath)

                print("     " + transcription)
                metadata.append(fpath + "|" + transcription)
            except Exception as error:
                print('Skipping ' + fpath + ' : An Error occurred : '+ error)
                metadata.append(fpath + "|" + "<ERROR>")
                new_fpath = './ignore/' + path.basename(fpath)
                # now move the file to the skipped directory
                rename(fpath, new_fpath)
                continue

    metadata_txt = '\n'.join(metadata)

    with open("metadata.csv", "w") as text_file:
        text_file.write(metadata_txt)
        

if __name__ == "__main__":
    # Use open ai whisper with large-v3 model, slow but best result
    transcribe(provider="whisper")

    # Use open ai whisper with large-v3 model, slow but best result
    # valid responses : tiny, base, small, medium, large, large-v2, or large-v3
#    transcribe(provider="whisper", model_name = "tiny")

    # Use Google Speech API.  In previous versions of LJ Speech Toolset relied on an embedded ket in
    # the speech recoginition library, that has been revoked.  Toy will need to provide your own API KEY
#    transcribe(provider="google", google_speech_api_key="[PLACE YOUR GOOGLE SPEECH KEY HERE")
