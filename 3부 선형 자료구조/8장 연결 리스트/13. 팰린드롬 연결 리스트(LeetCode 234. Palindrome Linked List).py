import collections
from dataclasses import dataclass
from typing import Optional, List, Deque


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
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head

        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev

    # 2. 데크를 이용한 최적화
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        q: Deque = collections.deque()

        if not head:
            return True

        node = head

        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

    # 1. 리스트 변환
    def isPalindrome1(self, head: Optional[ListNode]) -> bool:
        q: List = []

        if not head:
            return True

        node = head

        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True


    def isPalindrome_my(self, head: Optional[ListNode]) -> bool:
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
