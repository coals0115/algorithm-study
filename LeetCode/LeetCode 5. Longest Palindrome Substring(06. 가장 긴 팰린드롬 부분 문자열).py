from dataclasses import dataclass


# Q. 문자열 배열을 받아 애너그램 단위로 그룹핑하라.

@dataclass
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 1. 주어진 문자열에서 생길 수 있는 모든 경우의 수의 문자를 생성한다.
        # TODO 리스트 컴프리헨션으로 줄일 수 있는지 화긴
        result = ""
        for i in range(len(s)):
            for j in range(len(s) - 1):
                palindrom = s[i:j+2]

                # 팰린드롬인지 체크 | 글자 하나일 경우 스킵 | 이미 존재하던 팰린드롬보다 크기 큰지 체크
                if self.isPalindrome(palindrom) and len(palindrom) > 1 and palindrom > result:
                    result = palindrom

        return result


    def isPalindrome(self, s: str) -> bool:
        s = ''.join([char for char in s if char.isalnum()])

        palindrome = s[::-1]  # start와 stop 생략 시 처음부터 끝까지. -1은 거꾸로 추출

        s = s.lower()
        palindrome = palindrome.lower()

        for i in range(len(s)):
            if s[i] != palindrome[i]:
                return False

        return True

    def longestPalindrome1(self, s: str) -> str:
        # 1. 문자열이 들어왔다....
        # 1. 주어진 문자열에서 생길 수 있는 모든 경우의 수의 문자를 생성한다.
        # TODO 리스트 컴프리헨션으로 줄일 수 있는지 화긴

        result = ""
        for i in range(len(s)):
            for j in range(len(s) - 1):
                # print(f'i : {i}, j : {j}')
                # print(s[i:j+2])
                # 글자 하나일 경우에 스킵

                # 생성하는 건 슬라이스로 index 값으러
                # 1-1. 생성해서, 걔가 팰린드롬인지 체크. 만약 팰린드롬이라면 result 값에 넣어둔다.
                # print(s[i:j])
                # print(self.isPalindrome(s[i:j]))
                palindrom = s[i:j+2]

                if self.isPalindrome(palindrom) and len(palindrom) > 1:
                    if palindrom > result:
                        result = palindrom
                # 1-1-1. 그 전에 기존 result값과 비교해서 내가 더 크면 result에 넣고 아니면 안 넣음
                # print(result)
        return result

solution = Solution()
print(solution.longestPalindrome("babad"))
print(solution.longestPalindrome("cbbd"))
