#!/usr/bin/env python
# encoding: utf-8

from azure.storage.queue import QueueService
from datetime import datetime
from common.common import *

print('Sample program that demonstrates connection to Azure Queues')

print('1. First setting up connection...')
queue_service = get_queue_service()

print('2. Then putting a message on the queue..')
queue_service.put_message(QUEUE_NAME, 'Hello world @ %s' % datetime.now())

print('3. Reading the same(?) message off the queue...')
messages = queue_service.get_messages(QUEUE_NAME, 10)
print('4. Queue contains %d message(s):' % len(messages))

for message in messages:
    print('  - Queue says: "%s"' % message.message_text)

    # Try to comment out these lines to see what happens
    print('    (Deleting message since we are done with it)')
    queue_service.delete_message(QUEUE_NAME, message.message_id, message.pop_receipt)

print('5. Done')
