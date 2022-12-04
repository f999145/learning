Get-ChildItem -Filter *.webm -recurse | % { ffmpeg -y -i $_.Name -vf scale=-1:1080 -c:v dnxhd -profile:v dnxhr_lb -c:a aac -b:a 192k (("render"+"\"+$_.Name+".mov")) }
pause

::for %i in (*.webm) do ffmpeg -i "%i" "%~ni.mov"
::for %i in (*.webm) do ffmpeg -y -i "%i" -vf scale=-1:1080 -c:v dnxhd -profile:v dnxhr_lb -c:a aac -b:a 192k "%~ni.mov"
::Get-ChildItem *.ogg -recurse | % { ffmpeg.exe -i $_.FullName -map_metadata -1 -c:v copy -c:a copy ("NewPath" + "\" +$_.Name) }
::FOR /F "tokens=*" %G IN ('dir /b *.flac') DO ffmpeg -i "%G" -acodec mp3 "%~nG.mp3"
::ffmpeg -y ^

::-i "THE TEST 1440.webm" ^

::                              вырезать фрагмент видео
:: -ss 01:00:00 -to 02:00:00 

::                              Specify the Height To Retain the Aspect Ratio
::                              https://ottverse.com/change-resolution-resize-scale-video-using-ffmpeg/
::-vf scale=-1:1080 ^

::                              frame rate
:: -r 24 ^                  

::                              Kodec
::-c:v dnxhd ^                

::                              DNxHR LB: dnxhr_lb - Low Bandwidth. 8-bit 4:2:2 (yuv422p). Offline Quality.
::                              DNxHR SQ: dnxhr_sq - Standard Quality. 8-bit 4:2:2 (yuv422p). Suitable for delivery format.
::                              DNxHR HQ: dnxhr_hq - High Quality. 8-bit 4:2:2 (yuv422p).
::                              DNxHR HQX: dnxhr_hqx - High Quality. 10-bit 4:2:2 (yuv422p10le). UHD/4K Broadcast-quality delivery.
::                              DNxHR 444: dnxhr_444 - Finishing Quality. 10-bit 4:4:4 (yuv444p10le). Cinema-quality delivery.
::-profile:v dnxhr_lb ^                           

::                              кодирование аудио
::-c:a aac -b:a 192k ^        

::                              Possible values are 0, 8 and 16. Use 0 to disable alpha plane coding.
::-alpha_bits 0 ^             

::                              8-bit 4:2:0: yuv420p
::                              8-bit 4:2:2: yuv422p
::                              8-bit 4:4:4: yuv444p
::                              10-bit 4:2:0: yuv420p10le
::                              10-bit 4:2:2: yuv422p10le
::                              10-bit 4:4:4: yuv444p10le 
:: -pix_fmt yuv422p ^

::                              делить видео на фрагменты
:: -f segment ^            
:: -segment_time 00:02:00 ^
:: -reset_timestamps 1 ^
:: output%03d.mov" ^

::fin.mov
::pause