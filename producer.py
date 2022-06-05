import pika, json

params = pika.URLParameters('amqps://liltmcjs:uuslkpHY75_na5OufuekpazLaon1uR8H@rat.rmq2.cloudamqp.com/liltmcjs')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
