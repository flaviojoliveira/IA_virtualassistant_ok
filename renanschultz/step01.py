import speech_recognition as sr
import pyaudio
import os
def reconhece ():
    rec = sr.Recognizer()
    with sr.Microphone() as s:
        rec.adjust_for_ambient_noise(s)
        while True:
            try:
                audio = rec.listen(s)
                entrada = rec.recognize_google(audio, language="pt")
                return entrada.encode('utf-8')
            except sr.UnknownValueError:
                return "Nao entendi nada"
print("Ouvindo...")
  
