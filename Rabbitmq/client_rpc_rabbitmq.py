import pika, uuid, sys

if (len(sys.argv))!= 2:
   print "not passing arguments, pass one"
   sys.exit(1)


class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response, no_ack = True, queue=self.callback_queue)

    def on_response(self,ch,method,props,body):
        if self.corr_id ==props.correlation_id:
            self.response = body

    def __call__(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange= '',routing_key='rpc_queue', properties=pika.BasicProperties(reply_to = self.callback_queue,correlation_id = self.corr_id,),body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)

fibonacci_rpc = FibonacciRpcClient() 
n = int(sys.argv[1])
print ("[x] Requesting fib (%d)" %n )
response = fibonacci_rpc.__call__(n)
print(" [.] Got %r "% response)
