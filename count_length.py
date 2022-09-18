# using pydub, read all of the files in the /wavs folder, add up the total length and print
from pydub import AudioSegment
import glob

def get_length(filename):
    song = AudioSegment.from_wav(filename)
    return len(song)

def get_total_length(filenames):
    total_length = 0
    for filename in filenames:
        total_length += get_length(filename)
    return total_length

#glob all files in the wavs folder and call get_total_length
filenames = glob.glob('./wavs/*.wav')
total_length = get_total_length(filenames)

print("Total length of " + str(len(filenames)) + " files: " + str(total_length/1000) + "s" + " or " + str(total_length/60000) + "m")

# get the longest file
longest = max(filenames, key=get_length)
print("Longest file: " + longest + " at " + str(get_length(longest)/1000) + "s")
shortest = min(filenames, key=get_length)
print("Shortest file: " + shortest + " at " + str(get_length(shortest)/1000) + "s")