import os

import pika


class PikaHandler:

    def __init__(self):
        self._connection_params = pika.ConnectionParameters(os.getenv('RABBITMQ_HOST'))
        self.connection = None
        self.channel = None
        self.queue_name = None

    def open_connection(self):
        self.connection = pika.BlockingConnection(self._connection_params)
        self.channel = self.connection.channel()

    def declare_queue(self, queue_name, durable=False):
        self.channel.queue_declare(queue=queue_name, durable=durable)
        self.queue_name = queue_name

    def send_json_message(self, message):
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            body=message,
            properties=pika.BasicProperties(
                content_type='application/json',
                delivery_mode=2
            )
        )

    def close_connection(self):
        self.connection.close()
