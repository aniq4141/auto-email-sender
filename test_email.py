import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_user = 'aniqstavin41@gmail.com'
smtp_password = 'ehbf afqr paph naws'
server = 'smtp.gmail.com'
port = 587

msg = MIMEMultipart("alternative")
msg["Subject"] = 'Why, Oh why!'
msg["From"] = smtp_user
msg["To"] = "aniqkhokhar18357@gmail.com"
msg.attach(MIMEText('Sent via python', 'plain'))

s = smtplib.SMTP(server, port)
s.ehlo()
s.starttls()
s.login(smtp_user, smtp_password)
s.sendmail(smtp_user, "aniqkhokhar18357@gmail.com", msg.as_string())
s.quit()
