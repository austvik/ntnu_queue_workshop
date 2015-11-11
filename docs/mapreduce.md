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

Hint 1:

```python
from os import listdir
from os.path import isfile, join

def files_in_dir(path):
    return [ f for f in listdir(path) if isfile(join(path, f)) ]

```

[Example Solution](../lf_mapreduce.py)