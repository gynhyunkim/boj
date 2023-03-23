def solution(tickets):
    answer = ["ICN"]
    tickets.sort()
    visited = [False for i in range(len(tickets))]

    def DFS(route):
        for i, ticket in enumerate(tickets):
            if route[-1] == ticket[0] and not visited[i]:
                route.append(ticket[1])
                visited[i] = True
                DFS(route)
                if sum(visited) == len(tickets):
                    return
                route.pop()
                visited[i] = False
    DFS(answer)
    return answer

