from dataclasses import dataclass
from typing import List


# Q. 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

@dataclass
class Solution:
    # 풀이4: 조회 구조 개선
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(f'nums: {nums}')
        nums_map = {}

        # 하나의 for문으로 통합
        for i, num in enumerate(nums):
            print(f'nums_map: {nums_map}')
            print(f'i : {i}, num : {num}, target: {target}')
            print(f'target - num: {target - num}')
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i

    # 풀이3: 첫 번째 수를 뺀 결과 키 조회
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        print(nums_map)

        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return i, nums_map[target - num]

    # 풀이2: in을 이용한 탐색
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i + 1:]:
                return i, nums[i + 1:].index(complement) + (i + 1)

    # 풀이1: 브루트 포스로 계산
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum0(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]

solution = Solution()
# print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([3, 2, 1, 4, 9], 6))
