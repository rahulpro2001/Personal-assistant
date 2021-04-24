import speech_recognition as sr
import pyttsx3 
import pywhatkit
import datetime
#import wikipedia
import pyjokes
def talke(speech):
    engine.say(speech)
    engine.runAndWait()
listener = sr.Recognizer()
engine= pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
talke('hello Rahul')
talke('I am jerry')
talke('How can I help you')
def command_back():
    try:
        with sr.Microphone() as source:
                print('listening.....')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'jerry' in command:
                    command = command.replace('jerry','')
                    print(command)     
    except:
        pass
    return command


def run_jerry():
    command = command_back()
    print(command)
    if 'play' in command:
        play = command.replace('play','')
        talke('playing' + play)
        pywhatkit.playonyt(play)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talke(time)  
        print('current time is' + time)
    elif 'what is the date today' in command:
        date = datetime.datetime.now().strftime('%d-%B-%Y')
        talke(date)
        print("Today is:" + date)
    elif 'date' in command:
        talke("sorry, i have lot of things to do")
    elif 'are you single' in command:
        talke("i am in relationship with your laptop")
    elif 'joke' in command:
        joke=pyjokes.get_joke()
        print(joke)
        talke(joke)
    elif 'who' or 'what' in command:
        print('searching.........')
        search = command.replace('who is' or 'what is','')
#        talke(pywhatkit.info("Google",lines = 5))
 #       res= wikipedia.summary(search,5)
 #       print(res)
 #       talke(res)
        pywhatkit.search(search)
    else:
        pywhatkit.search(command)
    


while True:
    run_jerry()

















