import time
import chatbot1
import lesezeichenbot

# main program
def main():

	# Eine Dialogzeile, zu Beginn leer
	zeile = ''

	# Endlosschleife. Wird so lange ausgefuehrt, bis der Mensch den Dialog beendet
	while True:
		
		# Frage Bot 1
		zeile = chatbot1.sprich(zeile)

		# Wenn eine leere Antwort kommt, beende den Dialog
		if zeile == '':
			break

		# gib die Antwort von bot1 aus und warte 1 sekunde
		print (chatbot1.name + ": " + zeile)
		time.sleep(1)

		# jetzt ist bot 2 dran. Frage Bot 2
		zeile = lesezeichenbot.sprich(zeile)

		# Wenn eine leere Antwort kommt, beende den Dialog
		if zeile == '':
			break

		# gib die Antwort von bot2 aus und warte 1 Sekunde
		print (lesezeichenbot.name + ": " + zeile)
		time.sleep(1)

	# Ende des Gespraechs
	print ("--- Ende des Gespraechs ---")

if __name__ == "__main__":
    main()
