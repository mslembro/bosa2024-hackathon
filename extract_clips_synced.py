import argparse
import json
import pandas as pd
import os
from datetime import datetime
from datetime import timedelta

parser = argparse.ArgumentParser(description='Extract video clips')
parser.add_argument('--input', type=str, default="examples/cycling.xlsx", help='excel file with the timestamps of relevant data')
parser.add_argument('--input_dataset', type=str, default="examples/cycling_sync.json", help='input dataset')
parser.add_argument('--datapath_in', type=str, default="./", help='path of the input video folder')
parser.add_argument('--datapath_out', type=str, default="./", help='path of the input video folder')

args = parser.parse_args()

# Opening JSON file
f = open(args.input_dataset)

# returns JSON object as 
# a dictionary
data = json.load(f)

df = pd.read_excel(args.input)
df = df.reset_index()

# create output folder
os.makedirs(args.datapath_out, mode = 0o777, exist_ok = True)

for i, row in df.iterrows():
    st = datetime.strptime(row["Start Time"], '%Y-%m-%d %H:%M:%S.%f')
    et = datetime.strptime(row["End Time"], '%Y-%m-%d %H:%M:%S.%f')

    # determine videos that are within the interval
    vstack_videos = []
    for vid in data["videos"]:

        video_start = datetime.strptime(data["videos"][vid]["rtctime"], '%Y-%m-%d %H:%M:%S.%f')
        duration = datetime.strptime(data["videos"][vid]["duration"], "%H:%M:%S.%f")
        delta = timedelta(hours=duration.hour, minutes=duration.minute, seconds=duration.second,microseconds=duration.microsecond)
        video_end = video_start + delta

        print(video_start, video_end)
        if st > video_start and st < video_end:
            #extract start time in video
            clip_start = st-video_start
            clip_end = et-video_start

            video_out = os.path.join(args.datapath_out, row["Fragment Name"] + "_" + data["videos"][vid]["path"]) 
            
            vstack_videos.append(video_out)

            cmd = "ffmpeg -n -i '" + os.path.join(args.datapath_in, data["videos"][vid]["path"]) + "' -ss " + str(clip_start) + " -to " + str(clip_end) + " -c:v libx264 -crf 17 '" + video_out + "'"   
            print(cmd)
            os.system(cmd)

    if len(vstack_videos) > 0:
        cmd = "ffmpeg -n"
        for vid in vstack_videos:
            cmd += " -i '" + vid + "'"
        cmd += " -filter_complex vstack=inputs=" + str(len(vstack_videos)) + " -c:v libx264 -crf 17 '" + row["Fragment Name"] + ".mp4'"
        print(cmd)
        os.system(cmd)
    else:
        print("No video clip can be generated in given interval")
