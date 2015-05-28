#!/usr/bin/env python3
from multiprocessing.managers import BaseManager

# declare the QueueManager like server
class QueueManager(BaseManager):
    pass
# register method get_queue()
QueueManager.register('get_queue')

if __name__ == '__main__':
    server_address = ('140.112.187.33', 5000)
    authkey = b'qazwsxedc'
    m = QueueManager(address = server_address, authkey = authkey)
    m.connect()
    queue = m.get_queue()
    
    while True:
        try:
            item = queue.get()
        except KeyboardInterrupt: # Ctrl + C interrupt (i.e. want to exit)
            break

        ## do anything about your item
        try:
            print(item)
        except KeyboardInterrupt: # Ctrl + C interrupt (i.e. want to exit)
            # requeue your item, because fail to finish it
            queue.put(item)
            # break the while loop
            break
        except:
            pass ## catch the other exception, and handle it
