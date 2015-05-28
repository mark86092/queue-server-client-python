#!/usr/bin/env python3
from multiprocessing.managers import BaseManager
import queue

if __name__ == '__main__':
    q = queue.Queue()

    # a QueueManager hold a queue q, which automatically handle race condition
    class QueueManager(BaseManager):
        pass
    QueueManager.register('get_queue', callable = lambda: q)

    m = QueueManager(address = ('0.0.0.0', 5000), authkey = b'qazwsxedc')
    s = m.get_server()
    s.serve_forever()
