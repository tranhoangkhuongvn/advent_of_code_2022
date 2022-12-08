from queue import Queue

class Node:
    def __init__(self, size, name, type, parent=None):
        self.size = size
        self.name = name
        self.type = type
        self.parent = parent
        self.children_ls = []

def traverse_dir_tre_part1(root):
    src = root
    tree_queue = Queue()
    tree_queue.put(src)
    total_size = 0

    while tree_queue.qsize() > 0:
        node = tree_queue.get()
        if node.type == "dir" and node.size < 100000:
            total_size += node.size
        
        if node.parent:
            print(f"{node.name}: {node.size} - {node.type} - {node.parent.name}")
        else:
            print(f"{node.name}: {node.size} - {node.type}")
        for child in node.children_ls:
            tree_queue.put(child)

    print(total_size)


def traverse_dir_tree(root, min_amount):
    src = root
    tree_queue = Queue()
    tree_queue.put(src)
    dir_list = []

    while tree_queue.qsize() > 0:
        node = tree_queue.get()
        if node.type == "dir":
            dir_list.append(node.size)
        
        # if node.parent:
        #     print(f"{node.name}: {node.size} - {node.type} - {node.parent.name}")
        # else:
        #     print(f"{node.name}: {node.size} - {node.type}")
        for child in node.children_ls:
            tree_queue.put(child)

    dir_list = sorted(dir_list)
    for dir in dir_list:
        if dir >= min_amount:
            print(dir)
            break

def calculate_size(node):
    
    for child in node.children_ls:
        node.size += calculate_size(child)

    return node.size


if __name__ == '__main__':
    ls_output = False
    root = Node(0, "root", "dir")
    current_dir = root
    while True:
        # construct the directory tree from the input file
        try:
            line = list(input().split())
            #print(line)
            if line[0] == "$": # command
                command = line[1]
                if command == "cd":
                    args = line[2]
                    ls_output = False
                    if args == "/":
                        current_dir = root
                    elif args == "..":
                        if current_dir.parent != None:
                            current_dir = current_dir.parent
                    else:
                        for child in current_dir.children_ls:
                            if args == child.name:
                                current_dir = child
                                break
                elif command == "ls":
                    ls_output = True
            else:
                if line[0] == "dir":
                    dir_name = line[1]
                    new_node = Node(0, dir_name, "dir", current_dir)
                    current_dir.children_ls.append(new_node)
                else:
                    size = int(line[0])
                    file_name = line[1]
                    new_node = Node(size, file_name, "file", current_dir)
                    current_dir.children_ls.append(new_node)
        
        except Exception as e:
            print(e.args)
            break

    calculate_size(root)
    
    print(root.size)
    print("avail: ", 70000000 - root.size)
    print("amount to delete >= ", root.size - 40000000)
    min_delete_amount = root.size - 40000000
    traverse_dir_tree(root, min_delete_amount)