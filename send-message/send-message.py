import json
from twilio.rest import Client


with open("config.json") as json_data_file:
    config = json.load(json_data_file)
account_sid = config['TWILIO_ACCOUNT_SID']
auth_token = config['TWILIO_AUTH_TOKEN']
conversationSid = config['CONVERSATION_SID']
message_from = config['FROM']
message = config['MESSAGE']

client = Client(account_sid, auth_token)

message = client.conversations.conversations(conversationSid)\
    .messages.create(author=message_from, body=message, x_twilio_webhook_enabled='true')

print(message.sid)
