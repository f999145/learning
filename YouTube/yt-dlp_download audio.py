import os
import subprocess

link = '''
https://vk.com/audio229404382_456239903_981fe845e5a0ce7db1
'''.strip()

path = os.path.join('a:\\', 'youtube')

ytdlp_args = [
    'yt-dlp', '-f',
    
    'ba',
    '-x', '--audio-format', 'mp3',
    link,
        
    
    '-o', os.path.join(path, r'%(title)s.%(ext)s')
]

os.makedirs(path, exist_ok=True)
subprocess.run(ytdlp_args)
