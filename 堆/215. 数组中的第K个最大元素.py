#快排
class Solution:
    def findKthLargest(self, nums, k) :
        def partition(left, right):
            pivot = nums[left]
            l = left + 1
            r = right
            while l <= r:
                if nums[l] < pivot and nums[r] > pivot:
                    nums[l], nums[r] = nums[r], nums[l]
                if nums[l] >= pivot:
                    l += 1
                if nums[r] <= pivot:
                    r -= 1
            nums[r], nums[left] = nums[left], nums[r]
            return r
        left = 0
        right = len(nums) - 1
        while 1:
            idx = partition(left, right)
            if idx == k - 1:
                return nums[idx]
            if idx < k - 1:
                left = idx + 1
            if idx > k - 1:
                right = idx - 1
#堆
class Solution:
    def findKthLargest(self, nums, k):
        def createHeap(data, end):
            begin = (end - 1) // 2
            for i in range(begin, -1, -1):
                adjustHeap(nums, i, end)

        def adjustHeap(data, start, end):
            cur = start
            while cur <= end:
                # 交换元素
                leftChild = cur * 2 + 1
                rightChild = cur * 2 + 2
                if rightChild <= end:  # 左右子结点都存在
                    if data[rightChild] <= data[leftChild] and data[rightChild] < data[cur]:  # 右子结点
                        data[cur], data[rightChild] = data[rightChild], data[cur]
                        cur = cur * 2 + 2
                    elif data[leftChild] <= data[rightChild] and data[leftChild] < data[cur]:  # 左子结点
                        data[cur], data[leftChild] = data[leftChild], data[cur]
                        cur = cur * 2 + 1
                    else:
                        break
                elif leftChild <= end and data[cur] > data[leftChild]:  # 只左子结点存在
                    data[cur], data[leftChild] = data[leftChild], data[cur]
                    cur = cur * 2 + 1
                else:
                    break

        length = len(nums)
        createHeap(nums, k-1)  # 创建最小堆
        # 取第k个最大元素
        for i in range(k, length):
            # 若比最小堆的堆顶大，则交换元素
            if nums[0]<nums[i]:
                nums[0], nums[i] = nums[i], nums[0]
                # 调整堆
                adjustHeap(nums, 0, k-1)
        return nums[0]

# 215. 数组中的第K个最大元素.py