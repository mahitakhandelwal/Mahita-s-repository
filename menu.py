import speech_recognition as sr
import webbrowser
import pyttsx3

pyttsx3.speak("Welcome to my tools")

r = sr.Recognizer()

with sr.Microphone() as source:
        print('start saying your requirements...')
        audio = r.listen(source)
        print('okay we have got it...')

ch = r.recognize_google(audio)

#ch=input()
if ("date" in ch) and (("run" in ch) or ("execute" in ch)) :
	webbrowser.open("http://192.168.43.182/cgi-bin/iiec.py?x=date")
elif (("calender" in ch) or ("cal" in ch)) and (("run" in ch) or ("execute" in ch) or ("open" in ch)) :
	webbrowser.open("http://192.168.43.182/cgi-bin/iiec.py?x=cal")
else:
	print("not unerstand")
	
