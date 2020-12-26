import speech_recognition as sr


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something what you like ")
        print("Recognizing")
        r.pause_threshold  = 0.6  
        audio = r.listen(source)


        try:
            ask  = r.recognize_google(audio,language='en -us')
            print(f"you said :{ask}")
        except Exception:
            print(" sorry can Repeat that once again for me:")
            return ""
        return ask
command()
