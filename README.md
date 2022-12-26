### Soundcloud Playlist Downloader with Python without ID or App from API Soundcloud

#### Install soundcloud-lib

>**1.** If install soundcloud-lib with pip, you get an error
403 Client Error: Forbidden for url: https://api-v2.soundcloud.com/playlists/...

>**2.** So you have to download the source code from github and install it manually: 
Page pypi to package: https://pypi.org/project/soundcloud-lib/

>**3.** In this project already the source code is downloaded but if you got some problems with the execution, you can download it manually
``` sh
$ git clone https://github.com/3jackdaws/soundcloud-lib.git
```

#### Prepare environment

>**1.** Use conda to create a new environment with python 3.10.8
``` sh
$ conda create -n py3108 python=3.10.8
```

>**2.** Activate the environment and install python-dotenv
``` sh
$ conda activate py3108
$ pip install --upgrade pip
$ pip install python-dotenv
```

>**3.** Deactivate the environment
``` sh
$ conda deactivate
```

#### Create .env file

>**1.** Set in file .env:
**PLAYLIST_URL=https://soundcloud.com/playlist/...**


#### Run script

``` sh
$ python playlist_downloader.py
```