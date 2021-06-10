import smtplib


# a class for sending the daily notice email informing that this program is still running
class SendNotifyEmail:
    def __init__(self, gmail_user, gmail_password, to_address):
        self.gmail_user = gmail_user
        self.gmail_password = gmail_password
        self.to_address = to_address

    def sendEmail(self):
        try:
            email_text = "\r\n".join([
                ("From: " + self.gmail_user),
                ("To: " + ",".join(self.to_address),
                "Subject: NOTIFY - Timestream error checking in progress",
                "",
                "This is a daily confirmation notice that the Timestream Overseer continues to check for errors"
            ])

            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(self.gmail_user, self.gmail_password)
            server.sendmail(self.gmail_user, self.to_address, email_text)
            server.close()
        except:
            print('something went wrong')