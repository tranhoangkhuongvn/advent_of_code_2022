from pprint import pprint


def build_path(maze, src, dst):
    # print(src, dst)
    if src[0] == dst[0]: # same x
        small_y = min(src[1], dst[1])
        large_y = max(src[1], dst[1])
        for y in range(small_y, large_y+1):
            maze[y][src[0]] = "#"
    else:
        small_x = min(src[0], dst[0])
        large_x = max(src[0], dst[0])
        for x in range(small_x, large_x+1):
            maze[src[1]][x] = "#"

    return maze


def is_empty(maze, x, y):
    return maze[y][x] != "#" and maze[y][x] != "o"

def is_valid(maze, x, y):
    return True


def simulate(maze, sand_source, bottom_y):
    count = 0
    while True:
        temp = list(sand_source)
        while temp[1] <= bottom_y:
            # look down
            if is_empty(maze, temp[0], temp[1]+1):
                temp[1] += 1
            elif is_empty(maze, temp[0]-1, temp[1]+1):
                # look to the down-left
                temp[0] -= 1
                temp[1] += 1
            elif is_empty(maze, temp[0]+1, temp[1]+1):
                temp[0] += 1
                temp[1] += 1
            else:
                # all lower positions are occupied
                maze[temp[1]][temp[0]] = "o"
                count += 1
                print("pos:", temp)
                break
        
        if temp[1] > bottom_y:
            break
        
    return count


if __name__ == '__main__':
    # assume 0 <= x <= 800
    # assume 0 <= y <= 500
    maze = [["." for x in range(800)] for y in range(500)]
    sand_source = (500, 0)
    bottom_y = 0
    while True:
        try:
            line = input()
            # 498,4 -> 498,6 -> 496,6
            # 503,4 -> 502,4 -> 502,9 -> 494,9
            coords = line.replace(" ", "").split("->")
            #print(coords)
            for i in range(len(coords)-1):
                src_x, src_y = list(map(int, coords[i].split(",")))
                dst_x, dst_y = list(map(int, coords[i+1].split(",")))

                if src_y > bottom_y:
                    bottom_y = src_y
                if dst_y > bottom_y:
                    bottom_y = dst_y

                maze = build_path(maze, (src_x, src_y), (dst_x, dst_y))
            


        except Exception as e:
            print(e.args)
            break

    
    #pprint(maze[9][494:504])
    print(bottom_y)
    count = simulate(maze, sand_source, bottom_y)
    print(count)