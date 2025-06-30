import speech_recognition as sr
import pyttsx3

from GoogleNews import GoogleNews

news = GoogleNews()
a = pyttsx3.init()

speak_voice = a.getProperty('voices')
# Set the voice to a specific one (you can change the index to select different voices)
a.setProperty('voice', speak_voice[1].id)  

# Initialize the speech recognizer
recognizer = sr.Recognizer()

def speak_news():
    with sr.Microphone() as source:
        print("Clearing background noise, please wait...")
        # Adjust for ambient noise to improve recognition accuracy
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Tell me the topic for which you want the news....")
        listen_voice = recognizer.listen(source, timeout=1)
        print("Your voice has been recorded, processing...")

    try:
        # Recognize the speech using Google Web Speech API
        news_txt = recognizer.recognize_google(listen_voice,language='en-US')
        news_txt = news_txt.lower()
        print("Your message said is : ", format(news_txt))
    except Exception as e:
        print("Sorry, I did not understand that. Please try again.")
        print("Error: ", str(e))

    # Fetch news based on the recognized news_txt
    if 'business' in news_txt:
        a.say("Here are the latest business news...")
        a.runAndWait()
        news.get_news('Todays News Bussiness are : ') 
        news.result()
        b = news.get_texts()
        print(*b[1:5], sep=' , ')
    if 'sports' in news_txt:
        a.say("Here are the latest sports news...")
        a.runAndWait()
        news.get_news('Sports News')
        news.result()
        b = news.get_texts()
        print(*b[1:5], sep=' , ')
    if 'tech' in news_txt:
        a.say("Here are the latest technology news...")
        a.runAndWait()
        news.get_news('Technology News')
        news.result()
        b = news.get_texts()
        print(*b[1:5], sep=' , ')

speak_news()
