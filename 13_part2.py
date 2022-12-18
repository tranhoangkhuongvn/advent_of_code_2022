from pprint import pprint
import copy

def merge(A, p, m, r):
    """
    A[p:m] and A[m+1:r] are sorted
    """
    #import pdb; pdb.set_trace()
    n1 = m - p + 1
    n2 = r - m
    l1 = [None for _ in range(n1 + 1)]
    l2 = [None for _ in range(n2 + 1)]
    
    
    for i in range(n1):
        l1[i] = copy.deepcopy(A[p + i])
    for j in range(n2):
        l2[j] = copy.deepcopy(A[m + 1 + j])
    l1[n1] = [10000]
    l2[n2] = [10000]

    
    i, j = 0, 0
    for k in range(p, r+1):
        if compare_list(l1[i], l2[j]) == 1:#l1[i] <= l2[j]:
            A[k] = l1[i]
            i += 1
        else:
            A[k] = l2[j]
            j += 1


def merge_sort(A, p, r):
    #import pdb; pdb.set_trace()
    if p < r:
        mid = (p + r) // 2
        merge_sort(A, p, mid)
        merge_sort(A, mid + 1, r)
        merge(A, p, mid, r)
    
    


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
    

    # Test merge sort
    # ls = [10, 3, 1, 0, 43, 10, 20]
    # merge_sort(ls, 0, len(ls)-1)
    # print("sorted:")
    # print(ls)



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
    
    pairs.append([[2]])
    pairs.append([[6]])
    merge_sort(pairs, 0, len(pairs)-1)
    #pprint(pairs)
    idx1 = pairs.index([[2]])
    idx2 = pairs.index([[6]])
    print( (idx1 + 1) * (idx2 + 1))
        








    