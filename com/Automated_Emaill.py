import smtplib
import speech_recognition as sr

listner = sr.Recognizer()


def get_info():
    try:
        with sr.Microphone() as source:
            print("listening.......")
            voice = listner.listen(source)
            info = listner.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass




def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('popoolatunde52@gmail.com', '08138579886')
    server.sendmail('popoolatunde52@gmail.com', 'poptuma52@yahoo.com',
                    "testing my email bot code and how to automated the sending")


get_info()
