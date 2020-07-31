try:
    import pyttsx3
    import datetime
    import speech_recognition as sr
    import wikipedia
    import smtplib
    import webbrowser as wb
    import os
    import pyautogui
    import psutil
    import pyjokes

except:
    os.system('pip install pyttsx3 speechrecognition wikipedia pyautogui psutil pyjokes')

en=pyttsx3.init()

en.setProperty('rate', 130)
en.say('Hello Sarthak!')
en.runAndWait()

def speak(audio):
    en.say(audio)
    en.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year= int(datetime.datetime.now().year)
    month= int(datetime.datetime.now().month)
    date= int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def wishme():
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("good morning.")
    elif hour>=12 and hour<18:
        speak("good afternoon.")
    elif hour>=18 and hour<24:
        speak("good evening.")
    else:
        speak("good night.")

def takecommand():
    query = input('You: ').lower()
    return query

def searchWiki():
    speak('Searching...')
    query = query.replace('wikipedia','')
    result = wikipedia.summary(query, sentences=2)
    speak(result)
def sendEmail(to, content, mail, password):
    server = smtplib.SMTP('smtp.gmail.com',  587)
    server.ehlo()
    server.starttls()
    server.login(mail,password)
    server.sendmail(mail, to, content)
    server.close()
def open(query):
    application = query[5:]
    if application == 'telegram':
        os.system('telegram-desktop')
    if application == 'terminal':
        os.system('xfce4-terminal')
    else:
        os.system(application)
def mail():
    try:
        speak('please login to your gmail account sir')
        mail = input("Enter your GMail: ")
        password = input('Enter your password: ')
        print(mail,password)
        speak('What is the content of your mail?')
        content = input('Content: ')
        to = speak('Whom do you want to send the mail?')
        to = input('To: ')
        sendEmail(to, content, mail, password)
        speak('email has been sent')
    except Exception as e:
        print(e)
        speak('Unable to send the mail')
def screenshot():
    year= str(datetime.datetime.now().year)
    month= str(datetime.datetime.now().month)
    date= str(datetime.datetime.now().day)
    Time= str(datetime.datetime.now().strftime("%I:%M:%S"))
    img = pyautogui.screenshot()
    ssname = Time + '-' + date + '-' + month + '-' + year
    img.save(('/home/sarthak/PyScreenshots/'+ssname+'.png'))
    speak('screenshot saved in pictures folder')
def cpu_usage():
      usage = str(psutil.cpu_percent())
      speak('CPU usage is'+usage+'percent')
def joke():
    speak(pyjokes.get_joke())
    print(pyjokes.get_joke())
if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()
        if 'time'in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            searchWiki()
        elif 'send email' in query:
            mail()
        elif 'search google' in query:
            speak('this feature is in development')
            #speak('what should i search on google ?')
        elif 'reboot' in query:
            os.system('reboot')
        elif 'reboot' in query:
            os.system('shutdown now')
        elif 'logout' in query:
            os.system('pkill -KILL -u sarthak ')
        elif 'play songs' in query:
            speak('this feature is in development')
            #songs_dir = '/home/sarthak/Music'
            #songs = os.listdir(songs_dir)
            #os.startfile(os.path.join(songs_dir, songs[0]))
        elif 'take screenshot' in query:
            screenshot()
        elif 'cpu usage' in query:
            cpu_usage()
        elif 'open' in query:
            open(query)
        elif 'battery' in query:
            battery()
        elif 'joke' in query:
              joke()
        elif "offline" in query:
            quit()
        else:
              speak('sorry sir, i cant understand you. come again.')