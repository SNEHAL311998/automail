import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening....')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver,subject,message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('snehal311998@gmail.com', 'hydralex990')
    email = EmailMessage()
    email['From'] = 'snehal311998@gmail.com'
    email['to'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_list = {
    'snehal': 'snehal.3as@gmail.com',
    'lallu': '4jk18cs058snehal@gmail.com'
}

def get_email_info():
    talk('whom you want to send email to')
    name = get_info()
    receiver = email_list[name]
    talk('What is the subject of your email')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Your message was sent successfully')
    talk('do you want to send more email')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()

get_email_info()
