import json

import pika

from twilioHandler import TwilioClient

client = TwilioClient()


def make_sms_notification(ch, method, properties, body):
    """
        Send SMS notification using Twilio API
    """
    print(f" [x] Received {body}")
    # Send SMS notification using Twilio API
    user_data = json.loads(body)

    to = user_data.get('phone')
    message = f"Hola {user_data.get('name')} {user_data.get('last_name')}. Felicidades! tu oferta de tarjeta de crédito con id {user_data.get('offer_id')} ha sido aceptada. Por favor verifica tu correo {user_data.get('email')} Para más detalles. \n\nGracias por confiar en nosotros, Banco de los Alpes"
    client.send_message(to, message)

    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)
