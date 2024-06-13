import text_to_speech
import speech_to_text
import weather
import datetime
import webbrowser



#api key = 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
def Action(user_val):
        
    user_data = user_val

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("my name is virtural assistant")
        return "my name is virtural assistant"

    elif "hello" in user_data:
        text_to_speech.text_to_speech("hey, sir how can i help you")
        return "hey, sir how can i help you"

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("good morning sir, how can i help you")
        return "good morning sir, how can i help you"

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + "hour :" , (str)(current_time.minute) + "minute"
        text_to_speech.text_to_speech(Time)
        
        return Time

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return "ok sir"
    

    elif "play music" in user_data:
        webbrowser.open("https://ganna.com/")
        text_to_speech.text_to_speech("ganna.com is now ready for you")
        return "ganna.com is now ready for you"

    

    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("google.com is ready for you")
        return "google.com is ready for you"

    elif "weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans
    
    elif "youtube" in user_data:
        l = user_data.split()
        l.remove("youtube")
        if "search" in l:
            l.remove("search")
        search_query = ''
        for i in l:
            search_query += i
            search_query += '+'

        webbrowser.open(f"https://www.youtube.com/search?q={search_query}")
        text_to_speech.text_to_speech("showing your search result on youtube")
        return "showing your search result on youtube"
    
    elif "search" in user_data:
        l = user_data.split()
        l.remove("search")
        if "google" in l:
            l.remove("google")
        search_query = ''
        for i in l:
            search_query += i
            search_query += '+'

        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        text_to_speech.text_to_speech("showing your search result on google")
        return "showing your search result on google"
    
    

    else:
        text_to_speech.text_to_speech("i am not able to understand")
        return "i am not able to understand"
    


        
