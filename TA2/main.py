# Import smtplib, MIMEText, MIMEMultipart

class EmailSenderApp():
    def __init__(self):
        super().__init__()

    def send_single_email(self):
        sender_email = input("Enter Sender Email\n")
        sender_password = input("Enter Sender Password\n")
        recipient_email = input("Enter Recipient Email\n")
        subject = input("Enter Email Subject\n")
        message_body = input("Enter Message\n")
        
        # Setup SMTP server
       

        # Create and send the email
       

        # Print the values
       

       


def main():
    app = EmailSenderApp()
    app.send_single_email()

if __name__ == "__main__":
    main()

