def BFS(start,graph):
    visit=[start]
    q=[start]
    while len(q)!=0:
        ele=q.pop(0)
        for i in graph[ele]:
            if i not in visit:
                q.append(i)
                visit.append(i)
    return visit            
graph={
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","E"],
    "D":["B","E"],
    "E":["C","D"]
}
r=BFS("A",graph)
print(r)