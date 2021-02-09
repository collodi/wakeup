import requests
import xml.etree.ElementTree as ET
import vlc
import time
from datetime import datetime

def get_first_item(url):
	xml = requests.get(url).content
	root = ET.fromstring(xml)
	enclosure = root.find('channel').find('item').find('enclosure')
	return enclosure.attrib['url']

def wait_for_player(player):
	good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]
	while str(player.get_state()) in good_states:
		time.sleep(5)

def get_day():
	return datetime.today().strftime('%a')

def get_upfirst():
	# no upfirst on sundays
	if get_day() == 'Sun':
		return None

	return get_first_item('https://feeds.npr.org/510318/podcast.xml')

def get_shortwave():
	# no shortwave on sats, suns
	if get_day() in ['Sat', 'Sun']:
		return None

	return get_first_item('https://feeds.npr.org/510351/podcast.xml')

def main():
	upfirst = get_upfirst()
	shortwave = get_shortwave()

	for audio in [upfirst, shortwave]:
		if audio is None:
			continue

		player = vlc.MediaPlayer(audio)
		player.play()

		wait_for_player(player)
		player.stop()

if __name__ == '__main__':
	main()
