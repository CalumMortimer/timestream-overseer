import time
import os
from CheckResource import CheckResource
from dotenv import load_dotenv
from SendNotifyEmail import SendNotifyEmail
from SendAlarmEmail import SendAlarmEmail
load_dotenv()


# get the 2D resource list from .env file
resources = os.getenv("RESOURCES").split(";")
# get the email list from .env file
interestedParties = os.getenv("INTERESTED_PARTIES").split(",")
# get the admin email
veryInterestedParty = os.getenv("VERY_INTERESTED_PARTY").split(",")
# get gmail credentials
gmail_user = os.getenv("GMAIL_USERNAME")
gmail_password = os.getenv("GMAIL_PASSWORD")


if __name__ == '__main__':
    # parse the resources list
    newResources = []
    for resource in resources:
        resource = resource.split(",")
        newResources.append(resource)
    resources = newResources

    # continuously check the timestream server
    results = 0
    counter = 287
    while True:
        for resource in resources:
            checkResource = CheckResource(resource[0], resource[1], resource[2])
            results = checkResource.getResults()
            if results[0] == 1:
                break
        if results[0] == 1:
            break
        counter = counter+1
        # send a daily update
        if counter == 288:
            counter = 0
            email = SendNotifyEmail(gmail_user, gmail_password, veryInterestedParty)
            email.sendEmail()
        time.sleep(300)

    # if an error occurs, then send an email and terminate program
    if results[0] == 1:
        email = SendAlarmEmail(gmail_user, gmail_password, interestedParties, results[1], results[2])
        email.sendEmail()

