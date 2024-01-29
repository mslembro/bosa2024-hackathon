import argparse
import pandas as pd
import os

parser = argparse.ArgumentParser(description='Extract video clips from input data')
parser.add_argument('--input', type=str, default="examples/Hack_Padel_Labelling Video240129.xlsx", help='excel file with the timestamps of relevant data')
parser.add_argument('--datapath_in', type=str, default="./", help='path of the input video folder')
parser.add_argument('--datapath_out', type=str, default="./", help='path of the input video folder')

args = parser.parse_args()

print(args.input)

df = pd.read_excel(args.input)
df = df.reset_index()

# create output folder
os.makedirs(args.datapath_out, mode = 0o777, exist_ok = True)

for i, row in df.iterrows():
    cmd = "ffmpeg -i '" + args.datapath_in + row["Video"] + "' -ss " + str(row["Start Time"]) + " -to " + str(row["End Time"]) + " -c copy '" + args.datapath_out + "{:02d}".format(i) + "_" +row["Fragment Name"] + "_" + row["Video"] + "'"   
    print(cmd)
    os.system(cmd)