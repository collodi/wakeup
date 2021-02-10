import vlc
import time

def main():
	url = 'https://mp3stream.wfsu.org:8443/889hi'
	player = vlc.MediaPlayer(url)
	player.play()

	for i in range(100):
		player.audio_set_volume(i)
		time.sleep(2.4)

	player.audio_set_volume(100)
	time.sleep(60)

if __name__ == '__main__':
	main()
