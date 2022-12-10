class Node:
    def __init__(self, name: str, type: str, size: int = 0, ):
        self.name = name
        self.size = size
        self.type = type
        self.parent = None
        self.children = []
    
    def add_child(self, node):
        node.parent = self
        self.children.append(node)
    
    def __str__(self):
        return "{}=>{}=>{}=>{}".format(self.name, self.type, self.size, [c.name for c in self.children])

root = None
current = root
for line in open("/Users/zuko/Code/advent-of-code/2022/7/in.txt", "r"):
    line = line.strip()
    # print(line)
    if line.startswith("$ cd /"):
        root = Node("/", "d")
        root.parent = root
        current = root
    elif line.startswith("$ cd"): #change dir
        dir = line.split("cd")[1].strip()
        if dir == "..":
            current = current.parent
            print(current)
        else:
            for n in current.children:
                if n.name == dir:
                    current = n
        continue
    elif line.startswith("$ ls"): #dir
        continue
    elif line.startswith("dir"): #dir
        dir = line.split(" ")[1].strip()
        current.add_child(Node(dir, "d"))
        continue
    else: # file 
        (file_size, file_name) = tuple(line.split(" "))
        current.add_child(Node(file_name, "f", int(file_size)))

limit = 100000
l = []
def sum_sizes(node: Node):
    if node.size != 0:
        return node.size
    else:
        for n in node.children:
            node.size += sum_sizes(n)
        l.append(node.size)
        return node.size        

sum_sizes(root)

total = 0
for i in l:
    if i <= limit:
        total += i

print(total)
        
         
         


