# STEP 1 - INSTALLING REQUIRED LIBRARIES
from twilio.rest import Client
# Using this to send messsage
from datetime import datetime, timedelta
# datetime to select when to send the message and using timedelta to calculate time difference
import time 
# to send message at a particular time



 
 # STEP 2 -  TWILIO ESSENTIALS
account_sid = "Use your Unique Twiloi Acoount sid"
auth_token = "Use your unique authentication token"


client = Client(account_sid, auth_token)


# STEP 3 - DESIGN SEND MESSAGE FUNCTION
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            body = message_body,
            from_ = 'whatsapp:Your assigned Twilio Number',
            to=f'whatsapp:{recipient_number}'
        )
        print(f"message sent successfully! Message SID {message.sid}")
    except Exception as e:
        print(f"An error Occured: {e}")


# STEP 4 -  USER INPUT

name = input("Enter the recipient's name: ")
recipient_number = input("Enter the Recipient's WhatsApp number: ")
message_body = input(f"Enter the message you want to send to {name}: ")


send_whatsapp_message(recipient_number, message_body)
