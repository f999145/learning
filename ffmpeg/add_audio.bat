ffmpeg -y -i "lou.mkv" -map 0:v:0 -map 0:a:0 -c:v copy -ac 2 -c:a libmp3lame -b:a 320k output.mkv
pause
