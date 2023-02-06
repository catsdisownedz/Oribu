import os
from twilio.rest import Client

#we are using twilio website for the SMS service and integrated it into our code, inshallah we will continue where we left off and make a better application instead 

def notify(name):
    print("Sending...")
    account_sid = "AC543df96bf9583d51952e0201ba3a18c0"
    #TODO: Auth token should be hidden
    auth_token = "8a5f7873453b3dfbb6d6872548f0b613"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
            body="Alert!\n Criminal: {} is found near (the webcam :P)".format(name),
        from_="+16509552472",
        to="+201000024633"
    )

    print(message.sid)

notify("Zeina")
