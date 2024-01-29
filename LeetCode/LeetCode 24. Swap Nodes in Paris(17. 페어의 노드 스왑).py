import collections
from dataclasses import dataclass
from typing import Optional, List, Deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


@dataclass
# Definition for singly-linked list.
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            # b가 a(head)를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head

            # prev가 b를 가리키도록 할당
            prev.next = b

            # 다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next

        return root.next

    def swapPairs_my(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 첫 노드(나)와 다음 노드를 가지고 있는다.
        if head is None:
            return

        node = head
        next = node.next
        head = head.next

        # print(f'node: {node}')
        # print(f'node.next: {node.next}')
        # print(f'head: {head}')

        while node and node.next:
            # 2. 스왑
            node.next, next.next, node = next.next, node, node.next
            print(head)

            # 3. 다음 루프를 위한 값 세팅
            node = node.next
            next = node.next

        # print(head)


solution = Solution()
# print(solution.isPalindrome())
