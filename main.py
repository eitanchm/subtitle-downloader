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

    print("Downloading all subs...")
    # Search and download subtitles for all videos
    for video in video_list:
        print("Downloading " + video.search_name + " S" + video.season + " E" + video.episode + "Subs")
        # Creates a list of all the searched subtitles
        search_data = ost.search_subtitles([{
            'sublanguageid': 'eng',
            'query': video.search_name.lower(),
            'season': video.season,
            'episode': video.episode
        }])
        # Finds subtitle file ID of most downloaded subtitles file
        subtitle_file_id = find_most_downloaded(search_data)
        ost.download_subtitles([subtitle_file_id], output_directory='.\\Subs\\',
                               override_filenames={str(subtitle_file_id): video.file_name + '-eng.srt'},
                               extension='srt')
    
    print("Done!")

    print("Logging out...")
    ost.logout()


if __name__ == "__main__":
    main()