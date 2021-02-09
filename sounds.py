import requests
import xml.etree.ElementTree as ET
import vlc
import time

def get_first_item(url):
	xml = requests.get(url).content
	root = ET.fromstring(xml)
	enclosure = root.find('channel').find('item').find('enclosure')
	return enclosure.attrib['url']

def wait_for_player(player):
	good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]
	while str(player.get_state()) in good_states:
		time.sleep(5)

def main():
	upfirst = get_first_item('https://feeds.npr.org/510318/podcast.xml')
	shortwave = get_first_item('https://feeds.npr.org/510351/podcast.xml')

	for audio in [upfirst, shortwave]:
		player = vlc.MediaPlayer(audio)
		player.play()

		wait_for_player(player)
		player.stop()

if __name__ == '__main__':
	main()
