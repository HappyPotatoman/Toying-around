def SoXTracker(input, length):
  with open(input) as f:
    for line in f:
      l = line.rstrip()

  marker = [ch for ch in l[:length]]
  for i, x in enumerate(l[length:], length):
    marker_set = set(marker)
    if len(marker) == len(marker_set):
      return i
    marker.pop(0)
    marker.append(x)

if __name__ == '__main__':
  print(SoXTracker('input.txt', 14))