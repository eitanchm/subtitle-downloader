from os import path

class VideoObject(object):
    username = 'Ocelaw'
    password = 'EThan6627084'
    name = ''
    season = ''
    episode = ''
    path = ''
    video = ''

    def __init__(self, name, season, episode, path, video):
        self.name = name
        self.season = season
        self.episode = episode
        self.path = path
        self.video = video