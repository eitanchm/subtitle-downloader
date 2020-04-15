import os
from os import path, mkdir, listdir
from os.path import exists
from getpass import getpass
from videoobject import VideoObject
from pythonopensubtitles.opensubtitles import OpenSubtitles


def find_most_downloaded(search_data):
    # Returns the subtitle file ID of the most downloaded subtitles file from
    # the list of found subtitles with search subtitles function.
    count = 0
    sub_file_ID = None
    for i in search_data:
        if int(i.get('SubDownloadsCnt')) > count:
            count = int(i.get('SubDownloadsCnt'))
            sub_file_ID = i.get('IDSubtitleFile')
    return sub_file_ID


def create_subs_dir():
    # Create directory Subs if it doesn't exist
    if not path.exists('Subs'):
        mkdir('Subs')
        print("Directory Subs created successfully")
    else:
        print("Directory Subs exists")


def get_login_credentials():
    # Inputs login credentials to opensubtitles.org from the user
    username = input("Enter opensubtitles.org username: ")
    password = getpass("Enter opensubtitles.org password: ")
    return (username, password)


def get_video_filenames():
    # Scans the directory for all the video files (currently mp4 and mkv files)
    files = []
    for file in os.listdir('.'):
        if file.endswith('.mp4') or file.endswith('.mkv'):
            files.append(file)
    return files


def to_video_object_list(file_list):
    # Turns the video file names to instances of VideoObject from videoobject.py
    video_list = []
    for file in file_list:
        video_list.append(VideoObject(file))
    return video_list
