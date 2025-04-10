from ytmusicapi import YTMusic
ytmusic = YTMusic("browser.json")

with open('input_video_ids.txt', 'r') as f:
    lines = f.readlines()
    videoIds = [line.strip() for line in lines]

def get_valid_video_ids(ytmusic, videoIds):
    valid_video_ids = []
    try:
        for video_id in videoIds:
            search_results = ytmusic.search(query=video_id, filter='videos')
            if search_results:
                video = search_results[0]
                if video.get('videoId') == video_id:
                    valid_video_ids.append(video_id)
                    print("appended valid id\n")
    except Exception as e:
        print(f"error appending\n")
    return valid_video_ids

valid_video_ids = get_valid_video_ids(ytmusic, videoIds)
with open('valid_video_ids.txt', 'w') as f:
    for video_id in valid_video_ids:
        f.write(video_id + '\n')
