def elf_sections(sec_range):
    range_start = sec_range.split("-")[0]
    range_end = sec_range.split("-")[1]
    return list(range(int(range_start), int(range_end) + 1))


def is_overlap(line):
    elf0 = line.split(",")[0]
    elf1 = line.split(",")[1]
    elf0_sections = elf_sections(elf0)
    elf1_sections = elf_sections(elf1)
    if len(set(elf0_sections) & set(elf1_sections)) == 0:
        return False
    return True


with open("day4/input.txt", "r") as f:
    n = 0
    lines = f.readlines()
    for line in lines:
        if is_overlap(line.strip()):
            n += 1
    print(n)
