#!/usr/bin/env python
# encoding: utf-8

from os import listdir
from os.path import isfile, join
from azure.storage.queue import QueueService
from datetime import datetime
from common.common import *
import threading
import json
import random
import re

def connect_queue():
    queue_service = QueueService(ACCOUNT_NAME, ACCOUNT_KEY)
    return queue_service

def create_queue(queue_service, name):
    print('Creating queue %s' % name)
    queue_service.create_queue(name)
    
def queue_name(queue_num):
    return '%s-d-%d' % (QUEUE_NAME, queue_num)

def queue_name_for_word(word):
    return '%s-q-%s' % (QUEUE_NAME, word[0])

def random_queue_name(num_queues):
    q = random.randint(0, num_queues-1)
    return queue_name(q)

def crawler(path, num_queues):
    files = files_in_dir(path)
    for filename in files:
        print('Crawling %s' % filename)
        text = file_content(filename)
        content = {'file': filename, 'text': text, 'timestamp:': "%s" % datetime.now()}
        queue = random_queue_name(num_queues)
        queue_service.put_message(queue, json.dumps(content))

def mapper(mapper_num, queues_to_check):
    for queue in queues_to_check:
        check_mapper_queue(mapper_num, queue)

def check_mapper_queue(mapper_num, read_queue):
    while True:
        messages = queue_service.get_messages(read_queue, 32)
        for message in messages:                
            parsed = json.loads(message.message_text)
            try:
                filename = parsed['file']
            except:
                print(message.message_text)
            
            print('Mapper %d reading from %s: %s' % (mapper_num, read_queue, filename))

            wordcounts = {}
            for word in words(parsed['text']):
                if word in wordcounts:
                    wordcounts[word] += 1
                else:
                    wordcounts[word] = 1

            for word in wordcounts.keys():
                write_queue = queue_name_for_word(word)
                content = {'file': filename, 'word': word, 'count': wordcounts[word]}
                queue_service.put_message(write_queue, json.dumps(content))

            queue_service.delete_message(read_queue, message.message_id, message.pop_receipt)

        if (len(messages) == 0):
            break

def index_writer(path, queues_to_check):
    for queue in queues_to_check:
        check_index_queue(path, queue)
    
def check_index_queue(path, read_queue):
    print('Reducer reading from %s' % (read_queue))

    words = {}
    while True:
        messages = queue_service.get_messages(read_queue, 32)
        for message in messages:
            parsed = json.loads(message.message_text)
            try:
                filename = parsed['file']
                word = parsed['word']
                count = int(parsed['count'])
            except:
                print(message.message_text)

            content = {'wordcount': count, 'path': filename}
            if word in words:
                words[word].append(content)
            else:
                words[word] = [content]

            queue_service.delete_message(read_queue, message.message_id, message.pop_receipt)
                
        if (len(messages) == 0):
            break

    letter = read_queue[-1:]
    filename = '%s/%s.txt' % (path, letter)
    write_json(filename, words)
    
def write_json(filename, content):
    outfile = open(filename, 'w+')
    outfile.write(json.dumps(content))
    outfile.close();
    
def files_in_dir(path):
    return [ join(path, f) for f in listdir(path) if isfile(join(path, f)) and f.endswith('.md') and not f.startswith('.') ]

def file_content(filename):
    fh = open(filename)
    return fh.read()

def words(text):
    return re.sub("[^a-z0-9]", " ",  text.lower()).split()

def slice(list, cols=2):
    start = 0
    for i in range(cols):
        stop = start + len(list[i::cols])
        yield list[start:stop]
        start = stop
    
num_crawlers = 1
num_queues = 3
num_mappers = 5
num_index_writers = 7

queue_service = connect_queue()

all_queues = []
for q in range(0, num_queues):
    name = queue_name(q)
    create_queue(queue_service, name)
    all_queues.append(name)

letter_queues = []
for l in range(ord('a'), ord('z') + 1):
    name = queue_name_for_word(chr(l))
    create_queue(queue_service, name)
    letter_queues.append(name)

for l in range(ord('0'), ord('9') + 1):
    name = queue_name_for_word(chr(l))
    create_queue(queue_service, name)
    letter_queues.append(name)

c = threading.Thread(target=crawler, args=('docs', num_queues))
c.start()

for m in range(0, num_mappers):
    t = threading.Thread(target=mapper, args=(m, random.sample(all_queues, len(all_queues))))
    t.start()

queue_slices = list(slice(letter_queues, num_index_writers))
for m in range(0, num_index_writers):
    my_queues = queue_slices[m]
    t = threading.Thread(target=index_writer, args=('out', random.sample(my_queues, len(my_queues))))
    t.start()

