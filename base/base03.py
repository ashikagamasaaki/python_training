import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1():
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')

def worker2(x, y=1):
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')
    

if __name__ == '__main__':
    t1 = threading.Thread(name='rename workder1', target=worker1)
    t2 = threading.Thread(target=worker2, args=(100, ), kwargs={'y': 200})
    t1.start()
    t2.start()
    print('started')