import string
from pprint import pprint



if __name__ == '__main__':
    lower_characters = list(string.ascii_lowercase)
    upper_characters = list(string.ascii_uppercase)
    # print(lower_characters)
    # print(len(lower_characters))
    # print(upper_characters)
    # print(len(upper_characters))
    
    priority_dict = {}
    for idx, ch in enumerate(lower_characters):
        priority_dict[ch] = idx + 1
    for idx, ch in enumerate(upper_characters):
        priority_dict[ch] = idx + 1 + 26
    
    # pprint(priority_dict)
    priority_sum = 0
    count = 0
    char_dict1 = {}
    char_dict2 = {}
    
    while True:
        # read in 3 lines at a time
        try:
            line = input()
            if count % 3 == 0:
                for ch in line:
                    if ch not in char_dict1:
                        char_dict1[ch] = 0
            elif count % 3 == 1:
                for ch in line:
                    if ch in char_dict1:
                        char_dict2[ch] = 0
            else:
                for ch in line:
                    if (ch in char_dict1) and (ch in char_dict2):
                        priority_sum += priority_dict[ch]
                        char_dict1 = {}
                        char_dict2 = {}
                        break
            count += 1

        except Exception as e:
            print(e.args)
            break
    
    print(priority_sum)