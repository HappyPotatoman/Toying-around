def read(input, task2=False):
  decryption_key = 811589153
  output_list = []
  with open(input) as f:
    for idx, line in enumerate(f):
      l = line.rstrip()
      output_list.append((idx, int(l) * (1 if not task2 else decryption_key)))
  return output_list

def unmix(data_list, task2=False):
  i, n = 0, len(data_list)
  while i < n:
    for curr_pos, curr_tuple in enumerate(data_list):
      idx, val = curr_tuple
      if idx == i:
        data_list.pop(curr_pos)
        data_list.insert((curr_pos + val) % len(data_list), (idx, val))
        break
    i += 1
  if task2:
    return data_list
  else:
    out = []
    for _, x in data_list:
      out.append(x)
    return out

def main(task2=False):
  # read the input file
  data_list = read('input.txt', task2=task2)
  # feed the list into the unmix function
  unmixed_data_list = unmix(data_list, task2=task2)
  if task2:
    for _ in range(8):
      unmixed_data_list = unmix(unmixed_data_list, task2=task2)
    # final iteration to get the correct output
    unmixed_data_list = unmix(unmixed_data_list)
  # define the values to sum and the length of the list
  values, n = [1000, 2000, 3000], len(unmixed_data_list)
  # get the index of the first 0
  idxOfFirst0 = unmixed_data_list.index(0)

  # print the sum of the values at the index of the first 0 + the value in the values list
  print(sum([unmixed_data_list[(idxOfFirst0 + value) % (n + 1)] for value in values]))

if __name__ == '__main__':
  # tast 1
  main()
  # task 2
  main(True)