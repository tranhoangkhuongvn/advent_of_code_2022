import string
from pprint import pprint



if __name__ == '__main__':
    count = 0
    while True:
        try:
            p1, p2 = input().split(",")
            l1, r1 = list(map(int, p1.split("-")))
            l2, r2 = list(map(int, p2.split("-")))
            l_min = min(l1, l2)
            r_max = max(r1, r2)
            
            if (l1 <= l2 and r1 >= l2) or (l1 >= l2 and r2 >= l1):
                print(l1, r1, l2, r2)
                count += 1

            

        except Exception as e:
            print(e.args)
            break
    
    print(count)