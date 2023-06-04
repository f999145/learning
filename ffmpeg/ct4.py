from pathlib import Path
import subprocess
from textwrap import shorten

# path_to_folder = Path('a:\\')
path_to_folder = Path.cwd()
file_list = list(path_to_folder.iterdir())
print()
for index, item in enumerate(file_list):
    print(f'{index:02} {item.name}')
print('-'*80)
while True:
    try:
        number = int(input('\nВведите номер файла: '))
        break
    except ValueError:
        while True:
            match input('не число, повторить? (y/n):'):
                case 'y':
                    break
                case 'n':
                    exit()
                case _:
                    continue
            
    
video = file_list[number]

print(f'\nvideo file:\n\t{video.name}')

name = video.name.replace(video.suffix, '')
symbols = ' .abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789'
name = ''.join(filter(lambda x: x if x.lower() in symbols else '', name)).replace('.', ' ')

out_name = shorten(name, 40, placeholder='').replace(' ', '_') + '_out' + '.mp4'
out_file = path_to_folder.joinpath(out_name)
print('-'*80)
print(f'\nout file: \n\t{out_file}')

 
if not input('\nПродолжить? (enter)') == '':
    exit()

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
    '-b:v', '8M',
    
    '-af', "pan=stereo|FL < 0.7*FC + 0.3*FLC + 0.3*FL + 0.3*BL + 0.3*SL + 0.5*LFE | FR < 0.7*FC + 0.3*FRC + 0.3*FR + 0.3*BR + 0.3*SR + 0.5*LFE", #'loudnorm'
    '-ar', '48000',
    '-c:a', 'aac', '-b:a', '192k',
    # '-c:a', 'libmp3lame', '-b:a', '192k',
    # '-c:a', 'ac3',
    
    '-c:s', 'mov_text',
    
    out_file
]
subprocess.run(args, shell=True, check=True)