import os
import requests
from datetime import datetime
import vlc
import time
from gtts import gTTS

API_KEY = os.environ.get('OPEN_WEATHER_KEY')
url = f'https://api.openweathermap.org/data/2.5/onecall?lat=30.4377&lon=-84.2882&exclude=current,minutely,hourly,alert&units=imperial&appid={API_KEY}'

def main():
	resp = requests.get(url).json()
	today = resp['daily'][0]

	min_temp = int(today['temp']['min'])
	max_temp = int(today['temp']['max'])
	sunset = datetime.fromtimestamp(today['sunset']).strftime('%-I:%M')
	pop = int(today['pop'] * 100)
	description = today['weather'][0]['description']
	clouds = today['clouds']

	person = os.environ.get('WAKEUP_PERSON')
	if person is None:
		person = ''

	script = f"Good morning, {person}! Today's high is {max_temp} and low is {min_temp} degrees. The weather is {description} with a {pop} percent chance of rain. There is about {clouds} percent of cloud coverage. The sunset is at {sunset}. Enjoy your day!"

	print(today)
	print(script)

	speak(script)

def wait_for_player(player):
	good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]
	while str(player.get_state()) in good_states:
		time.sleep(5)

def speak(script):
	voice = gTTS(text=script, lang='en', slow=False)
	voice.save('/tmp/forecast.wav')

	player = vlc.MediaPlayer('/tmp/forecast.wav')
	player.audio_set_volume(100)
	player.play()
	wait_for_player(player)

if __name__ == '__main__':
	main()
