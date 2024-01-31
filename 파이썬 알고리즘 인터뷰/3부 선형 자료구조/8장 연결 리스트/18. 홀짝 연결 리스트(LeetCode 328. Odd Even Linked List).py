# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList_240131(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0. 예외처리

        # 1. 홀수(odd)와 짝수(even)노드를 각각 이어 만들어서
        odd = head
        even = even_head = head.next

        while even and even.next:
            # 1-1. 홀수, 짝수
            odd.next, even.next = odd.next.next, even.next.next
            # 1-2. 다음 loop를 위해 값 세팅
            odd, even = odd.next, even.next

        # 2. 홀수의 마지막 노드와 짝수의 첫 노드 이어주기
        odd.next = even_head

        return head

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0. 예외처리
        if head is None:
            return None

        # 1. 홀(odd), 짝(even) 노드를 각각 구성한다.
        odd = head
        even = even_head = head.next

        while even and even.next:  # 아 여기 왜 기준이 even인지.. 헷갈린다...
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

            # # 1-1. 홀수 노드 구성
            # odd.next = odd.next.next # 현재 홀수 노드의 next 값에 내 다음다음 노드를 가리키면 됨
            # odd = odd.next # 다음 loop를 위해 포인터 이동

            # # 1-2. 짝수 노드 구성
            # even.next = even.next.next
            # even = even.next

        # 2. 홀수의 마지막과 짝의 첫 노드 이어주기
        odd.next = even_head

        return head
