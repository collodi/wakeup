import vlc
import pafy
import time

def main():
	url = 'https://www.youtube.com/watch?v=5qap5aO4i9A'
	video = pafy.new(url)
	player = vlc.MediaPlayer(video.getbest().url, ':no-video')
	player.play()

	for i in range(93):
		player.audio_set_volume(i)
		time.sleep(2.7)

	time.sleep(60 * 3)

if __name__ == '__main__':
	main()
