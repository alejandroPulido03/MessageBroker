import os

import pika
from notifier import make_sms_notification

if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters(os.getenv('RABBITMQ_HOST')))
    channel = connection.channel()

    channel.queue_declare(queue='notify_service_queue', durable=True)
    print('[*] Waiting for messages. To exit press CTRL+C')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='notify_service_queue', on_message_callback=make_sms_notification)

    channel.start_consuming()
