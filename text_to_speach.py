import pyttsx3

text_to_speach = pyttsx3.init()
answer =  input('write a text please')
text_to_speach.say(answer)
text_to_speach.runAndWait()

