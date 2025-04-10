from ytmusicapi import YTMusic
ytmusic = YTMusic("browser.json")

playlist_name = 'INPUT HERE'
playlist_description = 'INPUT DESCRIPTION HERE'

playlistId = ytmusic.create_playlist(playlist_name, playlist_description)

with open('video_ids.txt', 'r') as f:
        lines = f.readlines()
        videoIds = [line.strip() for line in lines]

ytmusic.add_playlist_items(playlistId, videoIds)
print("Created playlist '" + playlist_name + "':" + "\"\n" + "https://music.youtube.com/playlist?list=" + playlistId)