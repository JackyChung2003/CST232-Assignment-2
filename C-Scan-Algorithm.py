import random

# Disk drive with 200 cylinders (global constant variable)
DISK_SIZE = 200

# Current head position at cylinder 50 (global constant variable)
HEAD_POSITION = 50

# SCAN algorithm

# C-SCAN algorithm
def CSCAN(reqs):
    requests = sorted(reqs) # sort the requests
    position = HEAD_POSITION # start at the head position
    time = 0 # time starts at 0
    seek_count = 0      # not sure later need this or not
    distance = 0
    cur_track = 0
    left = []
    right = []
    seek_sequence = []

    # Seek from curr_pos to end which is 200
    for i in range(position, DISK_SIZE):
        if i in requests:
            
            time += abs(position - i)
            position = i
            print("        ", i, "  seeked")
            requests.remove(i)
            # seek_sequence.append(i)
            # seek_count += 1

    # If there are still requests, perform a wrap-around to the beginning
    if requests:
        position = 0
        time += abs(DISK_SIZE - 1 - HEAD_POSITION)

        # Seek to hp from start
        for i in range(0, HEAD_POSITION + 1):
            if i in requests:
                time += abs(position - i)
                position = i
                print("        ", i, "  seeked")
                requests.remove(i)

    # Calculate average seek time
    # avg_seek_time = time / len(reqs)
    avg_seek_time = time 
    print(f"C-SCAN Avg. Seek Time: {avg_seek_time:.2f} ms")
    # return avg_seek_time

    # print("        ", DISK_SIZE - 1, "  seeked")
            

# C-LOOK algorithm

# analyse their performance

# Run each algorithm with a set of 10, 20, 50, and 100 random requests.

arr = [176, 79, 34, 60, 92, 11, 41, 114] 


class DiskRequest:
    def __init__(self, cylinder):
        self.cylinder = cylinder

    def __lt__(self, other):
        # Define how instances should be compared for sorting
        return self.cylinder < other.cylinder
    
# Can we have any duplicates position in the list of requests?
def generate_requests(num_requests, num_cylinders):
    return [DiskRequest(random.randint(0, num_cylinders - 1)) for _ in range(num_requests)]


def main():
    request_sizes = [10, 20, 50, 100]

    for size in request_sizes:
        print(f"\nRunning experiments for {size} requests:")
        # requests = generate_requests(size, DISK_SIZE)
        requests = [DiskRequest(176), DiskRequest(79), DiskRequest(34), DiskRequest(60), DiskRequest(92), DiskRequest(11), DiskRequest(41), DiskRequest(114)]

        # print list of requests to check if they are correct
        # for req in requests:
        #     print(req.cylinder, end=' ')
        # print()
        # Print list of requests
        print("Requests:", [req.cylinder for req in requests])

        # SCAN
        # C-SCAN
        # CSCAN(request_sizes, requests)
        CSCAN(requests)

        # avg_seek_time = CSCAN(requests)
        # print(f"C-SCAN Avg. Seek Time ({size} requests): {avg_seek_time:.2f} ms")
        # C-LOOK


# Add an indented block of code here


# class DiskScheduler:
#     def scan(self, requests, start):
#         sorted_requests = sorted(requests, key=lambda x: x.cylinder)
#         left = [req for req in sorted_requests if req.cylinder <= start]
#         right = [req for req in sorted_requests if req.cylinder > start]
#         return left + right

#     def c_scan(self, requests, start):
#         sorted_requests = sorted(requests, key=lambda x: x.cylinder)
#         right = [req for req in sorted_requests if req.cylinder > start]
#         left = [req for req in sorted_requests if req.cylinder <= start]
#         return right + left

#     def c_look(self, requests, start):
#         sorted_requests = sorted(requests, key=lambda x: x.cylinder)
#         right = [req for req in sorted_requests if req.cylinder > start]
#         left = [req for req in sorted_requests if req.cylinder < start]
#         return right + left


# def generate_requests(num_requests, num_cylinders):
#     return [
#         DiskRequest(random.randint(0, num_cylinders - 1)) for _ in range(num_requests)
#     ]


# def calculate_seek_times(scheduler, requests, start):
#     scheduled_requests = scheduler(requests, start)
#     seek_times = [abs(request.cylinder - start) for request in scheduled_requests]
#     avg_seek_time = sum(seek_times) / len(seek_times)
#     worst_seek_time = max(seek_times)
#     return avg_seek_time, worst_seek_time


# def main():
#     num_cylinders = 200
#     start_position = 50
#     request_sizes = [10, 20, 50, 100]
#     num_experiments = 5

#     for size in request_sizes:
#         print(f"\nRunning experiments for {size} requests:")
#         total_avg_seek_time = 0
#         total_worst_seek_time = 0

#         for _ in range(num_experiments):
#             requests = generate_requests(size, num_cylinders)

#             scheduler = DiskScheduler()
#             avg_seek_time, worst_seek_time = calculate_seek_times(
#                 scheduler.scan, requests, start_position
#             )

#             total_avg_seek_time += avg_seek_time
#             total_worst_seek_time += worst_seek_time

#             print(
#                 f"Experiment {_ + 1}: Avg. Seek Time: {avg_seek_time:.2f}, Worst Seek Time: {worst_seek_time}"
#             )

#         avg_avg_seek_time = total_avg_seek_time / num_experiments
#         avg_worst_seek_time = total_worst_seek_time / num_experiments

#         print(f"Avg. Avg. Seek Time for {size} requests: {avg_avg_seek_time:.2f}")
#         print(f"Avg. Worst Seek Time for {size} requests: {avg_worst_seek_time:.2f}")


if __name__ == "__main__":
    main()

# +--------------------------+---------------+---------------+---------------+---------------+
# | Algorithm / Request Size |     10        |     20        |     50        |     100       |
# +--------------------------+---------------+---------------+---------------+---------------+
# | SCAN                     | Avg: x.xx ms  | Avg: x.xx ms  | Avg: x.xx ms  | Avg: x.xx ms  |
# |                          | Worst: x.xx ms| Worst: x.xx ms| Worst: x.xx ms| Worst: x.xx ms|
# +--------------------------+---------------+---------------+---------------+---------------+
# | C-SCAN                   | Avg: x.xx ms  | Avg: x.xx ms  | Avg: x.xx ms  | Avg: x.xx ms  |
# |                          | Worst: x.xx ms| Worst: x.xx ms| Worst: x.xx ms| Worst: x.xx ms|
# +--------------------------+---------------+---------------+---------------+---------------+
# | C-LOOK                   | Avg: x.xx ms  | Avg: x.xx ms  | Avg: x.xx ms  | Avg: x.xx ms  |
# |                          | Worst: x.xx ms| Worst: x.xx ms| Worst: x.xx ms| Worst: x.xx ms|
# +--------------------------+---------------+---------------+---------------+---------------+