#ffmpeg Test
''' 
    This is a simple python program that uses pytube and ffmpeg module to download Youtube videos upto 
    8K resolution and concatinate them to make a single video file. You do not need to use a 3rd paty 
    video mixing software. The finale video concatinaton time will depend on your computers processing power
    and the maximum resolution of the video file.
    
    Disclaimer: Some video files may not be available in your region due to restrictions.
    created by : Anil Yadav
    '''

# https://www.youtube.com/watch?v=H0Edsuw9FmM&ab_channel=PlayStationPlayStationVerified

from pytube import YouTube
import ffmpeg
import os
import glob

vlink = input('Video Link:')
v = YouTube(vlink)
print(f'downloading {v.title}')

# Downloading Audio and Video files And concatinating them using ffmpeg module
try:
    vid = ffmpeg.input(v.streams.filter(adaptive= True).first().download(filename_prefix='vid'))
    aud = ffmpeg.input(v.streams.get_audio_only().download(filename_prefix='aud'))
    ffmpeg.concat(vid,aud,v=1,a=1).output(f'{v.title}.mp4').run()
except:
    exist = glob.glob('*.mp4')
    if f'{v.title}'in exist:
        print('file already exist')
    else:
        print('Unable to download file')

# Delete Audio and Video files after the concatination
vfiles = glob.glob('vid*.mp4')
afiles = glob.glob('aud*.mp4')
files = vfiles+afiles
delete  = [x for x in files if f'{v.title}' not in x]

for filename in delete:
    try:
        os.remove(filename)
    
    except:
        print('file not found')