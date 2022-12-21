def read(input):
  numbers = {}
  waiting = {}
  with open(input) as f:
    for line in f:
      l = line.rstrip().split()
      print(l)
      if len(l) == 2:
        numbers[l[0][:-1]] = int(l[1])
      else:
        waiting[l[0][:-1]] = l[1:]
  return numbers, waiting

def solve(numbers, waiting):
  while 'root' not in numbers:
    found = []
    for key, value in waiting.items():
      if value[0] in numbers and value[2] in numbers:
        if value[1] == "+":
          numbers[key] = numbers[value[0]] + numbers[value[2]]
          found += [key]
        elif value[1] == "-":
          numbers[key] = numbers[value[0]] - numbers[value[2]]
          found += [key]
        elif value[1] == "*":
          numbers[key] = numbers[value[0]] * numbers[value[2]]
          found += [key]
        elif value[1] == "/":
          numbers[key] = numbers[value[0]] // numbers[value[2]]
          found += [key]
    for key in found:
      del waiting[key]
  return numbers

def main():
  numbers, waiting = read("input.txt")
  solved_numbers = solve(numbers, waiting)
  return solved_numbers['root']

if __name__ == "__main__":
  print(main())
