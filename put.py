from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass
QueueManager.register('get_queue')

m = QueueManager(address=('140.112.187.33', 5000), authkey=b'qazwsxedc')
m.connect()

queue = m.get_queue()

# do anything you want to put the item into queue
# eg: queue.put('example')
