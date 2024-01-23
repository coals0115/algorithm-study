import sys
from dataclasses import dataclass
from typing import List


# Q. 자신을 제외한 배열의 곱

@dataclass
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        print(prices)
        # 최솟값과 최댓값을 계속 갱신한다.
        profit = -sys.maxsize
        min_price = sys.maxsize

        for price in prices:
            print(f'min_price: {min_price}, price: {price}, profit: {profit}')
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit

    def maxProfit1(self, prices: List[int]) -> int:
        max_price = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)

        return max_price

    def maxProfit_my(self, prices: List[int]) -> int:
        # 브루트 포스로 풀기
        result = []
        max_num = 0
        print(prices)

        # 1. 내 기준으로 우측에 있는 숫자들 중에 가장 큰 수를 찾아서
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if prices[j] > max_num:
                    max_num = prices[j]

            # 2. 이익 계산후 Result에 넣기
            result.append(max_num - prices[i])
            max_num = -1

        # 3. Result에서 가장 큰 수(이익)을 반환 max 이용
        return 0 if max(result) < 0 else max(result)



solution = Solution()
# price = [7, 6, 4, 3, 1]
price = [7, 1, 5, 3, 6, 4]
# price = [1]
print(solution.maxProfit(price))
