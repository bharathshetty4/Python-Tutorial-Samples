import pika
import logging

logging.basicConfig(filename = 'r.log',level=logging.WARNING)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',routing_key='hello',body="HELLO world")

print("Send 'HELLO world'")
connection.close()
