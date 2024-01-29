# bosa2024-hackathon

## Extract clips

Examples input file:

|Video	Fragment| Name|	Start Time|	End Time|	Duration|	Label 1|	Label 2|	Label 3|
|---------------|-----|-----------|---------|-----------|----------|-----------|-----------|
|20230528 PADEL VIGO  CLEAN.mp4|	Fragment 1|	00:01.68|	00:27.72|	00:26.04|	D| |   |

 ```
python extract_clips.py --input "examples/Hack_Padel_Labelling Video240129.xlsx" --datapath_in "path/to/input/videos" --datapath_out "path/to/output/videos"
 ```

## Process Video

```
python process_video.py --input "path/to/video.mp4"
```