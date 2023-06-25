def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    for a, b, c, d, e in problems:
        max_alp = max(a, max_alp)
        max_cop = max(b, max_cop)
    alp = min(max_alp, alp)
    cop = min(max_cop, cop)
    INF = float('inf')
    dp = [[INF] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j + 1 <= max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if alp_req <= i and cop_req <= j:
                    next_alp = min(i + alp_rwd, max_alp)
                    next_cop = min(j + cop_rwd, max_cop)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)
                
    return dp[max_alp][max_cop]

