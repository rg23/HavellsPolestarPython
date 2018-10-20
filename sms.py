# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACb2d934a903139b4d8d8d200889dc1265'
auth_token = '7c74b51471d59760b0dd7c1ab49060f8'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Hi. Whatsup?',
         from_='+14053478363',
         to='9873985883'
     )
# print(14)
print(message.sid)
