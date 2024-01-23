from dataclasses import dataclass
from typing import List


# Q. 자신을 제외한 배열의 곱

@dataclass
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 나를 제외하고 왼쪽값과 오른쪽 값을 곱한 2개 배열을 만들고, 그 배열끼리 곱한다.
        out = []
        p = 1

        for i in range(len(nums)):
            out.append(p)
            p *= nums[i]

        print(out)

        p = 1
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] *= p # 기존 out 변수 재활용하기. 공간복잡도 O(n) -> O(1)
            p *= nums[i]

        return out

    def productExceptSelf_my(self, nums: List[int]) -> List[int]:
        # 뭔가 결과도 배열이라 리스트 컴프리헨션 쓰면 될 것 같기도..

        result = []
        for i, num1 in enumerate(nums):
            tmp = 1
            for j, num2 in enumerate(nums):
                if i == j:
                    continue

                tmp *= num2

            result.append(tmp)

        return result


solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))
