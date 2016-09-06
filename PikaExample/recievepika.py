import pika

def callback(ch, method, properties, body):
	print "Recieved %r" % body
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_consume(callback, queue='hello', no_ack=True)

print "waiting,press ctrl+C"
channel.start_consuming()
