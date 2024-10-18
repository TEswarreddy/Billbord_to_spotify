import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:1234",
        client_id= "c7fa9d72a40747d9a0557451f43e80a0",
        client_secret="ccf184967bbd4f4eb0e640f74eb318fb",
        show_dialog=True,
        cache_path="token.txt",
        username="Thathieswarreddy", 
    )
)
user_id = sp.current_user()["id"]



date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
URL = "https://www.billboard.com/charts/hot-100/"+date
response = requests.get(url=URL,headers= header)
web_page = response.text
soup = BeautifulSoup(web_page,"html.parser")
song_names_title = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_title]

for song in song_names:
    print(song)
