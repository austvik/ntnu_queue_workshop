Structured Content
==================

We want to put something else than just text into the message and work on them.

Adjust the message content so that it contains this data:
- *data* for the message
- *message_num* for numbering the message
- *timestamp* for when the message was added to the queue

Then place *3* messages on the queue for each invocation of the program

Hint:

```python
import json
print(json.dumps({'foo': 123, 'bar': 'def'}))
```
    {"bar": "def", "foo": 123}

Hint 2:

```python
import json
from datetime import datetime
print(json.dumps({'foo': '%s' % datetime.now()}))
```

    {"foo": "2015-11-07 20:30:18.954288"}

Hint 3:

```python
import json
print(json.loads('{""message_num"": 1, ""data"": ""123""}')['data'])"
```

    123

[Example Solution](../lf_structured_content.py)