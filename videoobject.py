from os import path

class VideoObject(object):
    username = 'Ocelaw'
    password = 'EThan6627084'
    name = ''
    season = ''
    episode = ''

    def __init__(self, name, season, episode):
        self.name = name
        self.season = season
        self.episode = episode