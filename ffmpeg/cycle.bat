@echo off
setlocal enabledelayedexpansion

set input_folder=A:\input_folder
set output_folder=A:\output_folder

for %%a in ("%input_folder%\*.*") do (
    set input_file=%%a
    set output_file=%output_folder%/%%~na.mp4
    ffmpeg -y ^
    -i "!input_file!" ^
    -vf scale=1920:-1 ^
    -c:v h264_nvenc ^
    -preset fast ^
    -profile:v main ^
    -level 4.2 ^
    -cbr true ^
    -b:v 8M ^
    -c:a aac ^
    -b:a 192k ^
    -af "pan=stereo|FL < 0.7*FC + 0.3*FLC + 0.3*FL + 0.3*BL + 0.3*SL + 0.5*LFE | FR < 0.7*FC + 0.3*FRC + 0.3*FR + 0.3*BR + 0.3*SR + 0.5*LFE" ^
    "!output_file!"
)
pause