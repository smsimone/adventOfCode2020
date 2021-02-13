groups = []
with open("input.txt", "r") as f:
    lines = f.readlines()
    single_group = []
    for index in range(len(lines)):
        line = lines[index]
        line = line.replace("\n","")
        if not line == "":
            single_group.append(line)
            if index == len(lines)-1:
                groups.append(single_group)
        else:
            groups.append(single_group)
            single_group = []

counts = []
for group in groups:
    group_answers = list(group[0])
    for index in range(1,len(group)):
        person = group[index]
        group_answers = set.intersection(set(group_answers), set(list(person)))
    print(group_answers)
    print("----------")
    group_answers = set(group_answers)
    counts.append(len(group_answers))
print(sum(counts))
