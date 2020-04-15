from os import path
from os.path import exists
from os import mkdir
from pythonopensubtitles.opensubtitles import OpenSubtitles
from pythonopensubtitles.utils import File
from videoobject import VideoObject
from functions import find_most_downloaded


def main():
    # Input for the series name season and episode
    series = input("Series name: ")
    season = input("Season number: ")
    episode = input("Episode Number: ")
    # Append 0 at the start if they are only one-digit numbers
    if len(season) == 1:
        season = '0' + season
    if len(episode) == 1:
        episode = '0' + episode
    vo = VideoObject(series, season, episode)

    # Create directory Subs if it doesn't exist
    if not path.exists('Subs'):
        mkdir('Subs')
        print("Directory Subs created successfully")
    else:
        print("Directory Subs exists")
    
    # Login to opensubtitles.org through the API
    print("Logging in...")
    ost = OpenSubtitles()
    ost.login(vo.username, vo.password)

    print("Searching subtitles...")
    #Search the subtitles by name
    data = ost.search_subtitles([{
        'sublanguageid': 'eng',
        'query': series,
        'season': season,
        'episode': episode
    }])

    print('data length: ' + str(len(data)))

    # Subtitle file ID, used for setting the correct name in the dictionary
    subtitle_file_id = find_most_downloaded(data)

    # Downloads the subtitle file to the \subs folder
    print("Downloading to .\\Subs...")
    filenames = {
        str(subtitle_file_id): vo.name + ' - S' + vo.season + 'E' + vo.episode + '-eng.srt'
    }
    ost.download_subtitles([subtitle_file_id], output_directory='.\\Subs\\', override_filenames=filenames, extension='srt')
    print("Success! :)")
    ost.logout()


if __name__ == "__main__":
    main()