class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent

    def __str__(self):
        return "file_{}_{}".format(self.name, self.size)
    
class Dir:
    def __init__(self, name, size, files: list[File], dirs):
        self.name = name
        self.size = size
        self.files = files
        self.dirs = dirs
    
    def __str__(self):
        return "dir_{}_{}".format(self.name, self.size)



    

# file = open("test.txt", "r")
# lines = file.readlines()
# f_iter = iter(lines)
# entry = next(f_iter)
# if (entry.startswith("$ cd")):


traverse = []
structure = {}
top = ""
for line in open("/Users/zuko/Code/advent-of-code/2022/7/in.txt", "r"):
    line = line.strip()
    if line.startswith("$ cd"):
        dir = line.split("cd")[1].strip()
        if dir == "..":
            top = traverse.pop()
        else:
            traverse.append(dir)
            top = "_".join(traverse)
            structure[top] = {"size": 0, "dirs": []}
        continue
    if line.startswith("$ ls"):
        # top = traverse.pop()
        continue
    if line.startswith("dir"):
        dir = line.split(" ")[1].strip()
        ndir = "{}_{}".format(top, dir)
        structure[ndir] = {"size": 0, "dirs": []}
        structure[top]["dirs"].append(ndir) 
        continue
    (file_size, file_name) = tuple(line.split(" "))
    structure[top]["size"] = structure[top]["size"] + int(file_size)

   
print(structure)

total_size = {}    
 
def sum_sizes(k):
    if len(structure[k]['dirs']) == 0:
        return structure[k]['size']
    else:
        s = structure[k]['size']
        for i in structure[k]['dirs']:
            # nk = "{}_{}".format(k, i)
            s = s + sum_sizes(i)
        # total_size[k] = s
            # return structure[k]['size']
        return s

total = 0
limit = 100000
for s,v in structure.items():
    total_size[s] = sum_sizes(s)
    if total_size[s] <= limit:
        total += total_size[s]
    print(s, total_size[s])

used = sum_sizes('/')
unused = 70000000 - used
needed = 30000000 - unused
import math
smallest = math.inf
for k,v in total_size.items():
    if v > needed and v < smallest:
        smallest = v

print("total_size:", total)
print("smallest:", smallest)






