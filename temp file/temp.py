import random

DISK_SIZE = 200
HEAD_POSITION = 50


def generate_random_requests(n):
    return [random.randint(0, DISK_SIZE - 1) for _ in range(n)]


def C_SCAN(requests):
    current_position = HEAD_POSITION
    seek_count = 0
    seek_sequence = []
    worst_case_seek_time = 0

    left = [0]
    right = [DISK_SIZE - 1]

    for req in requests:
        if req < HEAD_POSITION:
            left.append(req)
        elif req > HEAD_POSITION:
            right.append(req)

    left.sort()
    right.sort()

    for track in right:
        seek_sequence.append(track)
        distance = abs(track - current_position)
        seek_count += distance
        worst_case_seek_time = max(worst_case_seek_time, distance)
        current_position = track

    current_position = 0
    seek_count += DISK_SIZE - 1

    for track in left:
        seek_sequence.append(track)
        distance = abs(track - current_position)
        seek_count += distance
        worst_case_seek_time = max(worst_case_seek_time, distance)
        current_position = track

    print("Total number of seek operations =", seek_count)
    print("Worst-case Seek Time =", worst_case_seek_time)
    print("Seek Sequence is", *seek_sequence)

    avg_seek_time = seek_count / len(requests)
    print("Average Seek Time =", avg_seek_time)


if __name__ == "__main__":
    request_sizes = [10, 20, 50, 100]

    for size in request_sizes:
        print(f"**********     C-SCAN     *********")
        print(f"Number of requests: {size}")
        requests = generate_random_requests(size)
        print("Randomly generated list of requests:", requests)
        C_SCAN(requests)
        print()
