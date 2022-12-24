mkdir outputs
for %%a in ("*.mkv") do ffmpeg -y -i "%%a" -vf scale=-1:720 -preset slow -c:v h264_nvenc -b:v 3M -profile:v high -level 4 -c:a aac -b:a 192k "outputs\%%~na.mp4"
pause