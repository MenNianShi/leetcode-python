class Solution:
    def magicTower(self, nums: List[int]) -> int:
        n = len(nums)

        cur_sum = 0  # 当前和
        time = 0  # 把负数往后扔的次数
        minSum = 0  # 负数的abs值
        minHeap = []  # 最小堆。每次把最小的负数，扔到后面去

        for i in range(n):
            cur_sum += nums[i]  # 当前和

            if nums[i] < 0:  # 所有的负数，都进堆
                heapq.heappush(minHeap, nums[i])

            if cur_sum < 0:  # 当前卡住了。需要把前面经历过的这些负数中，扔一个最小的到后面
                cur_min = heapq.heappop(minHeap)

                minSum -= cur_min  # 这些扔到后面的，眼前跳过了，在最后还是要掉血
                cur_sum -= cur_min  # 扔掉这个最小的负数。cur_sum会变大
                time += 1  # 记录往后扔的次数

        if cur_sum < minSum:  # 如果正值，不能够把扔到末尾的负值抵消掉
            return -1
        return time
# LCP 30. 魔塔游戏.py