graph={
    'A':['V','K'],
    'V':['L','C'],
    'K':['C'],
    'L':[],
    'C':['X'],
    'X':[]
    }
visited=set()
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
print("Following is Depth-Frist search")
dfs(visited,graph,'A')
