import collections
from dataclasses import dataclass
from typing import Optional, List, Deque


# Q. 정렬되어 있는 두 연결 리스트를 합쳐라.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

@dataclass
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1

        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1


solution = Solution()
# print(solution.isPalindrome())
