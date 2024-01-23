from dataclasses import dataclass
from typing import Optional


# Q. 연결 리스트가 팰린드롬 구조인지 판별하라

@dataclass
class ListNode:
    # 기본값을 None으로하면 안 된다 어쩌구 있었던 거 같은데..
    # -> None이 아니라 가변형을 기본값으로 사용 XX
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


@dataclass
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # print(help(ListNode.has_cycle))
        # print(dir(head))
        # print(head)

        result = []
        node = head
        while node:
            result.append(node.val)
            # print(node.val)
            node = node.next

        # 슬라이스 반대로 뒤집는 거 어케했더라..
        return result == result[::-1]


solution = Solution()
# print(solution.isPalindrome())
