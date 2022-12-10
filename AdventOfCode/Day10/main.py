with open('input.txt') as f:
  screen = []
  cycle = 0
  register = 1
  rows = [40, 80, 120, 160, 200]
  for line in f:
    l = line.rstrip().split()

    if cycle in rows:
      register += 40

    if l[0] == 'noop':
      cycle += 1
      if cycle == register or cycle == register + 1 or cycle == register + 2:
        screen.append('#')
      else:
        screen.append('.')

    elif l[0] == 'addx':
      cycle += 1
      if cycle == register or cycle == register + 1 or cycle == register + 2:
        screen.append('#')
      else:
        screen.append('.')
      if cycle in rows:
        register += 40
      cycle += 1
      if cycle == register or cycle == register + 1 or cycle == register + 2:
        screen.append('#')
      else:
        screen.append('.')
      register += int(l[1])

for i in range(0, 201, 40):
  print(''.join(screen[i:i+40]))