Batching
========

Now we write one and one message to the queue, but the queue supports 48/64kb of data.

Rewrite the producers and consumers so that they write many messages in each queue message by e.g. writing a list of json objects.