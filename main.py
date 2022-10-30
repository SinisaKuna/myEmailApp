import smtplib
import ssl
from email.message import EmailMessage

subject = "Email From Python"
body = "This is a test email form Python!"


sender_email = "ivan.kuna.python@gmail.com"
password = "njzhzgnbchrskxdn"

receiver_email = "kuna.sinisa@gmail.com"


message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Sending Email!")
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Success")
except Exception as e:
    print(e)


