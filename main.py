import speech_recognition as sr #speech-to-text
import pyttsx3 #converts text to speech.
import webbrowser # used to open web pages or URLs in a web browser directly from your Python code.
import musiclibrary # custom module for music library

# speech_recognition (sr) → Converts speech to text (listens to your voice and understands it).
# pyttsx3 → Converts text to speech (makes your program speak out loud).
# webbrowser → Opens websites or URLs in your system’s browser from Python.

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# recognizer = sr.Recognizer()
# Creates an instance of the Recognizer class from speech_recognition.
# This object (recognizer) is used to listen to audio and convert it into text.
# Example use: recognizer.listen(source) or recognizer.recognize_google(audio).

# engine = pyttsx3.init()
# Initializes the text-to-speech engine from pyttsx3.
# This object (engine) is used to speak text out loud.
# Example use: engine.say("Hello") and engine.runAndWait().

def speak(text): # This function takes a string (text) and uses the text-to-speech engine to speak it out loud.
    engine.say(text) # This function takes a string (text) and uses the text-to-speech engine to speak it out loud. 
    engine.runAndWait() # This function takes a string (text) and uses the text-to-speech engine to speak it out loud.
    
def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")  
    elif "open twitter" in c.lower():
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")
    elif "open linkedin" in c.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    
    elif "open weather" in c.lower():
        speak("Opening Weather")
        webbrowser.open("https://www.weather.com")
        
    elif "open news" in c.lower():
        speak("Opening News")
        webbrowser.open("https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en")
    
    elif "open stock market" in c.lower():
        speak("Opening Stock Market")
        webbrowser.open("https://www.moneycontrol.com/stocksmarketsindia/")
        
    elif "open my leetcode profile" in c.lower():
        speak("Opening your LeetCode profile")
        webbrowser.open("https://leetcode.com/u/Dipak_Gupta_11/")
        
    elif "open my github profile" in c.lower():
        speak("Opening your GitHub profile")
        webbrowser.open("https://github.com/DipakGupta2006")
        
    elif "open my hackerrank profile" in c.lower():
        speak("Opening your HackerRank profile")
        webbrowser.open("https://www.hackerrank.com/profile/idipakgupta2006")
        
        
    elif c.lower().startswith("play music"): #Play Music Saiyaara
        song = c.lower().split("play music ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
        speak(f"Playing {song}")

if __name__ == "__main__":
   speak("Hello, I am your voice assistant. How can I help you today?")
   while True:
        r = sr.Recognizer()
        # reate a speech recognition object that lets your Python program listen to and understand spoken words.
                
        try: 
            print("Recognizing...")
            with sr.Microphone() as source:  # Turns on your microphone so the program can “hear” you.
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=3)
                #sets the maximum time the program will wait for you to start speaking.
                # If you don’t say anything within 2 seconds, the program stops listening and raises an error.
                
                # phrase_time_limit=3 sets the maximum duration of recording after you start speaking.
            word = r.recognize_google(audio) 
            # Takes the audio you recorded using r.listen().
            # Sends it to Google’s speech recognition service.
            # Converts your spoken words into text.
            # Stores the result in the variable word.
            
            # print(command)
            if(word.lower() == "hello"): # If the recognized word is "hello", the program will respond.
                speak("Hello, how can I assist you?")
                
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)                
                processCommand(command)
                
        except Exception as e:
            print(f"Error; {e}")
            
            # speak("Sorry, there was an error with the request.")    