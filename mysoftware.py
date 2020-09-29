import pyttsx3
import os

pyttsx3.speak("Welcome to my tools")
print()
pyttsx3.speak("What can i do for you")

p=input()


if (('media' in p) or ("player" in p))and (("open" in p) or ('run' in p)):
  pyttsx3.speak("okay, let me open windows media player for you")
  os.system("wmplayer")

if (('notepad' in p) or ("text editor" in p)) and (("open" in p) or ('run' in p)):
  pyttsx3.speak("okay, let me open notepad for you")
  os.system("notepad")

if ('paint' in p) or ("Mspaint" in p) and (("open" in p) or ('run' in p)):
  pyttsx3.speak("okay, let me open MS Paint for you")
  os.system("Mspaint")

if ('task manager' in p) and (("open" in p) or ('run' in p)):
  pyttsx3.speak("okay, let me open task manager for you")
  os.system("taskmgr")