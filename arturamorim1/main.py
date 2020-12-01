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
                return "Nao entendi o que voce disse"
print("Escutando...")
while True:
    voz = reconhece()
    print("Voce falou: {}".format(voz))
    if (voz.lower() == "painel de controle"):
        os.system('control')
    elif (voz.lower() =="bloco de notas"):
        os.system('notepad')
    elif (voz.lower() == "gerenciador de tarefas"):
        os.system('taskmgr')
    elif (voz.lower() == "reprodutor de som"):
    	 os.system('mmsys.cpl')
    elif (voz.lower() == "painel de controle"):
        os.system('control')
    elif (voz.lower() == "explorer"):
        os.system('explorer')
    elif (voz.lower() == "teclado virtual"):
        os.system('osk')
    