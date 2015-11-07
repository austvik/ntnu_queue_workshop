#!/usr/bin/env python
# encoding: utf-8

from azure.storage.queue import QueueService
from datetime import datetime
import json
from common.common import *

print('Sample solution for structured content')

queue_service = get_queue_service()

for i in range(0, 3):
    content = {'data': '123', 'message_num': i, 'timestamp:': "%s" % datetime.now()}
    queue_service.put_message(QUEUE_NAME, json.dumps(content))

messages = queue_service.get_messages(QUEUE_NAME, 10)
print('Queue contains %d message(s)' % len(messages))

sum = 0
for message in messages:
    parsed = json.loads(message.message_text)
    sum += int(parsed['data'])

    queue_service.delete_message(QUEUE_NAME, message.message_id, message.pop_receipt)

print('Sum: %s' % sum)
