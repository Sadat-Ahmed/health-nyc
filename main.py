from kafka import KafkaProducer
from kafka import KafkaConsumer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

topic = 'topic1'
producer.send(topic, b't1')
producer.send(topic, b't2')


consumer = KafkaConsumer('sample',
                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'])
for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))