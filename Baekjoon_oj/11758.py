from sys import stdin

X, Y = 0, 1
coord = [list(map(int, stdin.readline().split())) for _ in range(3)]
d = (coord[1][Y] - coord[0][Y]) * (coord[2][X] - coord[1][X]) - (coord[1][X] - coord[0][X]) * (coord[2][Y] - coord[1][Y]) 
print(1 if d < 0 else (-1 if d > 0 else 0))
    
