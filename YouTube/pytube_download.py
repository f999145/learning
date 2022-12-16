import os
from pytube import YouTube
import subprocess

link = 'https://youtu.be/ZfN8nG0luig'

name = 'THE TEST'

resolution="2160"

path = os.path.join('./', 'youtube')

def connect_to_stream():
    print()
    print('connect to stream...', end='')
    yt = YouTube(link,
                # use_oauth=True
                )
    videos = yt.streams
    print('done')
    print()
    return videos

 
def create_video_dict():
    
    video = {}
    audio = {}
    if videos:
        print('finde stream...', end='')
        for index, item in (enumerate(videos)):
            item = str(item)
            if resolution in item:
                if 'mp4' in item:
                    video['mp4'] = index   
                else:
                    video['webm'] = index
            if 'audio' in item:
                if 'mp4' in item:
                    item = item.split(' ')
                    abr = int(item[3][5:-5])
                    if not 'mp4' in audio:
                        audio['mp4'] = {
                            'id':index,
                            'abr':abr
                        } 
                    elif audio['mp4']['abr'] < abr:
                        audio['mp4'] = {
                            'id':index,
                            'abr':abr
                        }       
                else:
                    item = item.split(' ')
                    abr = int(item[3][5:-5])
                    if not 'webm' in audio:
                        audio['webm'] = {
                            'id':index,
                            'abr':abr
                        } 
                    elif audio['webm']['abr'] < abr:
                        audio['webm'] = {
                            'id':index,
                            'abr':abr
                        }
        if 'mp4' in video:
            vdict = {
                'res':'mp4',
                'video_id': video['mp4'],
                'audio_id': audio['mp4']['id']
                }
        else:
            vdict = {
                'res':'webm',
                'video_id': video['webm'],
                'audio_id': audio['webm']['id']
                }
        print('  done')
        print('Stream:',vdict)
        print(round((videos[vdict['video_id']].filesize + videos[vdict['audio_id']].filesize)/(1024*1024*1024), 2),'GB')
        return vdict
    else:
        print('Нет данных')
    print()

def load_yt_files():
    if videos:
        print('download video...')
        video_print = videos[vdict['video_id']].download(output_path=path, filename='_video.' + vdict['res'])
        print(video_print)
        audio_print = videos[vdict['audio_id']].download(output_path=path, filename='_audio.' + vdict['res'])
        print(audio_print)
        print('complete')
        print()

def join_audio_and_video():
    if videos:
        print('join video and audio')
        args = [
            'ffmpeg',
            '-y',
            '-i',
            os.path.join(path, "_video."+ vdict['res']),
            '-i',
            os.path.join(path, "_audio."  + vdict['res']),
            '-c',
            'copy',
            str(os.path.join(path, name + "." + vdict['res']))
        ]
        subprocess.run(args, capture_output=True)
        print('comlete')
        print()
        
        
def delete_tmp():
    if videos:
        # Удаляем файлы
        os.remove(os.path.join(path, "_video." + vdict['res']))
        os.remove(os.path.join(path, "_audio." + vdict['res']))
        print('remove tmp files')
        
if __name__ == '__main__':
    videos = connect_to_stream()
    vdict = create_video_dict()
    load_yt_files()
    join_audio_and_video()
    delete_tmp()
    
    
    