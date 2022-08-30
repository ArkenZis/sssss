from email.message import EmailMessage
from multiprocessing import context
from password import pwd
import ssl
import smtplib

email_sender = "rahil.haneef10@gmail.com"
email_password = pwd

email_receiver = "bedaro1373@otodir.com"

subject = "Test Email 2"

body = """
This is a test email sent from python 2
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
