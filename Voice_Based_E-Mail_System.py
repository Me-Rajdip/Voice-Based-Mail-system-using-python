import speech_recognition as sr
import smtplib

import imaplib
from gtts import gTTS
import pyglet
import os
import time
import pyttsx3
import easyimap as e


mail = "...................."
pws ="....................."

r = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 130)


def speak(txt):
    print(txt)
    engine.say(txt)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        str = "Speak Now"
        speak(str)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            str = "Sorry could not recognize what you said"
            speak(str)


print("\n\t \t \t -------------------------Welcome to Voice Based Email-------------------------")
say = gTTS(text=" Hi welcome to voice based email \n", lang='en')
convert = ("1.mp3")
say.save(convert)
music = pyglet.media.load(convert, streaming=False)
music.play()
time.sleep(music.duration)
os.remove(convert)

print("\t \t \t-------------------------Guide by Prof. Piyali Sanyal--------------------------")
say = gTTS(text=" Guide by Professor Piyali Sanyal \n", lang='en')
convert = ("1.mp3")
say.save(convert)
music = pyglet.media.load(convert, streaming=False)
music.play()
time.sleep(music.duration)
os.remove(convert)

# txt = "\t \t \t----------------------------Guide by Pyali Sanyal--------------------------------"
# speak(txt)

txt = "\t \t \tCreated by Chayan Patra, Rajdip Bera, Sulagna Dey\n\n\n"
speak(txt)

txt = " Please select your required choice"
speak(txt)

print("\t\t\t1. Compose a mail. \t\t\t\t\t\t----------> (compose)\n")
say = gTTS(text="Say 'compose' to compose a mail.", lang='en')
convert = ("start2.mp3")
say.save(convert)
music = pyglet.media.load(convert, streaming=False)
music.play()
time.sleep(music.duration)
os.remove(convert)

print("\t\t\t2. Check your inbox. \t\t\t\t\t----------> (Check)\n")
say = gTTS(text="Say 'check' to Check your inbox", lang='en')
convert = ("start2.mp3")
say.save(convert)
music = pyglet.media.load(convert, streaming=False)
music.play()
time.sleep(music.duration)
os.remove(convert)

print("\t\t\t3. Read message. \t\t\t\t\t\t----------> (Read)\n")
say = gTTS(text="Say 'Read' to read message in your inbox", lang='en')
convert = ("start2.mp3")
say.save(convert)
music = pyglet.media.load(convert, streaming=False)
music.play()
time.sleep(music.duration)
os.remove(convert)

print("\t\t\t4. Delete recent Email. \t\t\t\t----------> (Delete)\n")
say = gTTS(text="Say 'Delete' to delete the Recent email ", lang='en')
convert = ("start2.mp3")
say.save(convert)
music = pyglet.media.load(convert, streaming=False)
music.play()
time.sleep(music.duration)
os.remove(convert)

print("\t\t\t5. Exit for mail. \t\t\t\t\t\t---------->  (Exit)\n")
say = gTTS(text="Say 'Exit' to exit from  a mail.", lang='en')
convert = ("start2.mp3")
say.save(convert)
music = pyglet.media.load(convert, streaming=False)
music.play()
time.sleep(music.duration)
os.remove(convert)

say = gTTS(text=" Select your choice  ", lang='en')
convert = ("start2.mp3")
say.save(convert)
music = pyglet.media.load(convert, streaming=False)
music.play()
time.sleep(music.duration)
os.remove(convert)

speech1 = sr.Recognizer()
with sr.Microphone() as source:
    print("\tYour choice:\n")
    speech2 = speech1.listen(source)
    print("\t\t\tCommand Accepted\n")

try:
    text = speech1.recognize_google(speech2)
    print("\t\tYou said : " + text)

except sr.UnknownValueError:
    print("Can't Understand the command. Run Again")

except sr.RequestError as e:
    print("Could not Connect to the Internet; {0}".format(e))

    # ch = listen()
if text == 'compose' or text == 'compoze' or text == 'compus' or text == 'kompoz':
    speech1 = sr.Recognizer()
    with sr.Microphone() as source:
        print(" \t\tSay Your message  :\n")
        speech2 = speech1.listen(source)
        print("\t\t\tCommand Accepted\n")
    try:
        text1 = speech1.recognize_google(speech2)
        print("\tYou said :" + text1)
        msg = text1
    except sr.UnknownValueError:
        print("Can't Understand the command. Run Again.")
    except sr.RequestError as e:
        print("Could not Connect to the Internet; {0}".format(e))

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('mail', 'pws')
    mail.sendmail('..............', 'reciver', msg)
    print(" \t\tYour message Has been Sent. ")
    say = gTTS(text="Your message Has been Sent", lang='en')
    convert = ("3.mp3")
    say.save(convert)
    music = pyglet.media.load(convert, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(convert)
    mail.close()

if text == 'check':
    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    username = ('mail')
    password = ('.............')
    mail.login(username, password)
    subtotal, total = mail.select('Inbox')
    print("\t\tTotal number of mails in your inbox :" + str(total))
    say = gTTS(text="Total  number of mails are :" + str(total), lang='en')
    convert = ("4.mp3")
    say.save(convert)
    music = pyglet.media.load(convert, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(convert)


    mail.close()
    mail.logout()

if text  == 'read':
    server = e.connect("imap.gmail.com", usn, pws)
    server.listids()

    str = "Please say the Serial Number of the email you wanna read starting from latest"
    speak(str)

    a = listen()
    #if (a == "Tu"):
        #a = "2"

    b = int(a) - 1

    email = server.mail(server.listids()[b])

    str = "The email is from: "
    speak(str)
    speak(email.from_addr)
    str = "The subject of the email is:"
    speak(str)
    speak(email.title)
    str = "The body of email is :"
    speak(str)
    speak(email.body)
    #mail.close()
    #mail.logout()

if text == 'delete' or text == 'dele' or text == 'delite' or text == 'dilit' or text == 'delight':
    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    mail.login("mail", ".................")
    mail.select('Inbox')
    typ, data = mail.search(None, 'ALL')
    ids = data[0]  # data is a list.
    id_list = ids.split()  # ids is a space separated string
    latest_email_id = id_list[-1]
    mail.store(latest_email_id, '+FLAGS', '\\Deleted')
    mail.expunge()
    print("\t\trecent mail is Deleted")
    mail.close()
    mail.logout()
if text == 'exit':

    mail.close()
    mail.logout()

