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

	# finde die richtige Antwort fuer ein Schluesselwort
	if 'morning' in mensch:
		bot = "Don't you ever say Hello?"
	elif 'yes' in mensch:
		bot = 'I see'
	elif 'you' in mensch:
		bot = "Would you prefer if I were not ?"
	elif 'philosophical' in mensch:
		bot = "Perhaps you would like to be so philosophical?"
	elif 'indeed' in mensch:
		bot = 'OK... "You am so philosophical". Tell me more.'
	else:
		bot = "I don't understand"

print ("Nice talking, have a good day!")

