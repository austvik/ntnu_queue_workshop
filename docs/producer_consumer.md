Producer/Consumer
=================

We are going to implement the standard producer/consumer pattern with one thread per consumer or producer.

Make *p* producer threads that each put *n* elements on the queue. Make it possible to identify which producer placed the given element on the queue.

Make *c* consumers that reads from the queue and prints the output until it is no more to read.

Hint 1:

Threading in Python:

```python
import threading

def consumer(consumer_num):
    while True:
        messages = queue_service.get_messages(QUEUE_NAME, 32)
	...
        if (len(messages) == 0) :
            break

for c in range(0, num_consumers):
    t = threading.Thread(target=consumer, args=(c,))
    t.start()
```

[Example Solution](../lf_producer_consumer.py)