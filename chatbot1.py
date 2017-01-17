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
name = "bot1"

# Bot programm
def sprich(mensch):

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

