from __future__ import print_function
from telesign.messaging import MessagingClient

customer_id = "id_here" 
api_key = "api_key_here"

phone_number = "57322004066"   
message = "Hello sending message with Python"  #Mensaje que se envia
message_type = "ARN"

messaging = MessagingClient(customer_id, api_key)
response = messaging.message(phone_number, message, message_type)