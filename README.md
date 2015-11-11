NTNU Queue Workshop with Azure Storage Queues
=============================================

Getting Started
---------------

### 1. Install Git

    https://git-scm.com/downloads

### 2. Install Python

    https://www.python.org/downloads/

And verify that it is in your path:

    python --version
    Python 3.4.2

### 3. Instal Azure Storage SDK for Python

    pip install azure-storage

or see [https://github.com/Azure/azure-storage-python](azure-storage-python github page)

### 4. Download source

    git clone https://github.com/austvik/ntnu_queue_workshop.git

### 5. Fix the connection strings

In common/common.py:

Change QUEUE_NAME to something that is unique for you.

Change ACCOUNT_KEY: Replace ? with should be J (there are two of them).

### 6. Run the first simple test

    python getting_started.py

### 7. Start on the tasks

* [Task 1 - Structured Content](docs/structured_content.md)
* [Task 2 - Producers/Consumers](docs/producer_consumer.md)
* [Task 3 -- Several Queues](docs/several_queues.md)

References
----------

* [Python Azure client libraries](http://azure-storage.readthedocs.org/en/latest/)
* [Getting started with Azure Storage Queues in Python Blog](https://azure.microsoft.com/en-us/documentation/articles/storage-python-how-to-use-queue-storage/)
* [Azure Queues REST API](https://msdn.microsoft.com/en-us/library/azure/dd179363.aspx)
