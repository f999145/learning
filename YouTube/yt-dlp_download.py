import os
from pytube import YouTube
from textwrap import shorten
import subprocess

link = '''

https://www.youtube.com/watch?v=hF66c3Xq_IM

'''.strip()

resolution="1080"

path = os.path.join('c:\\', 'youtube')

if ('youtu' in link.split('/', maxsplit=3)[-2]):
    yt = YouTube(link,
                    # use_oauth=True
                    )

    title = str(yt.title)
    symbols = '<>=#@`~^&{}[]:,"\'/\|?*'

    for s in symbols:
        title = title.replace(s,'')

    name = shorten(title, width=40, placeholder='')
else:
    name = '%(title)s'

ytdlp_args = [
    'yt-dlp', '-f',
    f'bv[height<={resolution}]+ba/b[height<={resolution}]',
    link,
    # '-P', path
    '-o', os.path.join(path, f'{name}.%(ext)s')
]

os.makedirs(path, exist_ok=True)
subprocess.run(ytdlp_args)
