

from twilio.rest import Client 
 
account_sid = 'AC00d51f0663ee1f916a6428838d9724b8' 
auth_token = 'c61c4b228fbd9e3a01b0e7bdb30ff9ee' 
client = Client(account_sid, auth_token) 
def msg():
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Hey go and sleep',      
                                to='whatsapp:+918240901474' 
                            ) 
    
    print(message.sid)