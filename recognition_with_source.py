import speech_recognition as sr


def command():
    r = sr.Recognizer()
    my_input = sr.AudioFile('audio.wav')
    with my_input as source:
     audio = r.record(source)
   # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("Speak something what you like ")
    #     r.pause_threshold  = 0.6
    #     audio = r.listen(source)


    try:
        ask  = r.recognize_google(audio,language='en-us')
        print(f"you said :{ask}")
    except Exception:
        print(" Repeat that again:")
        return ""
    return ask
command()
