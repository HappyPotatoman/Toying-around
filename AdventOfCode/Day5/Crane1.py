def stack(input):
  rows = []
  stacks = [[] for _ in range(9)] 
  res = ''

  # Get initial state of stacks
  with open(input) as f:
    for i, line in enumerate(f):
      if i < 8: 
        rows.append(line.rstrip())
      else:
        break
  
  for row in reversed(rows):
    for j, x in enumerate(range(1,len(row),4)):
      if row[x].isalpha():
        stacks[j].append(row[x])

  # Get moves
  with open(input) as f:
    for i, line in enumerate(f):
      if i >= 10:
        l = line.rstrip().split()
        # SAMPLE LINE ['move', '5', 'from', '5', 'to', '2']
        move, source, destination = int(l[1]), int(l[3]) - 1, int(l[5]) - 1
        for _ in range(move):
          stacks[destination].append(stacks[source].pop(-1))

  for stack in stacks:
    if stack:
      res += stack[-1]
  return res

if __name__ == '__main__':
  print(stack('input.txt'))