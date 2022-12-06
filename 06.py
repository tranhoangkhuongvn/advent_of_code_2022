import string
from pprint import pprint




if __name__ == '__main__':
    part1 = 3
    part2 = 13    
    while True:
        try:
            i, j = 0, 13
            line = input()
            print(line)
            last4 = {}
            for idx, ch in enumerate(line[:part2]):
                if ch in last4:
                    i = last4[ch] + 1
                last4[ch] = idx

            for idx, ch in enumerate(line[part2:]):
                #print(ch, i, j)
                if ch not in last4:
                    last4[ch] = j
                    if (j - i) == part2:
                        print(j+1)
                        break
                    j += 1
                else:
                    current_idx = last4[ch]
                    if (j - current_idx) <= part2:
                        # if the previous occurence of the char is less than current i, keep the current i
                        i = max(last4[ch] + 1, i) 
                    elif (j - i) == part2:
                        print(j+1)
                        break
                    
                    last4[ch] = part2 + idx
                    
                    j += 1
                #pprint(last4)

        except Exception as e:
            print(e.args)
            break
    

    