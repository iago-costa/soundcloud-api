
#### install soundcloud-lib

if install soundcloud-lib with pip, you get an error
403 Client Error: Forbidden for url: https://api-v2.soundcloud.com/playlists/...

so you have to download the source code from github and install it manually
https://pypi.org/project/soundcloud-lib/


in this project already the source code is downloaded but if you got some problems with the execution, you can download it manually


#### Prepare environment

> use conda to create a new environment with python 3.10.8
``` sh
$ conda create -n py3108 python=3.10.8
```

> activate the environment and install python-dotenv
``` sh
$ conda activate py3108
$ pip install --upgrade pip
$ pip install python-dotenv
```


> deactivate the environment
``` sh
$ conda deactivate
```


#### create .env file

set in file .env

PLAYLIST_URL=https://soundcloud.com/playlist/...


#### run script

``` sh
$ python playlist_downloader.py
```