#!/usr/bin/env python
# encoding: utf-8

#
# Please name your queue uniquely so that you are not working on anybody elses data
#
QUEUE_NAME = 'examplequeue'

#
# This is the account key, please add the missing data
#
ACCOUNT_KEY = 'VuEB6Y??OJ9M9xwTQif3FBwKGKrMP+xCgjiG7vCfb6zqFWzTWEW1stXMgcxyq8fUB0pa0Xb1OpG7YTLRTfbfKw=='

#
# Account name should not be changed
#
ACCOUNT_NAME = 'ntnuqueueworkshop'

from azure.storage.queue import QueueService

def get_queue_service():
    "Returns the QueueService that can be used to put, peek, get and delete messages"
    queue_service = QueueService(ACCOUNT_NAME, ACCOUNT_KEY)
    queue_service.create_queue(QUEUE_NAME)
    return queue_service

