line = str(input(""))
line = line.upper()

def split(line):
    return [char for char in line]

line = split(line)
for i in range(len(line)):
    a = str(line[i])
    if (line.count(a)> 1):
        line = [w.replace(a, ')') for w in line]
    else:
        line = [w.replace(a, '(') for w in line]
line = "".join(line)
print(line)