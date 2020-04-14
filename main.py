from pythonopensubtitles.opensubtitles import OpenSubtitles
from pythonopensubtitles.utils import File
from os import path
from videoobject import VideoObject

korra = VideoObject('Korra', '01', '01', 'C:\\Users\\eitan\\Downloads\\The Legend of Korra (2012) Season 1 S01 + Extras (1080p BluRay x265 HEVC 10bit AAC 5.1 RCVR)', 'The Legend of Korra (2012) - S01E01 - Welcome to Republic City (1080p BluRay x265 RCVR).mkv')

ost = OpenSubtitles()
token = ost.login('Ocelaw', 'EThan6627084')
assert type(token) == str

f = File(path.join(korra.path, korra.video))
hash = f.get_hash()
assert type(hash) == str

size = f.size
assert type(size) == str

data = ost.search_subtitles([
    {
        'sublanguageid': 'eng',
        'moviehash': hash,
        'moviebytesize': size
    }
])

id_subtitle = data[0].get('IDSubtitle')
id_subtitle_file = data[0].get('IDSubtitleFile')
id_sub_movie_file = data[0].get('IDSubMovieFile')
assert type(data) == list

print(id_subtitle + ', '  + id_subtitle_file + ', ' + id_sub_movie_file)

ost.download_subtitles([id_subtitle_file], output_directory='.\\tmp', extension='srt')