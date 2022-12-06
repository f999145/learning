mkdir outputs
for %%a in ("*.webm") do ffmpeg -y -i "%%a" -vf scale=-1:1080 -c:v dnxhd -profile:v dnxhr_lb -c:a aac -b:a 192k -alpha_bits 0 "outputs\%%~na.mov"
pause