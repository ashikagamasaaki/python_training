class ContextManager:
    def __enter__(self):
        # print('__enter__ was called')
        return 1
        
    def __exit__(self, exc_type, exc_value, traceback):
        # print('__exit__ was called')
        # print(f'{exc_type=}')
        # print(f'{exc_value=}')
        # print(f'{traceback=}')
        pass
        
with ContextManager() as f:
    print(f)
    print('inside the block')
    # 1 / 0


print('')
print('--------------------------------------------------------------------------------')
print('')
    
    
from contextlib import contextmanager

@contextmanager
def point(**kwargs):
    print('__enter__ was called')
    
    value = kwargs
    try:
        yield value
    except Exception as e:
        print(e)
        raise
    finally:
        print('__exit__ was called')
        print(value)
        

with point(x=1, y=2) as p:
    print(p)
    p['z'] = 3
    

print('')
print('--------------------------------------------------------------------------------')
print('')


import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

logger.setLevel(logging.INFO)

@contextmanager
def debug_context():
    level = logger.level
    try:
        logger.setLevel(logging.DEBUG)
        yield
    finally:
        logger.setLevel(level)
        
    
def main():
    logger.info('before: info log')
    logger.debug('before: debug log')
    
    with debug_context():
        logger.info('inside the block: info log')
        logger.debug('inside the block: debug log')
        
    logger.info('after: info log')
    logger.debug('after: debug log')
    

if __name__ == '__main__':
    main()