mkdir outputs
for %%a in ("*.mkv") do ffmpeg -y -i "%%a" -preset slow -c:v h264_nvenc -b:v 8M -profile:v high -level 5.2 -c:a aac -b:a 192k "outputs\%%~na.mp4"
pause