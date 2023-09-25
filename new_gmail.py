subject = "Automated Email"
message = "This is an automated email sent from Python."
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

# Attach the message to the email
msg.attach(MIMEText(message, "plain"))

# Attach a file (e.g., a PDF)
file_path = "path/to/attachment.pdf"
with open(file_path, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    
encoders.encode_base64(part)
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {os.path.basename(file_path)}",
)

msg.attach(part)



try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Enable TLS encryption
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print("Email sent successfully.")
except Exception as e:
    print(f"Error: {str(e)}")
finally:
    server.quit()

