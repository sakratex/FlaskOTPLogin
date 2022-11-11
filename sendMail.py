from email.mime.multipart import MIMEMultipart
import re
import smtplib
from email.mime.text import MIMEText
import os

def SendMail(OTP, mail):
    smtp_host = 'smtp.yandex.ru'
    login = "" #Yandex mail kullanici Adi
    password = "" #Yande mail sifre
    msg = MIMEMultipart()
    msg['Subject'] = 'OTP Login'
    msg['From'] = login
    msg['To'] = mail
    text = MIMEText(OTP)
    msg.attach(text)
    otpWrite(OTP)

    s = smtplib.SMTP(smtp_host, 587, timeout=10)

    try:
        s.starttls()
        s.login(login, password)
        s.sendmail(msg['From'], mail, msg.as_string())
        print("Mail başarı ile gönderildi.")
        return OTP
    except Exception as e:
        print(e)
    finally:
        s.quit()



def otpWrite(OTP):
    f = open("otp.txt", "a")
    f.write(OTP)
    f.close()

def otpRead():
    f = open("otp.txt", "r")
    otp = (f.read())
    os.remove("otp.txt")
    return otp
