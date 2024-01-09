from dataclasses import dataclass
from typing import List


# 로그를 재정렬하라. 기준은 다음과 같다.
# 1. 로그의 가장 앞 부분은 식별자다.
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# -> 우선순위가 문자 > 숫자라는데..
# 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 한다.
# 4. 숫자 로그는 입력 순서대로 한다.
# -> 입력순서대로 한다는게 무슨말임 아니 문제가 이해 안 되는데요

@dataclass
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []

        for log in logs:
            if  log.split()[1].isdigit(): # 제일 앞 부분은 식별자이기 때문에 2번째부터 확인
                # 숫자 변환 가능 log는 digits에
                digits.append(log)
            else:
                # 문자로그는 letters에
                letters.append(log)

        # 문자 로그 정렬(정렬기준 2개)
        # 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 한다.
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits



solution = Solution()
log = ["dig1 8 1 5 1", # 4
       "let1 art can", # 1
       "dig2 3 6", # 5
       "let2 own kit dig", # 2
       "let3 art zero"]
solution.reorderLogFiles(log) # 3

print(log)
print(log[0].split()[0])
print(log[0].split()[1:])
print(log[0].split()[1].isdigit())

# sort(key=lambda