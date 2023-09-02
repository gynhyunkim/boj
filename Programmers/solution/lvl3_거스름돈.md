```python3
DIV = 1_000_000_007

def solution(n, money):
    dp = [1] + [0] * n
    
    for coin in sorted(money):
        for price in range(coin, n + 1):
            dp[price] = (dp[price] + dp[price - coin]) % DIV
    return dp[n]
```
- dp를 이용해서 풀이
	- dp[price] + dp[price-coin]
- 각 코인 별로 dp를 계산한다.
	- 1의 경우 늘 한 가지 방법만 존재하므로 1 ~ n까지의 값이 모두 1이 된다
