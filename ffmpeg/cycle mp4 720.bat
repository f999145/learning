mkdir outputs
for %%a in ("*.mkv") do (
    ffmpeg -y ^
    -i "%%a" ^
    -vf scale=1280:-1 ^
    -preset slow ^
    -c:v h264_nvenc ^
    -b:v 3M ^
    -profile:v high ^
    -level 4 ^
    -af "pan=stereo|FL < 0.7*FC + 0.3*FLC + 0.3*FL + 0.3*BL + 0.3*SL + 0.5*LFE | FR < 0.7*FC + 0.3*FRC + 0.3*FR + 0.3*BR + 0.3*SR + 0.5*LFE" -c:a aac -b:a 192k ^
    "outputs\%%~na.mp4")
pause