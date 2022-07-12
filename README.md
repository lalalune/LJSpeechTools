# Speaker Isolation
A super simple, python based solution for separating a folder of audio files by speaker

To install

```bash
# optional
conda create env --name=separator
# optional
conda activate separator

sudo apt install ffmpeg

pip install resemblyzer
```

To run
```bash
bash separate.sh
# or
python resemblyze.py --source=date1.wav --threshold=0.65
```

