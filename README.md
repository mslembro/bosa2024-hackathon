# bosa2024-hackathon

## Extract clips

Examples input file:

|Video	Fragment| Name|	Start Time|	End Time|
|---------------|-----|-----------|---------|
|20230528 PADEL VIGO  CLEAN.mp4|	Fragment 1|	00:01.68|	00:27.72|

Additional columns are allowed, but not used in this script.

 ```
python extract_clips.py --input "examples/Hack_Padel_Labelling Video240129.xlsx" --datapath_in "path/to/input/videos" --datapath_out "path/to/output/videos"
 ```

## Extract clips synced

Multicam extraction of video clips. This script requires 2 inputs:

* dataset JSON (input_dataset)
* clip timestamps file (input)


| Name|	Start Time|	End Time|
|-----|-----------|---------|
|Exchange 1	|2024-01-25 10:31:27.000000	|2024-01-25 10:31:37.000000
|

Additional columns are allowed, but not used in this script. Note that the format of this file is different from the previous section.

* No video files are supplied since these are defined in the dataset JSON file.
* The Start Time and End Time are fulle datetime timestamps instead of relative timestamps

 ```
python extract_clips_synced.py --input "examples/cycling.xlsx" --input_dataset "examples/cycling.json" --datapath_in "path/to/input/videos" --datapath_out "path/to/output/videos"
 ```

## Process Video

Meant as an example for loading a video and perform processing on it
```
python process_video.py --input "path/to/video.mp4"
```