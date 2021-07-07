casenum = int(input()) # 테스트케이스 개수
results = list()
for i in range(casenum):
    doc, pos = input().split()
    doc = int(doc) # 문서 개수
    pos = int(pos) # 출력 순서를 알고 싶은 문서 위치
    queue = list(map(int, input().strip().split()))
    while len(results) == i:
            pmax = max(queue)
            if queue[0] != pmax:
                queue.insert(len(queue), queue.pop(0))
                pos = pos - 1 if pos != 0 else len(queue) - 1
            else:
                queue.pop(0)
                if pos == 0:
                    results.append(doc - len(queue))
                else:
                    pos = pos - 1

for rslt in results:
    print(rslt)
