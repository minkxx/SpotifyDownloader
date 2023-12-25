<h1 align="center">
  <b>Spotify Downloader</b>
</h1>

<b>A simple python script to download songs/albums/playlists from spotify.</b>

[![](https://img.shields.io/badge/SpotifyDownloader-v2.0-crimson)](#)
[![Stars](https://img.shields.io/github/stars/minkxx/SpotifyDownloader?style=flat-square&color=yellow)](https://github.com/minkxx/SpotifyDownloader/stargazers)
[![Forks](https://img.shields.io/github/forks/minkxx/SpotifyDownloader?style=flat-square&color=orange)](https://github.com/minkxx/SpotifyDownloader/fork)
[![Size](https://img.shields.io/github/repo-size/minkxx/SpotifyDownloader?style=flat-square&color=green)](https://github.com/minkxx/SpotifyDownloader/)   
[![Python](https://img.shields.io/badge/Python-v3.11.4-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-GPL-blue)](https://github.com/minkxx/SpotifyDownloader/blob/master/LICENSE) 

## Install and run
- Get your [Necessary Variables](#Necessary-Variables)
- create a file `config.py` and store them
- Clone the repository:    
`git clone https://github.com/minkxx/SpotifyDownloader.git`
- Go to the cloned folder:    
`cd SpotifyDownloader`
- Create a virtual env:      
`virtualenv -p /usr/bin/python3 myenv`
`. ./venv/bin/activate`
- Install the requirements:      
`pip(3) install -U -r requirements.txt`
- Run the script and enter spotify track/album/playlist link to download on `songs/` folder
- `pyhton spotifyDownloader.py`

## Necessary Variables
- `SPOTIFY_CLIENT_ID` - Spotify client_id. Get it from [here](https://developer.spotify.com/dashboard/)
- `SPOTIFY_CLIENT_SECRET` - Spotify client_secret. Get it from [here](https://developer.spotify.com/dashboard/)