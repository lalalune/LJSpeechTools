# convert all mp3 files in a directory to wav files
for file in *.mp3 do
        echo "Converting $file"
        # replace .mp3 extension with .wav extension
        new_file=${file%.mp3}.wav
        ffmpeg -i $file -acodec pcm_s16le -ac 1 -ar 16000 $new_file
    done
done