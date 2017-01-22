"""
> Hello, I am Eliza.
* good morning
> Don't you ever say Hello? 
* yes, i do
> I see. 
* How are you?
> Would you prefer if I were not ? 
* You are so philosophical
> Perhaps you would like to be so philosophical? 
* indeed
> OK... "You am so philosophical". Tell me more.
* bye
> Nice talking, have a good day!
"""

# python chat programm

# Bot programm
def get_bot(mensch):

	# finde die richtige Antwort fuer ein Schluesselwort
	if 'morning' in mensch:
		return "Don't you ever say Hello?"
	elif 'yes' in mensch:
		return 'I see'
	elif 'you' in mensch:
		return "Would you prefer if I were not ?"
	elif 'philosophical' in mensch:
		return "Perhaps you would like to be so philosophical?"
	elif 'indeed' in mensch:
		return 'OK... "You am so philosophical". Tell me more.'
	else:
		return "I don't understand"



# main program
def main():

	# Flag, zeigt an, dass der Dialog noch laeuft
	dialog = True

	# Text, den der Bot zur Begruessung sagt
	bot = "Hello, I am Eliza"

	# Endlosschleife. Wird so lange ausgefuehrt, bis der Mensch den Dialog beendet
	while dialog:
		
		# Bot spricht mit dem Mensch
		mensch = input("> " + bot + "\n* ")

		# ueberpruefe, ob der Mensch den Dialog beenden moechte
		if 'bye' in mensch or 'exit' in mensch:
			dialog = False

		# andernfalls frage den Bot nach seiner Antwort
		else:
			bot = get_bot(mensch)		

	print ("Nice talking, have a good day!")

if __name__ == "__main__":
    main()

