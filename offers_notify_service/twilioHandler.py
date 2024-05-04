import os

from twilio.rest import Client


class TwilioClient:

    def __init__(self):
        self._account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self._auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self._from = os.getenv("TWILIO_PHONE_NUMBER")

        self.client = Client(self._account_sid, self._auth_token)

    def send_message(self, to, body):
        try:
            message = self.client.messages.create(
                from_=self._from,
                to=to,
                body=body
            )
        except Exception as e:
            print(e)
            return message.sid

        return message.sid
