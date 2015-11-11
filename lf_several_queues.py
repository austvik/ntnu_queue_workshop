#!/usr/bin/env python
# encoding: utf-8

from azure.storage.queue import QueueService
from datetime import datetime
from common.common import *
import threading
import json
import random

def connect_queue():
    queue_service = QueueService(ACCOUNT_NAME, ACCOUNT_KEY)
    return queue_service

def create_queue(queue_service, queue_num):
    name = queue_name(queue_num)
    print('Creating queue %s' % name)
    queue_service.create_queue(name)
    
def queue_name(queue_num):
    return '%s-%d' % (QUEUE_NAME, queue_num)

def random_queue_name(num_queues):
    q = random.randint(0, num_queues-1)
    return queue_name(q)

def producer(producer_num, num_to_produce, num_queues):
    for i in range(0, num_to_produce):
        content = {'data': producer_num * 10 + i, 'message_num': i, 'timestamp:': "%s" % datetime.now()}
        name = random_queue_name(num_queues)
        queue_service.put_message(name, json.dumps(content))

def consumer(consumer_num, queues_to_check):
    for queue in queues_to_check:
        check_queue(queue)

def check_queue(queue):
    while True:
        messages = queue_service.get_messages(queue, 32)
        for message in messages:
            parsed = json.loads(message.message_text)
            num = int(parsed['data'])
            print('Comsumer %d reading from %s: %02d' % (consumer_num, queue, num));
            queue_service.delete_message(queue, message.message_id, message.pop_receipt)
                
        if (len(messages) == 0):
            break


num_consumers = 5
num_producers = 3
num_to_produce = 10
num_queues = 3

queue_service = connect_queue();

all_queues = []
for q in range(0, num_queues):
    create_queue(queue_service, q);
    all_queues.append(queue_name(q))

for p in range(0, num_producers):
    t = threading.Thread(target=producer, args=(p, num_to_produce, num_queues))
    t.start()
    
for c in range(0, num_consumers):
    t = threading.Thread(target=consumer, args=(c,random.sample(all_queues, len(all_queues))))
    t.start()

