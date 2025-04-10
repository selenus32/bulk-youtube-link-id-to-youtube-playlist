from ytmusicapi import YTMusic
import time
ytmusic = YTMusic("browser.json")

playlist_name = 'funky posts 3'
playlist_description = 'empty'

playlistId = ytmusic.create_playlist(playlist_name, playlist_description)

with open('valid_video_ids.txt', 'r') as f:
        lines = f.readlines()
        videoIds = [line.strip() for line in lines]

def add_video_ids_in_batches(ytmusic, playlistId, videoIds, batch_size=50, delay=1):
    for i in range(0, len(videoIds), batch_size):
        batch = videoIds[i:i+batch_size]
        try:
            ytmusic.add_playlist_items(playlistId, batch)
            print(f"Added batch {i // batch_size + 1} with {len(batch)} items.")
        except Exception as e:
            print(f"Error adding batch {i // batch_size + 1}: {e}")

add_video_ids_in_batches(ytmusic, playlistId, videoIds)
print(f"Created playlist '{playlist_name}':\nhttps://music.youtube.com/playlist?list={playlistId}")