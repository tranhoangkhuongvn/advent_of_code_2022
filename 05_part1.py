import string
from pprint import pprint

if __name__ == '__main__':
    upper_characters = list(string.ascii_uppercase)
    line_ls = []
    while True:
        line = input()
        if line == "":
            break
        line_ls.append(line)
    
    last_row = line_ls[-1]
    num_stack = list(map(int, last_row.split()))
    print(num_stack)
    stack_list = []
    for num in num_stack:
        stack_list.append([])
    
    for row_idx, row in enumerate(line_ls[::-1]):
        if row_idx == 0:
            continue
        #print(row_idx, row)
        for ch_idx, ch in enumerate(row):
            if ch in upper_characters:
                stack_list[ch_idx // 4].append(ch)

    
    print(stack_list)

    while True:
        try:
            command = list(map(str, input().split()))
            qty, src, dst = int(command[1]), int(command[3])-1, int(command[5])-1
            src_stack = stack_list[src]
            dst_stack = stack_list[dst]
            for i in range(qty):
                dst_stack.append(src_stack.pop())
                
        except Exception as ex:
            print(ex.args)
            break



    for st_idx, st in enumerate(stack_list):
        if len(st) > 0:
            print(st_idx, st[-1])