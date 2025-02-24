class solution:
    def qsort(self, arr, li, ri):
        if li < ri:
            pvt_id = self.pivot(arr, li, ri)
            self.qsort(arr, li, pvt_id-1)
            self.qsort(arr, pvt_id+1, ri)

    def pivot(self, arr, pvt_id, end_id):
        swap_id = pvt_id
        for i in range(pvt_id+1, end_id+1):
            if arr[i] < arr[pvt_id]:
                swap_id += 1
                arr[swap_id], arr[i] = arr[i], arr[swap_id]
        arr[pvt_id], arr[swap_id] = arr[swap_id], arr[pvt_id]
        return swap_id


if __name__ == "__main__":
    s = solution()
    arr = [3, 6, 8, 10, 1, 2, 1]
    print("Original array:", arr)
    s.qsort(arr, 0, len(arr)-1)
    print("Sorted array:", arr)