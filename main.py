from gtts import gTTS
from playsound import playsound
# need to install using pip

audio = 'speech.mp3'
language = 'en'


text = input("Enter the text that you want to convert to speech: ")
sp = gTTS(text=text, lang=language, slow=False)

sp.save(audio)      # Saves the audio in the project folder
playsound(audio)    # Plays the audio during execution
