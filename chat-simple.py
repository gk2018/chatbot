
def schoener(s):
	return input("> " + s + "\n* ")

# Bot spricht mit dem Mensch
mensch = schoener("Hallo")

if "hallo" in mensch or "hi" in mensch:
	mensch = schoener("Wie geht es Dir?")
else:
	mensch = schoener("ich verstehe dich nicht")

if "gut" in mensch:
	mensch = schoener("prima")
elif "schlecht" in mensch:
	mensch = schoener("schade")
else:
	mensch = schoener("ich verstehe dich nicht")

print ("Auf Wiedersehen!")


