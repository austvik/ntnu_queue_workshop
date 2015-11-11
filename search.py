#!/usr/bin/env python
# encoding: utf-8

import json
from sys import argv

def file_content(filename):
    fh = open(filename)
    return fh.read()

word = argv[1]
letter = word[0]
filename = 'out/%s.txt' % letter

print('Searching for %s in %s' % (word, filename))

parsed = json.loads(file_content(filename))

if word in parsed:
    print('Found!')
    occs = parsed[word]
    for occ in sorted(occs, key=lambda k: k['wordcount'], reverse=True):
        print('- %s (%d)' % (occ['path'], occ['wordcount']))
else:
    print('Not found :(')


