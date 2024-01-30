from dataclasses import dataclass
from typing import List

# Q. 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.

@dataclass
class Solution:
    def reverseString(self, s: List[str]) -> None:
        # s = s[::-1] # ;; 안됨;

        s.reverse() # 1
        s[:] = s[::-1] # 2 : 약간의 트릭으로 슬라이스 가능

solution = Solution()
print(solution.reverseString(["h", "e", "l", "l", "o"]))