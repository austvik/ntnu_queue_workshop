MapReduce
=========

Now we have all the tools we need to create a killer search engine.

First you'll create one producer that reads the docs/ directory and stores the files in this directory to one of *c* queues with *file name* and *content*.

Then you will have *m* consumers (Mappers) that read from the queues, and stores **word** and **document** to another set of queues. Here each first letter of the word (a-z0-9) should be written to a separate queue.

For the last queue, the *r* Reducers will read from a set of all the letter queues and generate a file in the *out* directory called *letter*.txt where all the words on this letter are writter with occurrences and which document they existed in.

Example:
```
   out/s.json

   {
   "search": [{"wordcount": 1, "path": "docs/mapreduce.md"}]
   "something": [{"wordcount": 1, "path": "docs/structured_content.md"}, {"wordcount": 1, "path": "docs/mapreduce.md"}]
   }
```

You can test it out with

```
python search.py search
```

Hint 1:

Find files you want:

```python
from os import listdir
from os.path import isfile, join

def files_in_dir(path):
    return [ join(path, f) for f in listdir(path) if isfile(join(path, f)) and f.endswith('.md') and not f.startswith('.') ]
```

Hint 2:

Read a file:

```python
def file_content(filename):
    fh = open(filename)
    return fh.read()
```

Hint 3:

Get words of text:

```python
def words(text):
    return re.sub("[^a-z0-9]", " ",  text.lower()).split()
```

Hint 4:

Write a structure to JSON:

```python
def write_json(filename, content):
    outfile = open(filename, 'w+')
    outfile.write(json.dumps(content))
    outfile.close();
```
    
Hint 5:

Slice a list into *cols* lists:

```python
def slice(list, cols=2):
    start = 0
    for i in range(cols):
        stop = start + len(list[i::cols])
        yield list[start:stop]
        start = stop
```

[Example Solution](../lf_mapreduce.py)