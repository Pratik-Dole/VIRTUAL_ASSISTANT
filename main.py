# So, Now This Is Our Mega Project Where We Create Our Virtual Assitant Named As "Jarvis".

# Importing Required Modules.
import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as tts

# 
recognizer = sr.Recognizer()
engine = tts.init()

# Creating A Speaking Function.
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Creating A Processing Function.
def processCommand(command):
    if(command.lower() == "open google"):
        wb.open("https://google.com")
        speak("Wait I'm Opening.....")
        
    elif(command.lower() == "open youtube"):
        wb.open("https://youtube.com")
        speak("Wait I'm Opening.....")

    elif(command.lower() == "open chat gpt"):
        wb.open("https://chatgpt.com")
        speak("Wait I'm Opening.....")

    elif(command.lower() == "open whatsapp"):
        wb.open("https://whatsapp.com")
        speak("Wait I'm Opening.....")

    else: 
        print(f"Invalid Command: {command}")

# "name-main" Check
if __name__ == "__main__":
    speak("Initializing Jarvis.........")

    # 
    while (True):
        r = sr.Recognizer()
        # recognize speech using Google_Cloud
        try:
            with sr.Microphone() as source:
                print("Listining......")
                audio = r.listen(source, timeout=2) # We Add Timeout As Well.....
                
            # Checking Commands.
            command = r.recognize_google(audio)
            print(command) 

            if(command.lower() == "hi jarvis" or command.lower() == "hey jarvis"):
                speak("Yes, How May I Help You")

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