import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from getpass4 import getpass
from speak import speak
import reconginze_speech as sr

class Sender:
    sender_email = ""
    password = ""

    def __init__(self):
        print("""Welcome to Automated Email Generator
        In order for you to write an email, we need access to your Gmail account. Don't worry, your information is safe with you. We don't keep track of it.
        Right now, it's for Gmail only, not Yahoo! or Bing.""")

        Sender.sender_email = input("Enter your Email:")
        Sender.password = getpass("Enter your password: ")
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        a= "What is the email of the other person: "
        speak(a)
        sr.speech_recognizer()
        self.receiver_email = input("What is the email of the other person: ")

    def get_message(self):
        # Getting the subject and the email
        # a = "Write down the Subject of your email: "
        # speak(a)
        self.subject = input("Write down the Subject of your email: ")
        self.message = input("Write down the message you want to send: ")

    def attach_file(self):
        self.msg = MIMEMultipart()
        print("Tell me if you want to attach any file:")
        path = input("Write down the path of that file: ")
        self.file_path = path
        with open(self.file_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {os.path.basename(self.file_path)}",
        )

        self.msg.attach(part)

    def send_email(self):
        try:
            self.get_message()
            self.attach_file()
            # Setting up the email:

            self.msg["From"] = Sender.sender_email
            self.msg["To"] = self.receiver_email
            self.msg["Subject"] = self.subject

            # Attach the message to the email
            self.msg.attach(MIMEText(self.message, "plain"))
            # server Handling

            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.ehlo()
            server.starttls()  # Enable TLS encryption
            server.login(Sender.sender_email, Sender.password)
            text = self.msg.as_string()
            server.sendmail(Sender.sender_email, self.receiver_email, text)
            print("Email sent successfully.")
            server.quit()
        except Exception as e:
            print(f"Error: {str(e)}")

# Usage Example:
if __name__ == "__main__":


    r = Sender()
    r.send_email()
