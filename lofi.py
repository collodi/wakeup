import vlc
import pafy
import time

def main():
	url = 'https://www.youtube.com/watch?v=5yx6BWlEVcY&t=0s'
	video = pafy.new(url)
	player = vlc.MediaPlayer(video.getbest().url, ':no-video')
	player.play()

	for i in range(100):
		player.audio_set_volume(i)
		time.sleep(2.4)

	player.audio_set_volume(100)
	time.sleep(60)

if __name__ == '__main__':
	main()
