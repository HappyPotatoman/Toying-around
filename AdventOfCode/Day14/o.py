def markimpossible(rows, floor):
    markedcount = 0
    for y in range(floor):
        markedcount += len(rows[y])
        rows[y+1].update(x for x in rows[y] if x-1 in rows[y] and x+1 in rows[y])
    return markedcount

def rockformation(rows, coords):
    xc, yc = next(coords), next(coords)
    rows[yc].add(xc)
    for x, y in zip(coords, coords):
        for j in range(min(y, yc), max(y, yc)+1):
            rows[j].update(range(min(x, xc), max(x, xc)+1))
        xc, yc = x, y

with open('input.txt') as f:
    input = [[int(x) for x in line.split() if x != "->"] for line in set(f.read().replace(",", " ").split("\n"))]
    floor = max(max(line[1::2] for line in input)) + 2
    rows = [set() for _ in range(floor+1)]
    for line in input:
        rockformation(rows, iter(line))
    print(floor * floor - markimpossible(rows, floor))

print(rows)