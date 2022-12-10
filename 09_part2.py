def satisfy(tail, head):
    """
    is the head and tail within the the 8 neighborhood
    """
    neighbors = [(1,0), (1,1), (0,1), (-1,1), (0,0), (-1,0), (-1,-1),(0,-1), (1,-1)]
    for next_node in neighbors:
        if (tail[0] + next_node[0] == head[0]) and (tail[1] + next_node[1] == head[1]):
            return True
    
    return False

def follow(current_head, current_tail):
    if not satisfy(current_tail, current_head):
        dx = current_head[0] - current_tail[0]
        dy = current_head[1] - current_tail[1]
        #print(current_head, current_tail)
        if abs(dx) + abs(dy) == 3:
            # move diagonally
            if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
                new_x, new_y = 1, 1
            elif (dx == -1 and dy == 2) or (dx == -2 and dy == 1):
                new_x, new_y = -1, 1
            elif (dx == 1 and dy == -2) or (dx == 2 and dy == -1):
                new_x, new_y = 1, -1
            elif (dx == -1 and dy == -2) or (dx == -2 and dy == -1):
                new_x, new_y = -1, -1
        elif abs(dx) + abs(dy) == 2:
            # move vertially or horizontally
            if dx == 2 and dy == 0:
                new_x, new_y = 1, 0
            elif dx == -2 and dy == 0:
                new_x, new_y = -1, 0
            elif dx == 0 and dy == 2:
                new_x, new_y = 0, 1
            elif dx == 0 and dy == -2:
                new_x, new_y = 0, -1
        elif abs(dx) + abs(dy) == 4:
            if dx == 2 and dy == 2:
                new_x, new_y = 1, 1
            elif dx == 2 and dy == -2:
                new_x, new_y = 1, -1
            elif dx == -2 and dy == -2:
                new_x, new_y = -1, -1
            elif dx == -2 and dy == 2:
                new_x, new_y = -1, 1

        current_tail[0], current_tail[1] = current_tail[0] + new_x, current_tail[1] + new_y
    
    return current_tail


if __name__ == '__main__':
    src_x, src_y = 0, 0
    dir = {
        "U": (0, 1),
        "D": (0, -1),
        "L": (-1, 0),
        "R": (1, 0)
    }
    current_head = [0,0]
    prev_head = [0,0]
    current_tail = [0,0]
    knot_ls = [[0,0] for i in range(10)]
    path = set()
    path.add((0,0))
    while True:
        try:
            d, step = list(input().split())
            step = int(step)
            print(d, step)
            head_dx, head_dy = dir[d]
            
            for i in range(step):
                #print("step:", i)
                current_head = knot_ls[0]
                current_head[0], current_head[1] = current_head[0] + head_dx, current_head[1] + head_dy
                
                for idx in range(len(knot_ls)-1):
                    #print(idx, idx+1)
                    if idx == 0:
                        current_tail = knot_ls[idx + 1]
                        
                    else:
                        current_head = knot_ls[idx]
                        current_tail = knot_ls[idx + 1]
                    current_tail = follow(current_head, current_tail)
                    if idx == len(knot_ls) - 2:
                        path.add(tuple(current_tail))

                # print("head:", knot_ls[0])
                # print("tail:", current_tail)
        except Exception as e:
            print(e.args)
            break
    
    print("head:", current_head)
    print("tail:", current_tail)
    print(len(path))
    #print(path)