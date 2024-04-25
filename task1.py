import time
from queue import Queue

queue = Queue()


def generate_request():
    request = f'Request: {time.time()}'
    queue.put(request)

    print(f'Request is added - {request}')


def process_request():
    if not queue.empty():
        request = queue.get()
        print(f'Request is processed - {request}')
    else:
        print('Requests queue is empty. Nothing to process....')


if __name__ == '__main__':
    while input('Continue? ').lower() != 'no':
        generate_request()
        process_request()
