lesezeichen = 0

# python chat programm
name = "Lesezeichenbot"

# Bot programm
def sprich(zeile):
	global lesezeichen #markiert, dass man auf die globale Variable zugreift

	lesezeichen += 1 # erhoehe Lesezeichen um 1
	if lesezeichen == 1:
		return "Hallo"
	elif lesezeichen == 2:
		return "das sehe ich auch so."
	elif lesezeichen == 3:
		return "Auf Wiedersehen"
	return ''

