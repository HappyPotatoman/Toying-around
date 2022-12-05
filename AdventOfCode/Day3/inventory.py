def inventory(input):
  priorities = 0
  priority = {chr(x): i for i, x in enumerate(range(ord('a'), ord('z')+1), 1)}
  for i, x in enumerate(range(ord('A'), ord('Z')+1), 27):
    priority[chr(x)] = i
  listOfItems = []
  group = []
  numGroups = 1 
  count = 0
  with open(input) as f:
    for line in f:
      l = line.rstrip()
      
      count += 1
      if count > 2:
        print(f'{numGroups = }, {count = }, {group = }, lastItem = {l}')
        for item in l:
          if item in group[0] and item in group[1]:
            listOfItems.append(item)
            print(item)
            break
        count = 0
        numGroups += 1
        group = []
      else:
        group.append(l)
  for item in listOfItems:
    priorities += priority[item]
  return priorities

if __name__ == '__main__':
  print(inventory('input.txt'))
  # print(inventory('testinput.txt'))