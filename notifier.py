import smtplib
from email.mime.text import MIMEText
import os





def send_notification(message):

    sender = "gourinandanarajesh@gmail.com"
    password = "sveuufdpgdzlxvfc"
    receiver = "gourinandanarajesh@gmail.com"

    msg = MIMEText(message)

    msg["Subject"] = "Period Tracker Alert"
    msg["From"] = sender
    msg["To"] = receiver

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(sender, password)

    server.sendmail(sender, receiver, msg.as_string())

    server.quit()