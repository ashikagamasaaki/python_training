from concurrent.futures import(
    ThreadPoolExecutor,
    wait
)

class Counter:
    def __init__(self):
        self.count =0
    
    def increment(self):
        self.count = self.count + 1
    
def count_up(counter):
    for _ in range(3000000):
        counter.increment()
        

if __name__ == '__main__':
    counter = Counter()
    threads = 4

    with ThreadPoolExecutor() as e:
        futures = [e.submit(count_up, counter) for _ in range(threads)]
        done, not_done = wait(futures)

    print(f'{counter.count=:,}')
