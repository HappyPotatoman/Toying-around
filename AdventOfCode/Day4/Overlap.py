def overlap(input):
  count = 0
  with open(input) as f:
    for line in f:
      l = line.rstrip()
      elf1, elf2 = str(), str()
      for i, v in enumerate(l):
        if v == ',':
          elf1 = l[:i]
          elf2 = l[i+1:]
          break
      elf1_min, elf1_max, elf2_min, elf2_max = str(), str(), str(), str()
      for i, v in enumerate(elf1):
        if v == '-':
          elf1_min = elf1[:i]
          elf1_max = elf1[i+1:]
          break
      for i, v in enumerate(elf2):
        if v == '-':
          elf2_min = elf2[:i]
          elf2_max = elf2[i+1:]
          break
      elf1_min, elf1_max, elf2_min, elf2_max = int(elf1_min), int(elf1_max), int(elf2_min), int(elf2_max)
      print(f'{elf1_min = }, {elf1_max = }, {elf2_min = }, {elf2_max = }')
      if elf1_min >= elf2_min and elf1_max <= elf2_max:
        count += 1
      elif elf2_min >= elf1_min and elf2_max <= elf1_max:
        count += 1
      elif elf1_min <= elf2_min and elf1_max >= elf2_min:
        count += 1
      elif elf2_min <= elf1_min and elf2_max >= elf1_min:
        count += 1
  return count
if __name__ == '__main__':
  print(overlap('input.txt'))