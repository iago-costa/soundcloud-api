# from sclib.asyncio import SoundcloudAPI, Track, Playlist

# api = SoundcloudAPI()
# playlist_url = 'https://soundcloud.com/carla-ferraz-2/sets/musica-de-rezo'

# playlist = await api.resolve(playlist_url)

# assert type(playlist) is Playlist

# for track in playlist.tracks:
#     filename = f'./{track.artist} - {track.title}.mp3'
#     with open(filename, 'wb+') as fp:
#         await track.write_mp3_to(fp)


from soundcloud_lib.sclib import SoundcloudAPI, Track, Playlist
import os
import logging
from dotenv import load_dotenv

load_dotenv()
PLAYLIST_URL = os.environ['PLAYLIST_URL']

api = SoundcloudAPI()
playlist = api.resolve(PLAYLIST_URL)

assert isinstance(playlist, Playlist)

playlist_folder = f'.downloaded_folders/{playlist.title} - {playlist.id}'

if os.path.isdir(playlist_folder):
    print('Folder already exists')
    logging.error('Folder %s already exists', playlist_folder)
else:
    print('Creating folder')
    os.mkdir(playlist_folder)
    
logging.basicConfig(
    filename=f'{playlist_folder}/------exceptions.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)

for track in playlist.tracks:
    try:
        filename = f'{playlist_folder}/{track.artist} - {track.title}.mp3'
        if not os.path.isfile(filename):
            with open(filename, 'wb+') as fp:
                track.write_mp3_to(fp)
        else:
            logging.info('File %s already exists', filename)
    except Exception as e:
        logging.exception('Error: %s', e)