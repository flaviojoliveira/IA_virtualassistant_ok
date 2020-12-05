import speech_recongnition as sr

r = sr.Recongnizer

with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)

    while True: 
        audio =r.listen(s)

        speech = r.recognize_google(audio, language='pt')

        print('Voce disse: ' speech)
