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


while True:
    fala = reconhece()
    print("Voce disse: {}".format(fala))

#Comandos para abrir programas
    if (fala.lower() =="abrir bloco de notas"):
        os.system('notepad')
    elif(fala.lower() =="abrir calculadora"):
        os.system('calc')
    elif (fala.lower() == "abrir gerenciador de tarefas"):
        os.system('taskmgr')
    elif (fala.lower() == "abrir editor de desenho"):
        os.system('mspaint')
    elif (fala.lower() == "abrir reprodutor de som"):
        os.system('mmsys.cpl')
    elif (fala.lower() == "abrir explorer"):
        os.system('explorer')
    elif (fala.lower() == "abrir dispositivos e impressoras"):
        os.system('CONTROL PRINTERS')
    elif (fala.lower() == "abrir teclado virtual"):
        os.system('osk')
    elif (fala.lower() == "abrir painel de controle"):
        os.system('control')
    elif (fala.lower() == "enviar arquivo"):
        os.system('fsquirt')
