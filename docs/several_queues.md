Several Queues
==============

With just one Queue, that could become the bottleneck.

In this task we will create several queues (lets say 3), and each producer should put the queue elements on a random queue. name the queues in a unique (for you) way.

The Consumers will check the queues in a random order so that all consumers check all queues (and nothing is left behind).

Hint 1:

```python
import random

def random_queue_name(num_queues):
    q = random.randint(0, num_queues-1)
    return queue_name(q)
```

Hint 2:

```python
def connect_queue():
    queue_service = QueueService(ACCOUNT_NAME, ACCOUNT_KEY)
    return queue_service

def create_queue(queue_num):
    queue_service.create_queue(queue_name(queue_num))
```

[Example Solution](../lf_several_queues.py)