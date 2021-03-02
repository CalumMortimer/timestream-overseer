import smtplib


# a class for sending an alarm email confirming a fault
class SendAlarmEmail:
    def __init__(self, gmail_user, gmail_password, to_addresses, database, table):
        self.gmail_user = gmail_user
        self.gmail_password = gmail_password
        self.to_addresses = to_addresses
        self.database = database
        self.table = table

    def sendEmail(self):
        try:
            email_text = "\r\n".join([
                ("From: " + self.gmail_user),
                ("To: " + ",".join(self.to_addresses)),
                "Subject: ALARM: Timestream Recording Error",
                "",
                "This is a notice that the dashboard relating to "
                + self.database + "." + self.table
                + " is not functioning normally. This is because no data for an instrument was recorded in the past "
                + "five minutes. Please investigate the fault and re-start monitoring. "
            ])
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(self.gmail_user, self.gmail_password)
            server.sendmail(self.gmail_user, self.to_addresses, email_text)
            server.close()
        except:
            print('something went wrong')