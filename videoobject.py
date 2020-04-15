from os import path

class VideoObject(object):
    file_name = ''
    search_name = ''
    season = ''
    episode = ''

    def __init__(self, file_name):
        self.file_name = file_name
        self.find_search_name()
        self.find_season()
        self.find_episode()


    def find_search_name(self):
        # Finds the name of the movie / series and keeps the data in
        # self.search_name
        for i in range(len(self.file_name)):
            if self.file_name[i] == '(':
                self.search_name = self.file_name[0:i-1]
                if self.search_name[len(self.search_name) - 1] == ' ':
                    self.search_name = self.search_name.rstrip()
                break
    
    
    def find_season(self):
        # Finds the season number and keeps it as a string in self.season
        for i in range(len(self.search_name), len(self.file_name)):
            if (self.file_name[i] == 'S' and
                self.file_name[i + 1] >= '0' and self.file_name[i + 1] <= '9' and
                self.file_name[i + 2] >= '0' and self.file_name[i + 2] <= '9'):
                self.season += self.file_name[i + 1]
                self.season += self.file_name[i + 2]
                break
    

    def find_episode(self):
        # Finds the episode number and keeps it as a string in self.episode
        for i in range(len(self.search_name), len(self.file_name)):
            if (self.file_name[i] == 'E' and
                self.file_name[i + 1] >= '0' and self.file_name[i + 1] <= '9' and
                self.file_name[i + 2] >= '0' and self.file_name[i + 2] <= '9'):
                self.episode += self.file_name[i + 1]
                self.episode += self.file_name[i + 2]
                break

