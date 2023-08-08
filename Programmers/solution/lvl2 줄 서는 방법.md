### Python3

### 코드
```python
import math
def solution(n, k):
    answer = []
    num = [x for x in range(1, n + 1)]
    for i in range(1, n + 1):
        i_fact = math.factorial(n - i)
        r = k // i_fact
        r = r - 1 if k % i_fact == 0 else r
        k %= i_fact
        answer.append(num[r])
        num.remove(num[r])
    return answer
```
- `itertools`를 이용하면 순열을 간편하게 구할 수 있지만 시간초과가 발생한다.
- `factorial` 연산을 이용해서 k번째 순열을 쉽게 구할 수 있다.
- `i`번째 항에 올 숫자는 factorial 연산을 이용해 찾을 수 있다. !(i - 1)이 몇 번 반복 되어야 하는지 알아야 하므로 k를 !(i - 1)로 나누어야 한다. 나눈 몫이 i번째에 해당하는 숫자가 된다. 만약 나머지가 0이라면 몫 - 1로 시작하는 순열의 마지막 값이므로 몫에서 1을 빼줘야 한다. 