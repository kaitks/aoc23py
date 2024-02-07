import re

import sympy


def day24(file: str) -> int:
    with open(file, "r") as file:
        contents = file.read()

    regex = re.compile(r"-?\d+")
    xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")
    equations = []
    h_stones = [[int(num) for num in re.findall(regex, line)] for line in contents.splitlines()]
    total = 0
    for i, (sx, sy, sz, vx, vy, vz) in enumerate(h_stones):
        equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
        equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
        if i < 2:
            continue
        answers = [soln for soln in sympy.solve(equations) if all(x % 1 == 0 for x in soln.values())]
        if len(answers) == 1:
            answer = answers.pop()
            total = answer[xr] + answer[yr] + answer[zr]
            print(i)
            print(total)
            break
    return total


day24("test.txt")
day24("input.txt")
