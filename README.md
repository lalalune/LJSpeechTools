# LJSpeech Tools
Tools for creating LJSpeech datasets from WAV files

To install:

```bash
sudo apt install ffmpeg
pip install resemblyzer SpeechRecognition
```

To remove any wav files which contain audio which isn't the source speaker
```bash
bash separate.sh
# or
python separator.py --source=date1.wav --threshold=0.65
```

To transcribe audio files in the wavs folder
```bash
bash transcribe.sh
# or
python transcriber.py
```

Transcription will create an LJSpeech compatible 'metadata.csv'

The files are very simple and lean heavily on existing libraries. Feel free to open the source and modify as you need, it's not that scary!
