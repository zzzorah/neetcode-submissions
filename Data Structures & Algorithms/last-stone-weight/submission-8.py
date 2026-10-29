class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    def doSwap(i: int):
      left = 2 * i + 1
      right = left + 1

      # both left and right exist
      if right < n:
        # left is the biggest
        if stones[left] > stones[i] and stones[left] > stones[right]:
          stones[i], stones[left] = stones[left], stones[i]
        # right is the biggest
        elif stones[right] > stones[i] and stones[right] > stones[left]:
          stones[i], stones[right] = stones[right], stones[i]
      # only left exist
      elif left < n and stones[left] > stones[i]:
        stones[i], stones[left] = stones[left], stones[i]

    def heapify():
      if n <= 1:
        return

      i = (n - 2) // 2
      while i >= 0:
        sift(i)
        i -= 1


    def sift(i: int):
      nonlocal n

      left = 2 * i + 1
      right = left + 1

      # both left and right exist
      if right < n:
        # left is the biggest
        if stones[left] > stones[i] and stones[left] >= stones[right]:
          stones[i], stones[left] = stones[left], stones[i]
          sift(left)
        # right is the biggest
        elif stones[right] > stones[i] and stones[right] >= stones[left]:
          stones[i], stones[right] = stones[right], stones[i]
          sift(right)
      # only left exist
      elif left < n and stones[left] > stones[i]:
        stones[i], stones[left] = stones[left], stones[i]
        sift(left)
      else:
        return

    n = len(stones)
    heapify()
    print(f"After heapity\nstones={stones}")

    buffer = []
    while (n >= 2) or (len(buffer) == 1 and n > 0):
      buffer.append(stones[0])
      print(f"buffer={buffer}")
      if len(buffer) < 2:
        stones[0] = stones.pop()
        n -= 1
      else:
        diff = buffer[0] - buffer[1]
        if diff > 0:
          stones[0] = diff
        else:
          if n > 1:
            stones[0] = stones.pop()
          else:
            stones.pop()
          n -= 1
        buffer = []

      print(f"Before: {stones}")
      sift(0)
      print(f"After: {stones}")

    if n == 0:
      return 0
    else:
      return stones[0]
