import random

# hp is initial head position
# and requests is the list of requests
# no of cylinders is 200
DISK_SIZE = 200
HEAD_POSITION = 50


def generate_random_requests(n):
    return [random.randint(0, DISK_SIZE - 1) for _ in range(n)]


def C_SCAN(reqs):
    requests = reqs.copy()
    current_position = HEAD_POSITION
    time = 0
    # end=199
    # start=0
    seek_count = 0
    left = []
    right = []
    seek_sequence = []
    worst_case_seek_time = 0

    left.append(0)
    right.append(DISK_SIZE - 1)

    for i in range(len(requests)):
        if requests[i] < HEAD_POSITION:
            left.append(requests[i])
        if requests[i] > HEAD_POSITION:
            right.append(requests[i])

    left.sort()
    right.sort()
    # print("left: ", left)
    # print("right: ", right)

    # track movement from head position to right
    for i in range(len(right)):
        cur_track = right[i]

        seek_sequence.append(cur_track)

        # Calculate absolute distance
        distance = abs(cur_track - current_position)

        # Increase the total count
        seek_count += distance

        worst_case_seek_time = max(worst_case_seek_time, distance)

        # Accessed track is now new head
        current_position = cur_track

    current_position = 0

    seek_count += DISK_SIZE - 1

    # track movement from head position to right
    for i in range(len(left)):
        cur_track = left[i]

        seek_sequence.append(cur_track)

        # Calculate absolute distance
        distance = abs(cur_track - current_position)

        # Increase the total count
        seek_count += distance

        worst_case_seek_time = max(worst_case_seek_time, distance)

        # Accessed track is now new head
        current_position = cur_track

    print("Total number of seek operations =", seek_count)
    print("Worst-case Seek Time =", worst_case_seek_time)
    print("Seek Sequence is")
    print(*seek_sequence, sep=" ")

    # seek from curr_pos to end which is 200
    # for i in range(pos,end+1):
    # 	if i in requests:
    # 		time+=abs(pos-i)
    # 		pos=i
    # 		print("        ",i,"  seeked")
    # 		requests.remove(i)
    # time+=abs(pos-end)
    # pos=end
    # #seek to hp from start
    # for i in range(start,hp+1):
    # 	if i in requests:
    # 		time+=abs(pos-i)
    # 		pos=i
    # 		print("        ",i,"  seeked")
    # 		requests.remove(i)

    # # calculate average seek time
    # # avg_seek_time = time/n
    avg_seek_time = seek_count / len(reqs)
    print("Average Seek Time =", avg_seek_time)
    # return avg_seek_time


if __name__ == "__main__":
    # n = 8
    # hp = 50
    # requests = [176, 79, 34, 60, 92, 11, 41, 114]
    request_sizes = [10, 20, 50, 100]

    for size in request_sizes:
        print(f"**********     C-SCAN     *********")
        print(f"Number of requests: {size}")
        requests = generate_random_requests(size)
        print("Randomly generated list of requests:", requests)
        C_SCAN(requests)
        print()
    # # num_requests = 8
    # requests = generate_random_requests(num_requests)
    # print("Randomly generated list of requests:", requests)

    # print("DISK SCHEDULING:")
    # print("Provide number of I/O requests")
    # n is the number of I/O requests
    # n = int(input())
    # print("Provide initial position of disc arm (total cylinders=200)")
    # hp = int(input())
    # while hp>200:
    # 	print("!!! INVALID !!! try again")
    # 	hp = int(input())
    # print("Provide positions to visit : max is 200")
    # requests = []
    # for i in range(n):
    # 	req = int(input())
    # 	requests.append(req)

    # print(requests)

    # calling the functions
    # print("  **********     C-SCAN     *********")
    # print("Avg seek time for  C-scan was ",
    # 	C_SCAN(requests))
    # C_SCAN(requests)
