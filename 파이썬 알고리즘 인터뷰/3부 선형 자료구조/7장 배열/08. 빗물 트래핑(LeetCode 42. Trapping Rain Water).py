from dataclasses import dataclass
from typing import List

# Q. 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 게산하라.

@dataclass
class Solution:
    # 풀이2: 스택 쌓기
    def trap(self, height: List[int]) -> int:
        stack = []
        volumn = 0

        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                print()
                print(f'stack: {stack}')
                print(i)
                # 스택에서 꺼낸다.
                top = stack.pop()

                if not len(stack):
                    break

                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volumn += distance * waters

            stack.append(i)
        return volumn


    # 풀이1: 투 포인터를 최대로 이동
    def trap1(self, height: List[int]) -> int:
        if not height:
            return 0

        volumn = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = (max(height[left], left_max),
                                   max(height[right], right_max))
            if left_max <= right_max:
                volumn += left_max - height[left]
                left += 1
            else:
                volumn += right_max - height[right]
                right -= 1

            print(f'volumn: {volumn}')

        return volumn

    def trap0(self, height: List[int]) -> int:
        if not height:
            return 0

        volumn = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            print()
            print(f'left: {left}, right: {right}')
            print(f'height[left] : {height[left]}, left_max: {left_max}')
            print(f'height[right] : {height[right]}, right_max: {right_max}')

            # 이걸 구하는 이유: 왼쪽이나 오른쪽이나 한칸을 이동했을텐데, 이동한 현재 위치와 기존의 값 비교해서 더 큰 걸 max에 넣음.
            left_max, right_max = (max(height[left], left_max),
                                   max(height[right], right_max))

            print(f'left_max: {left_max}, right_max: {right_max}')
            if left_max <= right_max:
                # 좌우 기둥 최대 높이가 현재 높이와의 차이만큼 물 높이를 더한다.
                volumn += left_max - height[left] # 이동한 자리보다 현재 위치가 더 크면
                left += 1 # 오른쪽으로 이동
            else:
                volumn += right_max - height[right]
                right -= 1 # 왼쪽으로 이동

            print(f'volumn: {volumn}')

        return volumn




solution = Solution()
print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
