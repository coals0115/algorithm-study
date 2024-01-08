from dataclasses import dataclass
from collections import deque


# 주어진 문장이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.(검증)
# 팰린드롬 - 앞뒤가 똑같은 단어나 문장
@dataclass
class Solution:
    # ver 1
    def isPalindrome1(self, s: str) -> bool:
        # 0. (해야되나?) 영문과 숫자가 아닌 게 들어올 경우 false?
        # 0-1. 그 전에 원본 문자열을 영문과 숫자만 남도록 다 제거해야 함
        s = ''.join([char for char in s if char.isalnum()])

        # 1. 일단 입력값이 있는데 그걸 뒤집어서 가져오기 -> 슬라이스 이용
        palindrome = s[::-1]  # start와 stop 생략 시 처음부터 끝까지. -1은 거꾸로 추출

        # 2. 그 뒤집은 값을 대소문자 구분하지 않도록 원본과 생성한 값 둘 다 소문자로 바꾸기
        s = s.lower()
        palindrome = palindrome.lower()

        for i in range(len(s)):
            if s[i] != palindrome[i]:
                return False

        # 3. 변환했으면 두 값을 비교해서 bool 값 반환하기
        return True

    # ver2
    # <개선점>
    # 굳이 또 나중에 lower 할 필요가 x -> 리스트 컴프리헨션 안에서 한꺼번에 하기
    # 또 굳이 join으로 string으로 바꿀 필요가 x 그냥 list pop하기
    def isPalindrome2(self, s: str) -> bool:
        # 1. s를 영문자와 숫자를 제외하고 다 제거한다.
        s = [char.lower() for char in s if char.isalnum()]

        # 2. 제거한 걸 반대로 뒤집고
        palindrome = s[::-1]

        # 3. 원본과 뒤집은 걸 비교해서 하나라도 다르면 false 반환
        for i in range(len(s)):
            if s.pop() != palindrome.pop():
                return False

        return True

    # ver3
    # 책 풀이(2) 데크 자료형을 이용한 최적화
    # List의 pop(0) -> O(n)
    # 데크의 popleft() -> O(1)
    def isPalindrome3(self, s: str) -> bool:
        # 자료형 데크로 선언
        strs: deque = deque()

        s = [strs.append(char.lower()) for char in s if char.isalnum()]

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True

    # ver4
    # 책 풀이(3) 슬라이싱 사용
    def isPalindrome4(self, s: str) -> bool:
        # s = s.lower()
        # s = re.sub('[^a-z0-9]', '', s)

        s = [char.lower() for char in s if char.isalnum()]

        return s == s[::-1]

solution = Solution()
print(solution.isPalindrome4("A man, a plan, a canal: Panama"))