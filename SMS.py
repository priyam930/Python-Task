#pip install twilio
from twilio.rest  import Client

account_sid = 'your account sid'
auth_tocken = "your auth tocken"

client = Client(account_sid, auth_tocken)
number = input("Enter the recepient number:")
messages = input("Enter the message you want to send:")

message = client.messages.create(
    body=messages,
    from_="your twilio number",
    to=number,
)

