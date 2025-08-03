lines = ["aptech"]
lines *= 10000

with open("data.txt", "w") as f:
    for line in lines:
        f.write(line + "\n")

def filter_lines_with_keyword(filepath, keyword):
    with open(filepath, "r") as file:
        for line in file:
            if keyword.lower() in line.lower():
                yield line.strip()

for line in filter_lines_with_keyword("data.txt", "Aptech"):
    print(line)
