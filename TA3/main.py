import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSenderApp():
    def __init__(self):
        super().__init__()

    def send_single_email(self):
        sender_email = input("Enter Sender Email\n")
        sender_password = input("Enter Sender Password\n")
        recipient_email = input("Enter Recipient Email\n")
        subject = input("Enter Email Subject\n")
        message_body = input("Enter Message\n")
        
        # Move the below code inside the try-except block
        
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)

        # Create and send the email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(message_body, "plain"))

        # Send mail using SMTP server
        

    


def main():
    app = EmailSenderApp()
    app.send_single_email()

if __name__ == "__main__":
    main()
