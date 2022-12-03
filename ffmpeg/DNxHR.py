import os
import subprocess

name = 'THE CALLISTO PROTOCOL 02'

path = os.path.join('a:\\', 'youtube')

vdict = {'res': 'webm', 'video_id': 3, 'audio_id': 21}

# Кодирование в Apple DNxHD
args =[
    'ffmpeg', '-y', 
    
    '-ss', '01:00:00', # '-to', '02:00:00', # вырезать фрагмент видео
    
    '-i', (os.path.join(path, name + "." + vdict['res'])),
        
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
    
    # '-pix_fmt', 'yuv422p',  # 8-bit 4:2:0: yuv420p
                                # 8-bit 4:2:2: yuv422p
                                # 8-bit 4:4:4: yuv444p
                                # 10-bit 4:2:0: yuv420p10le
                                # 10-bit 4:2:2: yuv422p10le
                                # 10-bit 4:4:4: yuv444p10le 
    
    # 
    # '-f', 'segment', # делить видео на фрагменты
    # '-segment_time', '00:02:00', 
    # '-reset_timestamps', '1',
    # '"' + os.path.join(path, name +' output%03d'+".mov") + '"'
    
    os.path.join(path, name +' output'+".mov")
]
# print(' '.join(args))
subprocess.run(args, shell=True, check=True)