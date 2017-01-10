lesezeichen = 0

# Funktion, die 3 Ausgaben macht
def function():
	global lesezeichen #markiert, dass man auf die globale Variable zugreift
	lesezeichen += 1 # erhöhe Lesezeichen um 1
	if (lesezeichen == 1):
		print("Hallo")
	elif ...
	print("das sehe ich auch so.")
	print("Auf Wiedersehen")

# rufe die Funktion 1x auf.
function()