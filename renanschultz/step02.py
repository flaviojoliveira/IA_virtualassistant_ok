import speech_recognition as sr
import pyttsx3
from random import choice


erros_feedback = [
		"Desculpe, não entendi",
		"Pode repetir por favor",
		"Que língua é esta?"
]


fala = pyttsx3.init()


def execucao(retorno):
   	fala.say(retorno)
   	fala.runAndWait()

def identifica(feedback_fala):
	rec = sr.Recognizer()

	with sr.Microphone() as s:
		rec.adjust_for_ambient_noise(s)

		while True:
			try:
				audio = rec.listen(s)
				entrada = rec.recognize_google(audio, language="pt")
				return "Você disse: {}".format(entrada)
			except sr.UnknownValueError:
				return feedback_fala

print("Estou lhe ouvindo... \n**********\n")

while True:
	feedback_fala = choice(erros_feedback)
	voz = identifica(feedback_fala)
	print("Você disse: {}".format(voz))
	execucao(voz)
