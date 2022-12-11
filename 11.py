from queue import Queue
from tqdm import tqdm

class Monkey:
    def __init__(self, id, items, operation, test, false_cond, true_cond):
        self.item_list = Queue()
        for item in items:
            self.item_list.put(item)
        self.operation = operation
        self.test = test
        self.false_cond = false_cond
        self.true_cond = true_cond
        self.id = id
        self.total_inspected_item = 0

    def inspect(self, monkey_list):
        while self.item_list.qsize() > 0:
            self.total_inspected_item += 1
            item = self.item_list.get()   
            new_item = eval(str(item) + self.operation)
            # new_item = new_item // 3 # for part 1
            new_item = new_item % part2_relief # for part 2
            if new_item % self.test == 0:
                self.throw(new_item, self.true_cond, monkey_list)
            else:
                self.throw(new_item, self.false_cond, monkey_list)


    def throw(self, item, receiver_id, monkey_list):
        for idx in range(len(monkey_list)):
            if idx == receiver_id:
                monkey_list[idx].item_list.put(item)
                break
        

    def __repr__(self):
        print(f"Monkey {self.id} - Item list: {list(self.item_list.queue)} - Operation {self.operation} - Test {self.test}")

    def __str__(self):
        return f"Monkey {self.id} - Item list: {list(self.item_list.queue)} - Operation {self.operation} - Test {self.test}"


def decrypt_operation(operation):
    """
    operation: new = old * 7 or new = old + old
    """
    ans = None
    assert operation[0] == "new", "Wrong output"
    assert operation[1] == "=", "Wrong equal sign"
    try:
        second = int(operation[-1])
        ans = operation[-2] + operation[-1]
    except:
        # failed to convert to int
        if operation[-2] == "*":
            ans = "**2"
        elif operation[-2] == "+":
            ans = "*2"
    
    return ans


if __name__ == '__main__':
    monkey_list = []
    part2_relief = 1
    while True:
        try:
            line = list(input().replace(":", "").split())
            if "Monkey" in line:
                # create a new monkey
                temp_id = int(line[-1])
                count = 0
                temp_list = []
                operation = ""
                div = 0
                false_id = 0
                true_id = 0
                while count < 5:
                    line = list(input().replace(",","").split())
                    count += 1
                    if "Starting" in line:
                        for item in line[2:]:
                            temp_list.append(int(item))
                    elif "Operation:" in line:
                        operation = decrypt_operation(line[1:])
                    elif "Test:" in line:
                        div = int(line[-1])
                        part2_relief *= div
                    elif "true:" in line:
                        true_id = int(line[-1])
                    elif "false:" in line:
                        false_id = int(line[-1])
                    else:
                        print("Empty line")
                monkey = Monkey(temp_id, temp_list, operation, div, false_id, true_id)
                print(monkey)
                monkey_list.append(monkey)

        except Exception as e:
            print(e.args)
            break
    
    for round in tqdm(range(10000)): # for part 2
        for monkey in monkey_list:
            monkey.inspect(monkey_list)

    result = []
    for idx, monkey in enumerate(monkey_list):
        print("Monkey: ", idx)
        print(monkey.total_inspected_item)
        result.append(monkey.total_inspected_item)
        #print(list(monkey.item_list.queue))

    result = sorted(result)
    print(result[-2] * result[-1])




    


