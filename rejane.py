from speech_recognition import Microphone, Recognizer, UnknownValueError
import pyautogui
import pyttsx3
import random

criatura = pyttsx3.init()
recog = Recognizer()
mic = Microphone()

def fala_criatura(fala):
    criatura.setProperty('rate', 195)
    criatura.say(fala)
    criatura.runAndWait()
    return()

while True:
    with mic:
        fala_criatura('diga a senha')
        audio1 = recog.listen(mic)
    try:
        recognizedsenha = recog.recognize_google(audio1, language='pt').lower()         
        if recognizedsenha in 'lucas':
            fala_criatura('acesso, liberado... Vamos começaar, luucas')            
            while True:
                with mic:
                    fala_criatura('')
                    audio = recog.listen(mic)
                try:
                    recognized = recog.recognize_google(audio, language='pt').lower()
                    print(f'você disse: {recognized}')

# COMANDOS CONVERSA >>>>>>>>>>>>>>>>>>>>>
                    if recognized in 'olá''oi''oie''olá rejane''oi rejane''oie rejane':
                        conv1 = ['olá, luucas ? no que posso ajudar ?','posso lhe ajudar? Luucas?','olá, Luucas ? o que vamos fazer agora ?', 'olá, o que iremos fazer hoje, Luucas']
                        fala_criatura(random.choice(conv1))
# PULAR O ANÚNCIO DO YOUTUBE  >>>>>>>>>>>>>>>>>>>>>>>
                    elif recognized in 'pular anúncio''pule o anúncio''pular o anúncio''pula o anúncio':
                        pyautogui.click(x=1294, y=642)
                    
                except UnknownValueError:
                    fala_criatura('')
        else:
            fala_criatura('senha incorreta, acesso negado!')
    except UnknownValueError:
        fala_criatura('não intendi, repita a senha por favor')


