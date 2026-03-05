import smtplib
from email.mime.text import MIMEText
import os


def send_notification(message):

    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("EMAIL_RECEIVER")

    msg = MIMEText(message)

    msg["Subject"] = "Period Tracker Alert"
    msg["From"] = sender
    msg["To"] = receiver

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(sender, password)

    server.sendmail(sender, receiver, msg.as_string())

    server.quit()