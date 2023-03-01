# youtube link to youtube playlist

This program may fulfill any need to bulk transfer Youtube links from wherever to a Youtube music/normal Youtube playlist.

You will need Python 3 and the 'ytmusicapi' library, which can be obtained via the following pip command:

pip install ytmusicapi

You will need to change the name of the file '.env.sample' to just '.env', which will be provided to the main.py file for proper functionality of the program. Therefore, you will need to provide the new .env file with your Youtube User ID (help via https://support.google.com/youtube/answer/3250431?hl=en) and your request headers via music.youtube.com from the Network tab on the 'F12' inspect page. 

Once in the Network tab you will need to filter the requests with method:POST and find a request with a status of 200 in the domain of music.youtube.com. Once found, right click this request and copy the request headers. Paste these request headers in the HEADERS={''} variable and main.py will convert these into JSON for use in the Youtube API.

Then, you will use the video_ids.txt file to input any Youtube video IDs from any Youtube links in list format (one ID per line) these IDs may be isolated in bulk simply by using a spreadsheet program.

Then run the program.