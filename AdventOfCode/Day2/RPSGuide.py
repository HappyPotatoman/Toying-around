def RPSGuide(input):
  scores = {'R': 1, 'P': 2, 'S': 3, 'win': 6, 'draw': 3, 'loss': 0}
  score = 0
  with open(input) as f:
    for line in f:
      l = line.rstrip()
      opponent, outcome = l[0], l[2]
      if outcome == 'X': # lose
        score += scores['loss']
        if opponent == 'A':
          score += scores['S']
        elif opponent == 'B':
          score += scores['R']
        else:
          score += scores['P']
      elif outcome == 'Y': # draw
        score += scores['draw']
        if opponent == 'A':
          score += scores['R']
        elif opponent == 'B':
          score += scores['P']
        else:
          score += scores['S']
      else:
        score += scores['win']
        if opponent == 'A':
          score += scores['P']
        elif opponent == 'B':
          score += scores['S']
        else:
          score += scores['R']
  return score

if __name__ == '__main__':
  print(RPSGuide('input.txt'))
  # print(RPSGuide('testinput.txt'))