# coding :  UTF-8

import heapq

class SelfHeap:
    @staticmethod
    def heappush(q, v):
        q.append(v)
        new_index = len(q) - 1
        while new_index > 0:
            parent_index = (new_index - 1) // 2
            if q[parent_index] > q[new_index]:
                q[parent_index], q[new_index] = q[new_index], q[parent_index]
                new_index = parent_index
            else:
                break
    
    @staticmethod
    def heappop(q):
        min_value = q[0]
        last_element = q.pop()
        if q:
            q[0] = last_element

        index = 0
        while True:
            left_index  = 2 * index + 1
            right_index = 2 * index + 2
            smallest = index
            if left_index < len(q) and q[left_index] < q[smallest]:
                smallest = left_index
            if right_index < len(q) and q[right_index] < q[smallest]:
                smallest = right_index
            if smallest == index:
                break
            q[index], q[smallest] = q[smallest], q[index]
            index = smallest

        return min_value

def operate_selfheapq () :
    l = [1, 3, 6, 4, 8, 7]
    q = []

    for v in l:
        SelfHeap.heappush(q, v)
        print("push",v, q)

    for _ in l:
        min_value = SelfHeap.heappop(q)
        print("pop", min_value, q)


def operate_heapq ():
    # Preset Heapq Ver.
    q = []
    l = [1, 3, 6, 4, 8, 7]

    for v in l:
        heapq.heappush(q,v)
        print("push", q)

    for _ in l:
        min_value = heapq.heappop(q)
        print("pop", min_value, q)

def main():
    operate_selfheapq()
    print("===")
    operate_heapq()

if __name__ == "__main__":
    main()