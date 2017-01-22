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

# Bot spricht mit dem Mensch
mensch = input("> " + "Hallo" + "\n* ")

if "hallo" in mensch or "hi" in mensch:
	mensch = input("> " + "Wie geht es Dir?" + "\n* ")
else:
	mensch = input("> " + "ich verstehe dich nicht" + "\n* ")

if "gut" in mensch:
	mensch = input("> " + "prima" + "\n* ")
elif "schlecht" in mensch:
	mensch = input("> " + "schade" + "\n* ")
else:
	mensch = input("> " + "ich verstehe dich nicht" + "\n* ")	

print ("Auf Wiedersehen!")

