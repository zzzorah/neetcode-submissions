class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    def heapify():
      if n <= 1:
        return

      i = (n - 2) // 2
      while i >= 0:
        sift(i)
        i -= 1


    def sift(i: int):
      while True:
        largest = i
        left, right = 2 * i + 1, 2 * i + 2
        if left < n and stones[left] > stones[largest]:
            largest = left
        if right < n and stones[right] > stones[largest]:
            largest = right
        if largest == i:
            return
        stones[i], stones[largest] = stones[largest], stones[i]
        i = largest


    n = len(stones)
    heapify()

    buffer = []
    while n > 1:
      a = stones[0]
      stones[0] = stones.pop(); n -= 1
      sift(0)

      b = stones[0]
      diff = a - b
      if diff > 0:
        stones[0] = diff
      else:
          last = stones.pop(); n -= 1
          if n > 0:
              stones[0] = last
      sift(0)

    if n == 0:
      return 0
    else:
      return stones[0]
