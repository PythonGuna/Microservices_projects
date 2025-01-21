
import pika,json 

params = pika.URLParameters('amqps://hceffqai:5o7j-fzKtnEt8InVt6ypIwVXbsXUJhLp@rabbit.lmq.cloudamqp.com/hceffqai')
connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='',routing_key='main',body=json.dumps(body),properties=properties)


