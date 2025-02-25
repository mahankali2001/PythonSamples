import heapq


class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and 
                    self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            if (right_index < len(self.heap) and 
                    self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
                       
    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value
    
class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and 
                    self.heap[left_index] < self.heap[max_index]):
                max_index = left_index

            if (right_index < len(self.heap) and 
                    self.heap[right_index] < self.heap[max_index]):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

                       
    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value
























def find_kth_largestwitheapq(nums, k):
    min_heap = nums[:k] #first k-elements
    heapq.heapify(min_heap) #convert into min-heap 0(k)
    
    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
    return min_heap[0]

print("***********************find_kth_largestwitheapq - Test cases")
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 3
print(find_kth_largestwitheapq(nums, k))

def find_kth_smallest(nums, k):
    max_heap = MaxHeap()
    for num in nums:
        max_heap.insert(num)
        if len(max_heap.heap) > k:
            max_heap.remove()

    return max_heap.remove()

# Test cases
print("***********************find_kth_smallest - Test cases")
nums = [[3,2,1,5,6,4], [6,5,4,3,2,1], [1,2,3,4,5,6], [3,2,3,1,2,4,5,5,6]]
ks = [2, 3, 4, 7]
expected_outputs = [2, 3, 4, 5]

for i in range(len(nums)):
    print(f'Test case {i+1}...')
    print(f'Input: {nums[i]} with k = {ks[i]}')
    result = find_kth_smallest(nums[i], ks[i])
    print(f'Output: {result}')
    print(f'Expected output: {expected_outputs[i]}')
    print(f'Test passed: {result == expected_outputs[i]}')
    print('---------------------------------------')


def find_kth_largest(nums, k):
    min_heap = MinHeap()
    for num in nums:
        min_heap.insert(num)
        if len(min_heap.heap) > k:
            min_heap.remove()

    return min_heap.remove()

# Test cases
print("***********************find_kth_largest - Test cases")
nums = [[3,2,1,5,6,4], [6,5,4,3,2,1], [1,2,3,4,5,6], [3,2,3,1,2,4,5,5,6]]
ks = [2, 3, 4, 7]
expected_outputs = [2, 3, 4, 5]

for i in range(len(nums)):
    print(f'Test case {i+1}...')
    print(f'Input: {nums[i]} with k = {ks[i]}')
    result = find_kth_largest(nums[i], ks[i])
    print(f'Output: {result}')
    print(f'Expected output: {expected_outputs[i]}')
    print(f'Test passed: {result == expected_outputs[i]}')
    print('---------------------------------------')

def stream_max(nums):
    max_heap = MaxHeap()
    stream_max = []
    for num in nums:
        max_heap.insert(num)
        stream_max.append(max_heap.heap[0])
    return stream_max

print("***********************stream_max - Test cases")
test_cases = [
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 2, 2, 1, 3, 3, 3, 2, 2], [1, 2, 2, 2, 3, 3, 3, 3, 3]),
    ([-1, -2, -3, -4, -5], [-1, -1, -1, -1, -1])
]

for i, (nums, expected) in enumerate(test_cases):
    result = stream_max(nums)
    print(f'\nTest {i+1}')
    print(f'Input: {nums}')
    print(f'Expected Output: {expected}')
    print(f'Actual Output: {result}')
    if result == expected:
        print('Status: Passed')
    else:
        print('Status: Failed')