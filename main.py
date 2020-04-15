from pythonopensubtitles.opensubtitles import OpenSubtitles
from pythonopensubtitles.utils import File
from videoobject import VideoObject

from functions import *


def main():
    # Run the program in current directory
    # Get login details from user
    ( username, password ) = get_login_credentials()
    
    # The OpenSubtitles object
    ost = OpenSubtitles()

    # Login to opensubtitles.org through the API
    print("Logging in...")
    while ost.login(username, password) is None:
        print("Login failed, try again.")
        ( username, password ) = get_login_credentials()
    
    # Creates the Subs directory if it doesn't exist
    create_subs_dir()
    # Gets a list of all the video file names in the directory (.mp4 or .mkv)
    filename_list = get_video_filenames()
    video_list = to_video_object_list(filename_list)

    for video in video_list:
        print("series: " + video.search_name + " season: " + video.season + " episode: " + video.episode)
    
    ost.logout()

    """
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
    """


if __name__ == "__main__":
    main()