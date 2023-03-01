from ytmusicapi import YTMusic
import os

USER_ID = os.getenv('USER_ID')
HEADERS = os.getenv('HEADERS')

playlist_name = 'INPUT'
playlist_description = 'INPUT'

class YTvideoIDtoPlaylist:
    def __init__(self):
        self.api = YTMusic(f'{HEADERS}', f'{USER_ID}')

    def create_playlist(self, name, info, privacy="PRIVATE", tracks=None):
        return self.api.create_playlist(name, info, privacy, video_ids=tracks)

def main():
    ytmusic = YTvideoIDtoPlaylist()

    with open('video_ids.txt', 'r') as f:
        lines = f.readlines()
        videoIds = [line.strip() for line in lines]
        
    playlistId = ytmusic.create_playlist(playlist_name, playlist_description,'PRIVATE', videoIds)
    print("Success: created playlist \"" + playlist_name + "\"\n" +
            "https://music.youtube.com/playlist?list=" + playlistId)

if __name__ == "__main__":
    main()
