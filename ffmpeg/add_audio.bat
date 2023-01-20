ffmpeg -i "lou.mkv" -i Untitled.wav -map 0 -map 1:a -c:v copy output.mkv
pause