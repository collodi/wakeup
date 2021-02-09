import vlc
import time

def main():
	url = 'https://mp3stream.wfsu.org:8443/889hi'
	player = vlc.MediaPlayer(url)
	player.play()

	for i in range(50):
		player.audio_set_volume(i * 2)
		time.sleep(6)

	player.audio_set_volume(100)
	time.sleep(60)

if __name__ == '__main__':
	main()
