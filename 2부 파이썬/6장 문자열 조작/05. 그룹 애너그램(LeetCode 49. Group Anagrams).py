import collections
import re
from dataclasses import dataclass
from typing import List
from collections import Counter


# Q. 문자열 배열을 받아 애너그램 단위로 그룹핑하라.

@dataclass
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬해 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word) # 문자도 정렬가능하다는 거 처음 알았음..! 와 어케 이렇게 풀지 대단하다
        return anagrams.values()

    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        # 1. 한 단어를 한 글자단위로 쪼개서 유니코드 값 다 더한다음
        # 1-1. key는 원래값. value는 유니코드값.
        # 1-2. 여기서 Map을 쓰는 게 최선인가,, 리스트[(튜플)] 도 될 것 같은데
        tmp = 0
        str_unicode_map = {}
        for str in strs:
            for char in str:
                tmp += ord(char)
            str_unicode_map[str] = tmp
            tmp = 0

        print(str_unicode_map)

        # 3. 같은 값 가지는 애들끼리 묶기
        # 3-1. 2중 for문 돌면서 아니야 하나로도 될듯..? 그니까 같은 값을 가지는 애들은 pop 해버려서 아예 없애버리는 거지
        result = []
        for base_str, base_unicode in str_unicode_map.items():
            for compare_str, compare_unicode in str_unicode_map.items():
                tmp = []
                # del str_unicode_map[base_str]
                # 4. 일단 처음 만나는 base_str은 result에 넣기
                if base_unicode == compare_unicode:
                    tmp.append(compare_str)
                    del str_unicode_map[compare_str]
            result.append(tmp)
        return result



input = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
print(solution.groupAnagrams(input))

