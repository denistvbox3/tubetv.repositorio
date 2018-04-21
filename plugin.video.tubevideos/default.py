# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/virtual0135
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import os
import sys
import time
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.tubevideos'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
#icon = local.getAddonInfo('icon')

icon = "https://vignette.wikia.nocookie.net/capcomdatabase/images/c/c0/SFV_Logo.png/revision/latest?cb=20150415000109"
icon2 = "https://lh3.googleusercontent.com/tDww2ZaqSITWO0jfB-lS1YTads3G2S7BZdqCD9J2U0Dl5Ui-NzvIvn63wrxK-1QNepndmzuXq8UBPg=w330-h330-n-o-rw"
icon3 = "http://www.iconarchive.com/download/i60373/graphics-vibe/classic-3d-social/youtube.ico"
icon4 = "http://kultme.com.br/kt/wp-content/uploads/2016/09/musica.jpg"

addonfolder = local.getAddonInfo('path')
resfolder = addonfolder + '/resources/'
entryurl=resfolder+"entrada.mp4"
YOUTUBE_CHANNEL_ID  = "virtual0135"
YOUTUBE_CHANNEL_ID2 = "UC1JHuR3Gz7LiTo089N1nSLg"
YOUTUBE_CHANNEL_ID3 = "tdQR8GNUE_k"
YOUTUBE_CHANNEL_ID4 = "PL66lEUUDdrxW3pqe27U6lnyvi3JxVZT9e"


# Ponto de Entrada
def run():
	# Pega Parâmetros
	params = plugintools.get_params()
	
	if params.get("action") is None:
		xbmc.Player().play(entryurl)
		
		while xbmc.Player().isPlaying():
			time.sleep(1)

		main_list(params)
	else:
		action = params.get("action")
		exec action+"(params)"

	plugintools.close_item_list()

# Menu Principal
def main_list(params):
	plugintools.log("tubevideos.main_list "+repr(params))
	
	plugintools.log("tubevideos.run")
	
	#plugintools.direct_play(str(entryurl))

plugintools.add_item(
		title = "arcade collection",
		url = "plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID+"/",
		thumbnail = icon,
		folder = True )
plugintools.add_item(
		title = "Meu canal",
		url = "plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID2+"/",
		thumbnail = icon2,
		folder = True )
plugintools.add_item(
		title = "youtube",
		url = "plugin://plugin.video.youtube/?path=/root/video&amp;action=play_video&amp;videoid="+YOUTUBE_CHANNEL_ID3+"/",
		thumbnail = icon3,
		folder = True )
plugintools.add_item(
		title = "Minha Playlist",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID4+"/",
		thumbnail = icon4,
		folder = True )		

run()