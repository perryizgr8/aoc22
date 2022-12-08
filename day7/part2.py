import sys


inodes = {}


def inode_name(path):
    n = "/".join(path)
    if len(n) > 1 and n[0] == "/" and n[1] == "/":
        return n[1::]
    return n


def read_input(lines):
    path = []
    cwd = None
    ls = False
    for line in lines:
        line = line.rstrip()
        if line.startswith("$ cd"):
            cwd = line.split(" ")[2]
            if cwd == "..":
                path.pop()
                cwd = path[-1]
            else:
                path.append(cwd)
            if inode_name(path) not in inodes.keys():
                inodes[inode_name(path)] = {"dir": True, "size": None, "children": []}
            ls = False
            continue
        if line.startswith("$ ls"):
            ls = True
            continue
        if ls:
            if line.startswith("dir"):
                dirname = line.split(" ")[1]
                if inode_name(path + [dirname]) not in inodes.keys():
                    inodes[inode_name(path + [dirname])] = {
                        "dir": True,
                        "size": None,
                        "children": [],
                    }
                if cwd:
                    inodes[inode_name(path)]["children"].append(
                        inode_name(path + [dirname])
                    )
                continue
            else:
                filesize = line.split(" ")[0]
                filename = line.split(" ")[1]
                if inode_name(path + [filename]) not in inodes.keys():
                    inodes[inode_name(path + [filename])] = {
                        "dir": False,
                        "size": int(filesize),
                    }
                assert cwd
                inodes[inode_name(path)]["children"].append(
                    inode_name(path + [filename])
                )


def get_size(name):
    if not inodes[name]["dir"]:
        return inodes[name]["size"]
    if inodes[name]["size"]:
        return inodes[name]["size"]
    sz = 0
    for child in inodes[name]["children"]:
        sz += get_size(child)
    return sz


def calc_dir_sizes():
    for name, metadata in inodes.items():
        sz = 0
        if metadata["dir"]:
            for child in metadata["children"]:
                sz += get_size(child)
            metadata["size"] = sz


with open("day7/input.txt", "r") as f:
    lines = f.readlines()
    read_input(lines)
    print(f"created {len(inodes)} inodes")
    calc_dir_sizes()
print("calculated sizes")
cap = 70000000
min_req = 30000000
used = inodes["/"]["size"]
to_free = min_req - (cap - used)
top = [
    (name, metadata["size"])
    for name, metadata in inodes.items()
    if metadata["dir"] and metadata["size"] >= to_free
]
print(min([x[1] for x in top]))