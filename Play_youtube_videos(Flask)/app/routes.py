import flask 
from flask import request
from app import app
import pafy 
import vlc



@app.route('/home', methods=['GET'])
def Home():
    return 'Here you can play any music video you like from Youtube.'


@app.route('/PlayMusic', methods=['GET'])
def play():
    if 'url' in request.args:
        url = str(request.args['url'])
    else:
        return "Error: No url field provided. Please specify url."
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url

    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    return playurl.de
