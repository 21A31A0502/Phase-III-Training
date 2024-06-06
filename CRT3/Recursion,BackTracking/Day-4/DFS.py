def DFS(start,graph,visit):
    #if visit==None:
   #     visit=[]
    visit.append(start)
    for i in graph[start]:
        if i not in visit:
            DFS(i,graph,visit) 
    return visit            
    
graph={
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","E"],
    "D":["B","E"],
    "E":["C","D"]
}
r=DFS("E",graph,[])
print(r)