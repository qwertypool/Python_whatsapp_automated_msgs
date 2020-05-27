

from twilio.rest import Client                                  #pip install twilio
 
account_sid = 'AC00d51f0663ee1f916a6428838d9724b8' 
auth_token = 'YOUR AUTH TOKEN' 
client = Client(account_sid, auth_token) 
def msg():
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',     #twilio whatsapp number
                                body='Hey, time to code!',         #Message to be sent
                                to='whatsapp:PHONE NUMBER'         #whatsapp number 
                            ) 
    
    print(message.sid)
