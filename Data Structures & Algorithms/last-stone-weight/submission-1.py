class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        first = 0
        second = 0
        tmp_list = []

        def insertSort(value):
            nonlocal tmp_list
            if value == 0:
                return
            if len(tmp_list) > 0:
                for i in range(len(tmp_list)):
                    if tmp_list[i] < value:
                        tmp_list.insert(i - 1, value)
                        return
            tmp_list.append(value)

        while len(stones) > 1:
            for s in stones:
                if s > first:
                    insertSort(second)
                    second = first
                    first = s
                elif s > second:
                    insertSort(second)
                    second = s
                else:
                    insertSort(s)
            insertSort(first - second)
            first = 0
            second = 0
            stones = [*tmp_list]
            tmp_list = []

        if len(stones) == 0:
            return 0
        return stones[0]