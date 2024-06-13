import speech_recognition as sr
import threading

# def speech_to_text():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         audio = r.listen(source)

#     try:
#         voice_data = ''
#         voice_data = r.recognize_google(audio)
#         print(voice_data)
#         return voice_data
#     except sr.UnknownValueError:
#         print("error")
#     except sr.RequestError:
#         print("request error")
#     except Exception as e:
#         print(e)

# speech_to_text()



# def speech_to_text():
#     r = sr.Recognizer()
#     with sr.Microphone(energy_threshold=4000) as source:
#         audio = r.listen(source, timeout=5, phrase_time_limit=10)

#     try:
#         voice_data = r.recognize_google(audio)
#         print(voice_data)
#         return voice_data
#     except sr.UnknownValueError:
#         print("error")
#     except sr.RequestError:
#         print("request error")
#     except Exception as e:
#         print(e)

# # Create a thread to run speech_to_text
# speech_thread = threading.Thread(target=speech_to_text)

# if __name__ == "__main__":
#     speech_to_text()
#     # Your main program can continue running here

# import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    r.energy_threshold = 4000  # Set the energy threshold
    with sr.Microphone() as source:
        audio = r.listen(source, timeout=5, phrase_time_limit=10)

    try:
        voice_data = r.recognize_google(audio)
        print(voice_data)
        return voice_data.lower()
    except sr.UnknownValueError:
        print("error")
    except sr.RequestError:
        print("request error")
    except Exception as e:
        print(e)

# speech_to_text()


