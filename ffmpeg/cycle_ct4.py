from pathlib import Path
import subprocess
from textwrap import shorten

# path_to_folder = Path('a:\\')
path_to_folder = Path.cwd()
out_dir = Path.joinpath(path_to_folder, 'out')
out_dir.mkdir(exist_ok=True)
file_list = list(path_to_folder.iterdir())

videosuffix = ['.mkv', '.mp4']
new_file_list: list[Path] = []

for index, item in enumerate(file_list):
    if item.suffix in videosuffix:
        new_file_list.append(item)        


for video in new_file_list:

    print(f'\nvideo file:\n\t{video.name} \n')

    name = video.name.replace(video.suffix, '')
    symbols = ' _.abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789'
    name = ''.join(filter(lambda x: x if x.lower() in symbols else '', name)).replace('.', ' ')

    out_name = shorten(name, 40, placeholder='').replace(' ', '_') + '_out' + '.mp4'
    out_file = out_dir.joinpath(out_name)


    args = [
        'ffmpeg', '-y',
        '-i', video,
        
        '-map', '0',
        # '-map', '0:a',
        # '-map', '0:s',
        
        '-vf', 'scale=1920:-1',
        '-c:v', 'h264_nvenc',
        '-preset', 'fast',
        '-profile:v', 'main',
        '-level', '4.2',
        # '-cbr', 'true',
        '-b:v', '6M',
        
        '-af', "pan=stereo|FL < 0.7*FC + 0.3*FLC + 0.3*FL + 0.3*BL + 0.3*SL + 0.5*LFE | FR < 0.7*FC + 0.3*FRC + 0.3*FR + 0.3*BR + 0.3*SR + 0.5*LFE, loudnorm",
        '-ar', '48000',
        '-c:a', 'aac', '-b:a', '192k',
        # '-c:a', 'libmp3lame', '-b:a', '320k',
        # '-c:a', 'ac3',
        
        '-c:s', 'mov_text',
        
        out_file
    ]
    subprocess.run(args, shell=True, check=True)
    video.unlink(True)