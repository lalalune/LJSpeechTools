# split metadata.csv into two files -- train_filelist.txt and val_filelist.txt
# val_filelist.txt should randomly have 10% of the lines of text while train_filelist.txt should have about 90%
import csv
import random
import os
import sys

# read in the metadata.csv file
with open('metadata.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    # split the lines into two different arrays -- train and val
    # randomly select 10% of the lines to be in the val array
    train = []
    val = []
    for line in data:
        if random.random() < 0.1:
            val.append(line[0])
        else:
            train.append(line[0])
    # save the files
    with open('train_filelist.txt', 'w') as f:
        for line in train:
            f.write(line + '\n')
    with open('val_filelist.txt', 'w') as f:
        for line in val:
            f.write(line + '\n')

# zip all the wavs in the wavs folder into a zip file and save as dataset.zip
os.system('zip -r dataset.zip wavs')

print('done')