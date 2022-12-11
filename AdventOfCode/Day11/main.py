def op(operation, old):
  if operation[2] == 'old':
    operator2 = old
  else:
    operator2 = int(operation[2])

  if operation[1] == '+':
    return old + operator2
  elif operation[1] == '*':
    return old * operator2

def test(test, new, conditions):
  new = new % lcm
  if new % test == 0:
    monkeys[conditions[0]][0].append(new)
  else:
    monkeys[conditions[1]][0].append(new)
  
monkeys = []
monkey_count = -1
lcm = 1

with open('input.txt') as f:
  for line in f:
    l = line.rstrip().split()
    if l == []:
      continue
    if l[0] == 'Monkey':
      monkey_count += 1
      monkeys.append(['items', 'op', 'test', [], 0])
    elif l[0] == 'Starting':
      items = []
      for item in l[2:]:
        if item[-1] == ',':
          item = item[:-1]
        items.append(int(item))
      monkeys[monkey_count][0] = items
    elif l[0] == 'Operation:':
      monkeys[monkey_count][1] = l[3:]
    elif l[0] == 'Test:':
      # test condition is divisible by l[3]
      monkeys[monkey_count][2] = int(l[3])
      lcm *= int(l[3])
    elif l[0] == 'If':
      monkeys[monkey_count][3].append(int(l[-1]))
# 20 Rounds
for _ in range(10000):
  for monkey in monkeys:
    while monkey[0]:
      old = monkey[0].pop(0)
      monkey[4] += 1
      new = op(monkey[1], old)
      test(monkey[2], new, monkey[3])

touches = sorted([monkey[4] for monkey in monkeys], reverse = True)
print(touches[0] * touches[1])

