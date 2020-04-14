from os import path
from os.path import exists
from os import mkdir
from pythonopensubtitles.opensubtitles import OpenSubtitles
from pythonopensubtitles.utils import File
from videoobject import VideoObject

korra = VideoObject(
    'Korra',
    '01',
    '01',
    'C:\\Users\\eitan\\Downloads\\The Legend of Korra (2012) Season 3 S03 + Extras (1080p BluRay x265 HEVC 10bit AAC 5.1 RCVR) REPACK',
    'The Legend of Korra (2012) - S03E03 - The Earth Queen (1080p BluRay x265 RCVR).mkv'
)

series = input("Series name: ")
season = input("Season number: ")
episode = input("Episode Number: ")

if len(season) == 1:
    season = '0' + season
if len(episode) == 1:
    episode = '0' + episode

print('season - ' + season)
print('episode - ' + episode)

if not path.exists('Subs'):
    mkdir('Subs')
    print("Directory Subs created successfully")
else:
    print("Directory Subs exists")

print("Logging in...")

ost = OpenSubtitles()
token = ost.login('Ocelaw', 'EThan6627084')
assert type(token) == str

#f = File(path.join(korra.path, korra.video))
#hash = f.get_hash()
#assert type(hash) == str

#size = f.size
#assert type(size) == str

print("Searching subtitles...")

#data = ost.search_subtitles([
#    {
#        'sublanguageid': 'eng',
#        'moviehash': hash,
#        'moviebytesize': size
#    }
#])

#if len(data) == 0:
#    print("Failed to find Subtitles, trying to find by name")
#    data = ost.search_subtitles([
#        {
#            'sublanguageid': 'eng',
#            'query': series,
#            'season': season,
#            'episode': episode
#        }
#    ])
#else:
#    print("Subtitles found, information for debugging:")

data = ost.search_subtitles([
    {
        'sublanguageid': 'eng',
        'query': series,
        'season': season,
        'episode': episode
    }
])

id_subtitle = data[0].get('IDSubtitle')
id_subtitle_file = data[0].get('IDSubtitleFile')
id_sub_movie_file = data[0].get('IDSubMovieFile')
assert type(data) == list
print(id_subtitle + ', '  + id_subtitle_file + ', ' + id_sub_movie_file)

print("Downloading to .\\Subs...")

filenames = {
    str(id_subtitle_file): series + ' - S' + season + 'E' + episode + '-eng.srt'
}

ost.download_subtitles([id_subtitle_file], output_directory='.\\Subs\\', override_filenames=filenames, extension='srt')

print("Success! :)")

ost.logout()