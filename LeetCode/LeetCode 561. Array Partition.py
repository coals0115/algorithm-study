from dataclasses import dataclass
from typing import List


# Q. n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.

@dataclass
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

    # 짝수 번째 값 계산
    def arrayPairSum_1(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n

        return sum

    def arrayPairSum_my(self, nums: List[int]) -> int:
        # min인데 가장 큰 수이려면.. 차이가 얼마 안 나는 숫자끼리 비교해야 함
        # 오름차순 정렬해서 2개 뽑아내기

        # 1. nums를 오름차순 정렬한다.
        nums.sort(reverse=True)
        print(nums)

        # 2. pair 수를 구한다.
        pair = len(nums) // 2

        # 3. pair 수 만큼 for문 돌려서 min(a, b) 합 구하기
        result = 0
        for i in range(pair):
            result += min(nums[i * 2], nums[i * 2 + 1])

        return result


solution = Solution()
print(solution.arrayPairSum([1, 4, 3, 2]))
