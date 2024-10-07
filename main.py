# So, Now This Is Our Mega Project Where We Create Our Virtual Assitant Named As "Jarvis".

# Importing Required Modules.
import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as tts
import music_library as ml
from playsound import playsound as ps

# Initializing Objects For sr & tts
recognizer = sr.Recognizer()
engine = tts.init()

# Creating A Speaking Function.
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Creating A Processing Function.
def processCommand(command):
    if(command.lower() == "open google"):
        speak("Wait I'm Opening.....")
        wb.open("https://google.com")
        
    elif(command.lower() == "open youtube"):
        speak("Wait I'm Opening.....")
        wb.open("https://youtube.com")

    elif(command.lower() == "open chat gpt"):
        speak("Wait I'm Opening.....")
        wb.open("https://chatgpt.com")

    elif(command.lower() == "open whatsapp"):
        speak("Wait I'm Opening.....")
        wb.open("https://whatsapp.com")

    # Adding Play-Song Functionality.
    elif(command.lower().startswith("play")):
        song = command.lower().split(" ")[1]
        songLink = ml.music[song]
        speak(f"Playing {song} On Youtube")
        wb.open(songLink)

    else: 
        print(f"Invalid Command: {command}")

# "name-main" Check
if __name__ == "__main__":
    speak("Hey There, I Am Jarvis And I Am Your Virtual Assistant")

    # 
    while (True):
        r = sr.Recognizer()
        # recognize speech using Google_Cloud
        try:
            with sr.Microphone() as source:
                print("Listining......")
                audio = r.listen(source, timeout=2, phrase_time_limit=1) # We Add Timeout As Well.....
                
            # Checking Commands.
            command = r.recognize_google(audio)
            print(command) 

            if(command.lower() == "hi jarvis" or command.lower() == "hey jarvis"):
                # speak("Yes, How May I Help You")
                ps('alert.mp3')

                # For Listining Command.
                try: 
                    with sr.Microphone() as source:
                        print("Jarvis Listining......")
                        audio = r.listen(source, timeout=2)
                        # print("waiting........") # Testing
                    
                except Exception as e:
                    print(e)

                # Checking Commands.
                command = r.recognize_google(audio)
                print(command) 

                processCommand(command)

        except Exception as e:
            print(f"Jarvis Error {e}")