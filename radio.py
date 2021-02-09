import vlc
import time

def main():
	url = 'https://mp3stream.wfsu.org:8443/889hi'
	player = vlc.MediaPlayer(url)
	player.play()

	for i in range(70):
		player.audio_set_volume(30 + i)
		time.sleep(3)

	player.audio_set_volume(100)
	time.sleep(60)

if __name__ == '__main__':
	main()
