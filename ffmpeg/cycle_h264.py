import os
import subprocess

# path = os.path.join('/','mnt', 'test', 'youtube') 
path_in = os.path.join('a:\\', 'youtube')
path_out = os.path.join('a:\\', 'youtube', 'out')


files = []
for dirpath, dirname, filenames in (os.walk(path_in)):
    for file in filenames:
        files.append(os.path.join(dirpath, file))

if not os.path.isdir(path_out):
    os.mkdir(path_out)

for file in files[:1]:
    """multi(1080p) = 5.375
    """
    name, ext = os.path.splitext(os.path.basename(file))
    args =[
        'ffmpeg', '-y',
        
        '-ss', '00:05:00', '-to', '00:20:00', # вырезать фрагмент видео
        
        '-i', file,
            
        '-vf', 'scale=-1:1440', # Specify the Height To Retain the Aspect Ratio
                                # https://ottverse.com/change-resolution-resize-scale-video-using-ffmpeg/
        
        # '-r', '24',             # frame rate
        
        '-c:v', 'h264_nvenc',
        '-b:v', '40M',
        '-minrate', '39M',
        '-maxrate', '40M',
        '-bufsize', '2M',
       
        '-c:a', 'aac', '-b:a', '192k', # кодирование аудио
        
        '-alpha_bits', '0', # Possible values are 0, 8 and 16. Use 0 to disable alpha plane coding.
        
        '-reset_timestamps', '1',
        
        os.path.join(path_out, f'{name}.mov')
    ]
    # print(' '.join(args))
    subprocess.run(args, shell=True, check=True)