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
    while True:
        try:
            line = input()
            mid = len(line) // 2
            char_dict = {}
            for ch in line[:mid]:
                if ch not in char_dict:
                    char_dict[ch] = 0
                char_dict[ch] += 1

            for ch in line[mid:]:
                if ch in char_dict:
                    priority_sum += priority_dict[ch]
                    break

        except Exception as e:
            print(e.args)
            break
    
    print(priority_sum)