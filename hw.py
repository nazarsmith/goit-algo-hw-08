import heapq

def heap_sort(iterable):
    h = [el for el in iterable]
    print("Heap of cables:", h)
    heapq.heapify(h)
    if len(h) == 1:
        return h
    else:

        combined_cable = [heapq.heappop(h) for _ in range(2)]
        print("Combined pair of shortest cables:", sum(combined_cable))
        heapq.heappush(h, sum(combined_cable))
        h = heap_sort(h)
        return h

cable_lengths = [2, 12, 11, 13, 5, 6, 7]
total_exp = total_len = sum(cable_lengths)
sorted_arr_asc = heap_sort(cable_lengths)
print("Combined final cable:", sorted_arr_asc)

