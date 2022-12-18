from pprint import pprint



def compare_list(list1, list2):
    """
    return 1 (order), 0(equal), -1 (non-order)
    """
    n1 = len(list1)
    n2 = len(list2)
    temp = None
    for i in range(n1):
        if i >= n2:
            return -1
        
        if isinstance(list1[i], int) and isinstance(list2[i], int):
            if list1[i] < list2[i]:
                return 1
            elif list1[i] > list2[i]:
                return -1
            else:
                continue
        elif isinstance(list1[i], list) and isinstance(list2[i], list):
            temp = compare_list(list1[i], list2[i])
            if temp == 0:
                continue
            else:
                return temp
        else:
            if isinstance(list1[i], int) and isinstance(list2[i], list):
                temp = compare_list([list1[i]], list2[i])
            elif isinstance(list1[i], list) and isinstance(list2[i], int):
                temp = compare_list(list1[i], [list2[i]])
            if temp == 0:
                continue
            else:
                return temp
    
    if n1 < n2:
        return 1
    return 0


if __name__ == '__main__':
    from pprint import pprint
    pairs = []
    count = 0
    
    # TODO: will try to recursively parse the input string without using eval later
    # test_ls = ["[", "1", ",", "2", ",", "3", "]"]
    # print(parse_line(test_ls, 0, []))
    
    

    
    while True:
        try:
            #line = list(map(eval, list(input())))
            line = input()
            if line != "":
                line = eval(line)
                pairs.append(line)
        except Exception as e:
            print(e.args)
            break

    count = 0
    result = {}
    for i in range(0, len(pairs), 2):
        p1 = pairs[i]
        p2 = pairs[i+1]
        flag = compare_list(p1, p2)
        result[count+1] = flag
        count += 1

    total = 0
    for k, v in result.items():
        if v == 1:
            total += k

    pprint(total)
        








    