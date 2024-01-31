# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # 0. 예외처리
        # head가 None이거나 역순으로 만들어야 하는 범위가 같다면 바꿀 필요가 없기 때문에 그대로 head를 반환한다.
        if not head or left == right:
            return head

        # 0. 더미 root 노드 하나 만들어서 연결해두기
        root = start = ListNode(None)
        root.next = head

        # 1. start와 end를 지정한다.
        # 1-1. start는 항상 고정 위치.(left-1) - root로 연결 한번 더 해서 left-1..
        for _ in range(left - 1):
            start = start.next
        # 1-2. end는 항상 left위치
        end = start.next

        # 2. end뒤에 있는 노드를 start뒤에 위치시키는 방식으로 반복(right-left 횟수)해서 위치를 바꾼다.(큰 수가 점점 앞으로 올 것)
        for _ in range(right - left):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp

        return root.next