import smtplib
import ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.encoders import encode_base64
from email.mime.text import MIMEText
import os
from rich import print
import re





def check_email(email:str):
    #[\w-]+@([\w-]+\.)+[\w-]+ # https://regexlib.com/Search.aspx?k=email
    if re.match(r"[\w-]+@([\w-]+\.)+[\w-]+", email):
        return True
    else:
        return False

def send_email(filename_recipients:str,email_sender:str,email_sender_name:str,email_password:str,subject:str,body:str,attachments_folder:str="attachments",smtp_server:str="smtp.gmail.com",smtp_port:int=465):
    
    #get list of files in attachments folder
    attachments = [f"{file}" for file in os.listdir(attachments_folder)]
    
    with open(filename_recipients, 'r') as f:
        for email_receiver in f:
            email_receiver = email_receiver.strip("\n")
            if not check_email(email_receiver):
                print(f"Invalid email: {email_receiver}")
                continue
            msg = MIMEMultipart()
            msg['From'] = email_sender_name
            msg['To'] = email_receiver
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            for attachment in attachments:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(open(f"{attachments_folder}\\{attachment}", 'rb').read())
                encode_base64(part)
                part.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', attachment))
                msg.attach(part)
            # Send the email
            try:
                server = smtplib.SMTP_SSL(smtp_server, smtp_port)
                server.ehlo()
                server.login(email_sender, email_password)
                server.sendmail(email_sender, email_receiver, msg.as_string())
                server.close()
                print(f'Email to {email_receiver} sent!')
            except:
                print(f'Something went wrong while sending to {email_receiver} ')


