from pprint import pprint
from collections import OrderedDict
import heapq

from queue import Queue

def is_valid(node, nrow, ncol):
    return (0<= node[0] < nrow) and (0 <= node[1] < ncol)


def bfs(matrix, src, dst, visited):
    dir = [(0,1), (-1,0), (0,-1), (1,0)]
    
    nrow = len(matrix)
    ncol = len(matrix[0])
    path = OrderedDict()
    path[src] = -1
    st = Queue()
    st.put((0, src))
    visited[src[0]][src[1]] = True
    

    while st.qsize() > 0:
        
        _, node = st.get()

        if node[0] == dst[0] and node[1] == dst[1]:
            return path
        for d in dir:
            new_node = (node[0] + d[0], node[1] + d[1])
            if is_valid(new_node, nrow, ncol) and not visited[new_node[0]][new_node[1]]:
                h0 = ord(matrix[node[0]][node[1]])
                h1 = ord(matrix[new_node[0]][new_node[1]])
                delta = h1 - h0
                if delta <= 1:
                    #st.append((delta, new_node))
                    st.put((delta, new_node))
                    path[new_node] = node
                    visited[new_node[0]][new_node[1]] = True
        #heapq.heapify(st)

    print(node)
    print("Failed to find path!")
    return path




if __name__ == '__main__':
    
    matrix = []
    nrow, ncol = 0, 0
    src, dst = -1, -1
    while True:
        try:
            line = list(map(str, input()))
            if ncol == 0:
                ncol = len(line)
            if "S" in line:
                src = (nrow, line.index("S"))
            if "E" in line:
                dst = (nrow, line.index("E"))
            matrix.append(line)
            nrow += 1
        except Exception as e:
            print(e.args)
            break

    
    print(nrow, ncol) # 41, 136
    matrix[src[0]][src[1]] = "a"
    matrix[dst[0]][dst[1]] = "z"

    print(src, dst)
    
    visited = [[False for c in range(ncol)] for r in range(nrow)]

    print(src, dst)
    result = bfs(matrix, src, dst, visited)
    
    shortest = []
    while True:
        prev = result[dst]
        dst = prev
        shortest.append(prev)
        if prev == src:
            break

    print(len(shortest))