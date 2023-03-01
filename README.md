# bulk youtube link id to youtube playlist

This program may fulfill any need to bulk transfer Youtube links from wherever to a Youtube music/normal Youtube playlist.

You will need Python 3 and the 'ytmusicapi' library, which can be obtained via 'pip install ytmusicapi'.

You will need to change the name of the file '.env.sample' to just '.env', which will be provided to the main.py file for proper functionality of the program. Therefore, you will need to provide the new .env file with your Youtube User ID (help via https://support.google.com/youtube/answer/3250431?hl=en).

Your request headers can be obtained via music.youtube.com from the Network tab on the 'F12' inspect page. Once you have your request headers copied, you will need to setup the project with 'setup.py', which will generate a 'headers_auth.json' file after you paste in your request headers appropriately (help via https://ytmusicapi.readthedocs.io/en/stable/setup.html) and 'main.py' will then handle this information.

Then, you will use the video_ids.txt file to provide the program with any Youtube video IDs in list format from your Youtube links (one ID per line). These IDs will have to be isolated externally in bulk, which may be performed simply by using a spreadsheet program with relevant formulae (will change to internal possibly in the future).

Then run the program via 'python main.py' from the relevant path. Your playlist link will be provided as a print message.