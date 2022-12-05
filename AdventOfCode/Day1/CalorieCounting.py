def CalorieCounting(input):
  listOfElves = []
  curr = 0
  with open(input) as f:
    for line in f:
      if line.rstrip() == '':
        listOfElves.append(curr)
        curr = 0
      else:
        curr += int(line.rstrip())
  return sum(sorted(listOfElves, reverse=True)[:3])

if __name__ == '__main__':
  print(CalorieCounting('CalorieCountingInput.txt'))