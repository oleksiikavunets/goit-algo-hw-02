from queue import Queue

queue = Queue()

total_requests = 0


def generate_request():
    global total_requests
    total_requests += 1
    request = f'Request: {total_requests}'
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
