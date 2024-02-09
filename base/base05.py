from hashlib import md5
from pathlib import Path
from urllib import request
import time

from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed
)


urls = [
    'https://facebook.com',
    'https://instagram.com'
]


def elapsed_time(f):
    def wrapper(*args, **kwargs):
        st = time.time()
        v = f(*args, **kwargs)
        print(f'{f.__name__}: {time.time() - st}')
        return v
    return wrapper

def download(url):
    req = request.Request(url)
    name = md5(url.encode('utf-8')).hexdigest()
    file_path = './' + name
    with request.urlopen(req) as res:
        Path(file_path).write_bytes(res.read())
        return url, file_path

@elapsed_time
def get_sequential():
    for url in urls:
        print(download(url))
        
@elapsed_time
def get_multi_thread():
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(download, url) for url in urls]
        
        for future in as_completed(futures):
            print(future.result())







if __name__ == '__main__':
    # get_sequential()
    get_multi_thread()