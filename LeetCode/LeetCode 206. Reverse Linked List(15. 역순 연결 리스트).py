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
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None

        while node:
            # 현재 node = 0x200
            # 1-1. 내 다음 노드(순차)를 next에 저장. next = 0x300(덮어씌워지기 전에)
            # 1-2. 내 다음 노드에 이전 값을 저장 node.next = 0x100
            next, node.next = node.next, prev
            # 2-1. 나는 이전 값이 되고 (다음 loop에서 나는 이전 값이 되어야 하니까 현재 내 노드를 prev에 저장)
            # 2-2. 다음 노드는 다음 loop에서 현재 값이 됨
            prev, node = node, next

        print(prev)

        return prev

    def reverseList_my(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_list: List[ListNode] = []

        while head is not None:
            node_list.append(head)
            head = head.next

        head = None
        pointer = None
        if node_list:
            head = node_list.pop() # head 가지고 있기
            pointer = head

        while node_list:
            next_node = node_list.pop()
            next_node.next = None
            pointer.next = next_node
            pointer = next_node

        return head



solution = Solution()
# print(solution.isPalindrome())
