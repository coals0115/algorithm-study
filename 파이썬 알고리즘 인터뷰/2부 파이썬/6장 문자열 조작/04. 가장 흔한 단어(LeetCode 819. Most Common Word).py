import re
from dataclasses import dataclass
from typing import List
from collections import Counter


# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
# 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.

@dataclass
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 1. 입력값 전처리
        # 1. 정규식으로 문자숫자만 남게 2. 대소문자 구분X 3. 잘라서 banned에 포함 안 된 것만 거름)
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                .lower().split() if word not in banned]

        counts = Counter(words)

        return counts.most_common(1)[0][0]


    def mostCommonWord1(self, paragraph: str, banned: List[str]) -> str:
        # 1. 데이터 가공
        # 1-1. 대소문자 구분 X # 1-2. 구두점 제거
        paragraph = paragraph.lower().replace(",", "").replace(".", "")
        # 1. 문자를 split한다.(공백 기준)
        splitList = paragraph.split()

        # 2. Counter를 이용해서 카운팅
        count = Counter(splitList)

        # 3. banned된 단어 제거
        # banned가 리스트니까 모든 요소를 몰면서 banned 대상 단어가 있는지 확인해야 함
        for str in banned:
            if str in count.keys():
                del count[str]

        print(count)

        # 4. count 수가 제일 큰 단어를 출력한다.
        result = ""
        max = -1
        for key, value in count.items():
            if value > max:
                max = value
                result = key

        return result

    # for str in banned:
    #     print(banned)
    #     # Map에서 key에 저 요소 존재하는지 확인하려면 어케하지..
    #     if count in str:
    #         del count[str]

    # count = {}
    #
    # # 2. 가장 흔하게 등장하는 단어를 key로 등록한다. value에는 count
    # for str in splitList:
    #     # 2-1. 이때 banned된 단어에 포함되어 있는지 in문으로 체크할 것
    #
    #     # 2-2. 그니까 카운팅을 하려면 아니 그 Map중에 CounterMap인가 있었던 거 같은데  count[str]
    #     count.setdefault(str, 1)
    #
    # # 3. count 수가 제일 큰 단어를 출력한다.

    # print(count)


solution = Solution()

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# paragraph = "Bob!"
banned = ["hit"]

print(solution.mostCommonWord(paragraph, banned))
