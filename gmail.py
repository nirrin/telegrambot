#!/usr/bin/env python


import smtplib
import keyring

class Gmail(object):
    def __init__(self, email):
        self.email = email
        self.password = keyring.get_password("gmail", email)
        self.server = 'smtp.gmail.com'
        self.port = 587

    def create_session(self):
        session = smtplib.SMTP(self.server, self.port)        
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.email, self.password)
        self.session = session

    def send_message(self, to, subject, body):
        headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + to,
            "MIME-Version: 1.0",
           "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        self.create_session()
        self.session.sendmail(
            self.email,
            to,
            headers + "\r\n\r\n" + body)
