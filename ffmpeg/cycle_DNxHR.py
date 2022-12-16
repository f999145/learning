import os
import subprocess

# path = os.path.join('/','mnt', 'test', 'youtube') 
path = os.path.join('a:\\', 'youtube') 
files = []
for dirpath, dirname, filenames in (os.walk(path)):
    for file in filenames:
        files.append(os.path.join(dirpath, file))

if not os.path.isdir(os.path.join(path, 'out')):
    os.mkdir(os.path.join(path, 'out'))

for file in files:
    """multi = 5.375
    """
    name, ext = os.path.splitext(os.path.basename(file))
    args =[
        'ffmpeg', '-y', 
        
        '-i', file,
            
        '-vf', 'scale=-1:1440', # Specify the Height To Retain the Aspect Ratio
                                # https://ottverse.com/change-resolution-resize-scale-video-using-ffmpeg/
        
        # '-r', '24',             # frame rate
        
        '-c:v', 'dnxhd',        # FFmpeg contains two ProRes encoders, the prores-aw and prores-ks encoder.
                                # You can choose the encoder you want using the -vcodec option.
        
        '-profile:v', 'dnxhr_lb',  
                                    # DNxHR LB: dnxhr_lb - Low Bandwidth. 8-bit 4:2:2 (yuv422p). Offline Quality.
                                    # DNxHR SQ: dnxhr_sq - Standard Quality. 8-bit 4:2:2 (yuv422p). Suitable for delivery format.
                                    # DNxHR HQ: dnxhr_hq - High Quality. 8-bit 4:2:2 (yuv422p).
                                    # DNxHR HQX: dnxhr_hqx - High Quality. 10-bit 4:2:2 (yuv422p10le). UHD/4K Broadcast-quality delivery.
                                    # DNxHR 444: dnxhr_444 - Finishing Quality. 10-bit 4:4:4 (yuv444p10le). Cinema-quality delivery.
        
        '-c:a', 'aac', '-b:a', '192k', # кодирование аудио
        
        '-alpha_bits', '0', # Possible values are 0, 8 and 16. Use 0 to disable alpha plane coding.
        
        os.path.join(path, 'out', f'{name}.mov')
    ]
    # print(' '.join(args))
    subprocess.run(args, shell=True, check=True)