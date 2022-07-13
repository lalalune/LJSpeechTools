# LJSpeech Tools
Tools for creating LJSpeech datasets from WAV files

To install:

```bash
sudo apt install ffmpeg
pip install resemblyzer SpeechRecognition
```

To remove any wav files which contain audio which isn't the source speaker

First, place some example audio from your speaker in the 'target' folder.

Then, place any example audio from speakers who are *not* your speaker in the 'ignore' folder

Then run the separate.py with a --threshold, probably somewhere between 0.6 and 0.9

```bash
bash separate.sh
# or
python separator.py --threshold=0.65
```

To transcribe audio files in the wavs folder
```bash
bash transcribe.sh
# or
python transcriber.py
```

Transcription will create an LJSpeech compatible 'metadata.csv'

The files are very simple and lean heavily on existing libraries. Feel free to open the source and modify as you need, it's not that scary!
