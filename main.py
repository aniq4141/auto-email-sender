import getpass
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

def initialize():
    print("Welcome to Automated Email Generator: ")
    print("In order for you to write Email, We need access to your gamil"
          "accoutn, Don't worry You information is saved with You. We don't keep track "
          "of it.")
    print("Right now It's for only the Gamil Not Yahoo! or bing")

    sender_email = str(input("Enter your Email:"))
    password = getpass.getpass("Enter your password: ")
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

def email_content():
    print("Now tell Us What do you want to send")
    subject = str(input("What is the subject of you email:"))
    receiver_email = str(input("What is the email of the other person."))
    message = str(input("Write down the message You want to send."))

# def writing_email():




if __name__ == "__main__":
    initialize()










