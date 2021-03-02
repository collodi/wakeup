import os
import asyncio
from kasa import SmartDimmer

KASA_DIMMER_ADDR = os.environ.get('KASA_DIMMER_ADDR')

async def main():
	d = SmartDimmer(KASA_DIMMER_ADDR)
	await d.update()

	await d.turn_on()
	await d.set_brightness(0)
	await d.update()

	await d.set_dimmer_transition(100, 5 * 60 * 1000)
	await d.update()

if __name__ == '__main__':
	asyncio.run(main())
