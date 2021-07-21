import sys
sys.setrecursionlimit(10000)

# def DFS(arr, x, y):
#     if arr[x][y] == 0:
#         return ;
#     arr[x][y] = 0
#     if x + 1 < len(arr):
#         DFS(arr, x + 1, y)
#     if y + 1 < len(arr[x]):     
#         DFS(arr, x, y + 1)
#     if x - 1 >= 0:
#         DFS(arr, x - 1, y)
#     if y - 1 >= 0:
#         DFS(arr, x, y - 1)
        
def DFS(arr, x, y):
    

casenum = int(input())
results = [0 for i in range(casenum)]
for case in range(casenum):
    row, col, locnum = input().split()
    row, col, locnum = int(row), int(col), int(locnum)
    arr = [[0 for i in range(col)] for j in range(row)]
    for loc in range(locnum):
        x, y = input().split()
        x, y = int(x), int(y)
        arr[x][y] = 1
    for k in range(len(arr)):
        for l in range(len(arr[k])):
            if arr[k][l] == 1:
                DFS(arr, k, l)
                results[case] += 1

for i in range(casenum):
    print(results[i])
    
    


