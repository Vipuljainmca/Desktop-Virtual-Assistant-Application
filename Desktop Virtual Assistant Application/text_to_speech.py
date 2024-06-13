import pyttsx3 

def text_to_speech(text):
    
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate','rate-70')
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":

    text_to_speech("hey i am your Virtual assistant. how can i help you, sir")