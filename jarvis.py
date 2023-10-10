import pyttsx3 as ptx  # convert text to speech
import datetime
import speech_recognition as sr
import smtplib
from secrets import sender, pwd, to
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
import wikipedia
from time import sleep
import pywhatkit
import os

engine = ptx.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is: ")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)

    speak("current date is")
    speak(date)
    speak(month)
    speak(year)


def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning dear")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon dear")
    elif hour >= 18 and hour < 24:
        speak("Good Evening dear")
    else:
        speak("Good night dear")


def wishme():
    speak("Welcome Back dear")
    time()
    date()
    greeting()
    speak("Jarvis at your service, How I can help you?")


def take_Command_From_Cmd():
    q = input("How can I help You 😊")
    return q


def take_Voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language="en-IN")
        print("User Said: "+query)

    except Exception as e:
        print(e)
        speak("Say that Again Please....")
        return None

    return query


def sendEmail(receiver, subjectcontent):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, pwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subjectcontent
    email.set_content(content)
    server.send_message(email)

    server.sendmail(sender, to, content)
    server.close()


def send_Whatsapp_Message(phone_no, message):
    Message = message
    web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    slepp(10)
    pyautogui.press('enter')


def searchgoogle():
    speak("what should I search")
    search = input("Enter content to be searched")
    wb.open('https://www.google.com/search?q='+search)


if __name__ == "__main__":
    # wishme()
    while True:
        query = take_Command_From_Cmd().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'email' in query:
            email_list = {
                "aray": 'avcf@gmail.com'
            }
            try:
                speak("To whom you want to send the mail?")
                name = input("name")
                receiver = email_list[name]

                speak("what is subject")
                subject = input("subject")

                speak("Give the content to be sent")
                content = input("Type content to be sent")

                sendEmail(receiver, subject, content)
                speak("email has been send")
            except Exception as e:
                print(e)
                speak("Unable to send the email")
        elif 'message' in query:
            user_name = {
                'gok': '+91 94488 88990'
            }
            try:
                speak("To whom you want to send the message?")
                name = input("name")
                phone_no = user_name[name]

                speak("Give the content to be sent")
                message = input("Type content to be sent")

                send_Whatsapp_Message(phone_no, message)
                speak("Message has been send")
            except Exception as e:
                print(e)
                speak("Unable to send the messsage")
        elif 'wikipedia' in query:
            speak("searching on wikipedia")
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'search' in query:
            searchgoogle()
        elif 'youtube' in query:
            speak("what should I search on youtube")
            topic = input("input")
            pywhatkit.playonyt(topic)
        elif 'open' in query:
            os.system('explorer C://{}'.format(query.replace('Open', '')))
        elif 'offline' in query:
            quit()
