#!/usr/bin/env python
# encoding: utf-8

from azure.storage.queue import QueueService
from datetime import datetime
from common.common import *
import threading
import json

queue_service = get_queue_service()

def producer(producer_num, num_to_produce):
    for i in range(0, num_to_produce):
        content = {'data': producer_num * 10 + i, 'message_num': i, 'timestamp:': "%s" % datetime.now()}
        queue_service.put_message(QUEUE_NAME, json.dumps(content))

def consumer(consumer_num):
    while True:
        messages = queue_service.get_messages(QUEUE_NAME, 32)
        for message in messages:
            parsed = json.loads(message.message_text)
            num = int(parsed['data'])
            print('Comsumer %d: %02d' % (consumer_num, num));
            queue_service.delete_message(QUEUE_NAME, message.message_id, message.pop_receipt)

        if (len(messages) == 0) :
            break
        

num_consumers = 5
num_producers = 3
num_to_produce = 10

for p in range(0, num_producers):
    t = threading.Thread(target=producer, args=(p, num_to_produce))
    t.start()

for c in range(0, num_consumers):
    t = threading.Thread(target=consumer, args=(c,))
    t.start()

