from sendmail import send_email

attachments_dir = "attachments"
recipient_list = "recipients.txt"

# Define email sender and receiver
email_sender = 'example@gmail.com'
email_sender_name = 'Nice Name'

#check how to generate an app password for gmail https://support.google.com/mail/answer/185833?hl=en
email_password = 'this password must be an app password from your gmail account'


subject = 'example email subject'
body = """
Hello

This is a test email

Best regards
"""


send_email(email_sender=email_sender,email_sender_name=email_sender_name, email_password=email_password, filename_recipients=recipient_list, subject=subject, body=body)
print("Emails sent!")