import functools
import operator
from typing import Optional, List, Deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합 계산
            if l1:
                print(f'l1.val: {l1.val}')
                sum += l1.val
                l1 = l1.next
                print(f'sum: {sum}')
            if l2:
                print(f'l2.val: {l2.val}')
                sum += l2.val
                l2 = l2.next
                print(f'sum: {sum}')
            print()

            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next

    # start ============================== my_2 ===================================
    # 1. 연결리스트 하나씩 val을 읽어서 숫자로 만들기(거꾸로)
    def LinkedListToReversedNum(self, list: Optional[ListNode]) -> int:
        head = list
        num = 0
        tmp = 1

        while head:
            num += head.val * tmp
            head = head.next
            tmp *= 10

        return num

    # 3. 이제 만든 리스트를 pop해서 하나씩 ListNode에 넣어주기
    def listToReversedLinkedList(self, list1) -> Optional[ListNode]:
        pointer = head = ListNode(list1.pop(), None)

        while list1:
            node = ListNode(list1.pop(), None)
            pointer.next = node
            pointer = node

        return head

    def addTwoNumbers_my2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 연결리스트 하나씩 val을 읽어서 숫자로 만들기(거꾸로)
        l1_num = self.LinkedListToReversedNum(l1)
        l2_num = self.LinkedListToReversedNum(l2)

        # 2. 결과값 만든 후에는 결과값을 자리수 쪼개서 연결리스트 만들어 반환
        result_str = str(int(l1_num) + int(l2_num)) # 두 수를 더한 값을 문자열로 변환
        result_list = [char for char in result_str] # 한글자씩 쪼개서 list에 넣기

        # 3. 이제 만든 리스트를 pop해서 하나씩 ListNode에 넣어주기
        head = self.listToReversedLinkedList(result_list)
        return head

    # // end ============================== my_2 ===================================


    def addTwoNumbers_my1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 연결리스트 하나씩 val을 읽어서 숫자로 만들기
        print(self.LinkedListtoReversedNum(l1))

        l1_head = l1
        l2_head = l2

        l1_num = 0
        l2_num = 0
        tmp = 1


        while l1_head:
            l1_num += l1_head.val * tmp
            l1_head = l1_head.next
            tmp *= 10

        tmp = 1
        while l2_head:
            l2_num += l2_head.val * tmp
            l2_head = l2_head.next
            tmp *= 10

        # 2. 결과값 만든 후에는 결과값을 자리수 쪼개서 연결리스트 만들어 반환
        result_str = str(int(l1_num) + int(l2_num)) # 두 수를 더한 값을 문자열로 변환
        result_list = [char for char in result_str] # 한글자씩 쪼개서 list에 넣기

        # 3. 이제 만든 리스트를 pop해서 하나씩 ListNode에 넣어주기
        # 3-1. head를 먼저 세팅해야하나..?

        head = ListNode(result_list.pop(), None)
        pointer = head

        while result_list:
            node = ListNode(result_list.pop(), None)
            pointer.next = node
            pointer = node

        return head

solution = Solution()
# print(solution.isPalindrome())














