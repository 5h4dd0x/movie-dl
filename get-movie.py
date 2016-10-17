#! /usr/bin/python3

# automated youtube downloader.
# reads contents of clipbard and passes it to youtube-dl,
# and downloads it into the ~/movies directory.
# possibly more as time goes on.

import pyperclip, os, youtube_dl

home = os.path.expanduser('~')
os.chdir(home + '/movies')
ydl_opts = {
    'output': '%(title)s/%(title)s.%(ext)s',
    'restrict-filenames': '',
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([pyperclip.paste()])