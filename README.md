# bulk youtube link id to youtube playlist

## Dependencies
You will need Python 3 and the 'ytmusicapi' library, which can be obtained via 'pip install ytmusicapi'.

## Setup
Follow this guide to get your auth headers and fill in browser.json, required for yt music auth
https://ytmusicapi.readthedocs.io/en/stable/setup/browser.html

## Input data

Use the video_ids.txt file to provide the tool with any Youtube video IDs in list format from your Youtube links (one ID per line) 

You may also edit the playlist name, description, and visibility inside the 'main.py' file. 

## Output link

Run main.py when all is good. Your playlist link will be provided as a print message.