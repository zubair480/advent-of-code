from typing import List

def get_springs(file_path: str) -> List[List]:
    with open(file_path, "r") as file:
        lines = file.readlines()

    springs = []
    for line in lines:
        diagram, nums_str = line.strip().split(" ")
        diagram = list(diagram)
        nums = [int(x) for x in nums_str.split(",")]
        springs.append([diagram, nums])

    return springs

def get_possibilities(diagram: List[str], nums: List[int]) -> int:
    potential = []

    def generate(idx: int, l: List[str]) -> None:
        if idx >= len(diagram):
            potential.append(l)
        elif diagram[idx] == "?":
            generate(idx+1, l + ["."])
            generate(idx+1, l + ["#"])
        else:
            generate(idx+1, l + [diagram[idx]])

    def score(l: List[str]) -> List[int]:
        curr = ""
        res = []

        for item in l:
            if item == "#":
                curr += "#"
            else:
                if len(curr) > 0:
                    res.append(len(curr))
                    curr = ""
        if len(curr) > 0:
            res.append(len(curr))

        return res

    generate(0, [])
    total = 0
    for p in potential:
        if score(p) == nums:
            total += 1
    return total

def get_sums(file_path: str) -> int:
    springs = get_springs(file_path)
    res = 0

    for diagram, nums in springs:
        local = get_possibilities(diagram, nums)
        res += local

    return res

print(get_sums("./input.txt"))
