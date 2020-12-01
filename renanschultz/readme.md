### Inserindo voz em nossa assistente virtual - ALUNO RENAN MEDINA

BIBLIOTECAS UTILIZADAS 

### Step 01

- [x] SpeechRecognition
- [x] Pyaudio

Premissas para execução:

```sh
$ pip3 install SpeechRecognition

$ pip3 install pyaudio

```
Se ocorrer erro na execução com a biblioteca pyaudio:
```
#verifique sua versão do Python
$ python --version
```
Acesse o site abaixo e realize o download correspondente.

https://thetechinfinite.com/2020/07/14/how-to-install-pyaudio-module-in-python-3-0-in-windows/

### Step 02

No step anterior nosso código estava com apenas uma resposta no return

Nesta etapa de nosso projeto criamos um "feedback_fala" com uma lista de respostas para os casos de erro quando não tivermos a compreensão da voz.

- [x] Instalar Pyttsx3
```sh
$ pip3 install pyttsx3
```
