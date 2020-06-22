from email.mime.text import MIMEText
import smtplib

def send_email():
    from_email="abc123@gmail.com" #The email id from which you want to send the email
    from_password="**********" #The password of the from_email
    to_email="xyz321@gmail.com" #The email id to which you want to send the email...I don't think it's compulsory for it to be a gmail account
                                #but since I don't have any yahoo account in my family I couldn't try...if you guys do then just try that out...
                                #but I'm pretty sure from_email has to be a gmail account

    subject="Automated Emails Demo"
    message="Hey there, I am sending you an automated email"

    msg=MIMEText(message)
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
send_email()
