import random


c = 'c' #cooperated as intended
d = 'd' #defected as intended
C = 'C' #cooperated by mistake
D = 'D' #defected by mistake
cc = 2 #reward matrix (cooperate,cooperate)
cd = -1 #reward matrix (cooperate,defect)
dc = 3 #reward matrix (defect,cooperate)
dd = 0 #reward matrix (defect,defect)
last_move = 200
failure_c_p = 5 #probability of failing to cooperate (defect by mistake) in integer percentage
failure_d_p = 0 #probability of failing to defect (cooperate by mistake) in integer percentage
available_players = {'tit_for_tat', 'tit_for_two_tats', 'grudger', 'simpleton',
                     'tester', 'always_defect', 'always_cooperate',
                     'tit_for_tat_advanced', 'delayed_tit_for_two_tats'}
view_moves = None
view_scores = None


def tit_for_tat(mine, other, move):
  if move == 1:
    return c
  else:
    return other[-1]


def tit_for_two_tats(mine, other, move):
  if move <= 2:
    return c
  elif (other[-1] == d) and (other[-2] == d):
    return d
  else:
    return c


def grudger(mine, other, move):
  if move == 1:
    return c
  elif d in other:
    return d
  else:
    return c


def simpleton(mine, other, move):
  if move == 1:
    return c
  elif other[-1] == c:
    return mine[-1]
  elif other[-1] == d:
    return opposite(mine[-1])


def tester(mine, other, move):
  if move == 1:
    return d
  elif move == 2:
    return other[0]
  elif move == 3 and other[1] == d:
    return c
  elif move >= 4 and other[1] == d:
    return other[-1]
  elif move >= 3 and other[1] == c:
    return opposite(mine[-1])


def always_defect(mine, other, move):
  return d


def always_cooperate(mine, other, move):
  return c


# New Stretegy 1
def tit_for_tat_advanced(mine, other, move):
  if move == 1:
    return c
  elif move == 2:
    return other[-1]
  elif (other[-1] == d) and (mine[-2] == c):
    return d
  elif move <= 5:
    return c
  elif not (c in other[-5:]):
    return d
  else:
    return c


# New Stretegy 2
def delayed_tit_for_two_tats(mine, other, move):
  waiting_period = 10 #the number of moves it will play like tit_for_tat
  if move == 1:
    return c
  elif move <= waiting_period:
    return other[-1]
  elif (other[-1] == d) and (other[-2] == d):
    return d
  else:
    return c


# =======================================================================
def opposite(move):
  if move == c:
    return d
  if move == d:
    return c


def mistake(move):
  if move == c:
    return D
  if move == d:
    return C


def points(my_move, other_move):
  my_move = my_move.lower()
  other_move = other_move.lower()
  if (my_move == c) and (other_move == c):
    return cc
  if (my_move == c) and (other_move == d):
    return cd
  if (my_move == d) and (other_move == c):
    return dc
  if (my_move == d) and (other_move == d):
    return dd


def find_move(s, mine, other, move):
  strategy = s.split()[0]
  if 'tit_for_tat' == strategy:
    return tit_for_tat(mine, other, move)
  if 'tit_for_two_tats' == strategy:
    return tit_for_two_tats(mine, other, move)
  if 'grudger' == strategy:
    return grudger(mine, other, move)
  if 'simpleton' == strategy:
    return simpleton(mine, other, move)
  if 'tester' == strategy:
    return tester(mine, other, move)
  if 'always_defect' == strategy:
    return always_defect(mine, other, move)
  if 'always_cooperate' == strategy:
    return always_cooperate(mine, other, move)
  if 'tit_for_tat_advanced' == strategy:
    return tit_for_tat_advanced(mine, other, move)
  if 'delayed_tit_for_two_tats' == strategy:
    return delayed_tit_for_two_tats(mine, other, move)


def game(s1, s2):
  '''
  game: Str Str -> (list Nat Nat)
  Requires:
    s1, s2 must contain one of the listed strategies
    
  '''
  move = 1
  s1_moves = []
  s2_moves = []
  s1_result = []
  s2_result = []
  s1_score = 0
  s2_score = 0
  while move <= last_move:
    s1_move = find_move(s1, s1_moves, s2_moves, move)
    s2_move = find_move(s2, s2_moves, s1_moves, move)
    if s1_move == c and failure_c_p >= random.randint(1, 100):
      s1_move = mistake(s1_move)
    if s2_move == c and failure_c_p >= random.randint(1, 100):
      s2_move = mistake(s2_move)
    if s1_move == d and failure_d_p >= random.randint(1, 100):
      s1_move = mistake(s1_move)
    if s2_move == d and failure_d_p >= random.randint(1, 100):
      s2_move = mistake(s2_move)    
    s1_earned = points(s1_move, s2_move)
    s2_earned = points(s2_move, s1_move)
    s1_score += s1_earned
    s2_score += s2_earned
    s1_moves.append(s1_move.lower())
    s2_moves.append(s2_move.lower())
    s1_result.append(s1_move)
    s2_result.append(s2_move)
    move += 1
  if view_moves == 'y':
    print(s1 + ':' + '\n', s1_result)
    print(s2 + ':' + '\n', s2_result)
    print('Score: ', [s1_score, s2_score])
    print('\n')
  elif view_scores == 'y':
    print(s1 + ' vs. ' + s2)
    print('Score: ', [s1_score, s2_score])
    print('\n')
  return [s1_score, s2_score]


def all_pairs(los):
  pairs = []
  for i in range(len(los)):
    for j in range(i+1, len(los)):
      pair = [los[i], los[j]]
      pairs.append(pair)
  return pairs


def tournament(players):
  '''
  tournament: (listof Str) -> (listof Nat)
  Requires: 
    strings in players are unique
    len(players) > 1
  '''
  scores = [0] * len(players)
  pairs = all_pairs(players)
  for pair in pairs:
    s1 = pair[0]
    s2 = pair[1]
    result = game(s1, s2)
    s1_result = result[0]
    s2_result = result[1]
    s1_ind = players.index(s1)
    s2_ind = players.index(s2)
    scores[s1_ind] += s1_result
    scores[s2_ind] += s2_result
  return scores


# =======================================================================
def is_number(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


def enter_rules():
  while True:
    first_command = input("Do you want to customize the rules for this\
tournament? Enter y for yes and n for no: ")
    if not (first_command.lower() == 'y' or first_command.lower() == 'n'):
        print("Invalid input. Please enter y or n.")
        continue
    break
  if first_command.lower() == 'y':
    global cc
    global cd
    global dc
    global dd
    global last_move
    global failure_c_p
    global failure_d_p

    # Reward Matrix
    print("\nSet up the reward matrix for this tournament.")
    while True:
      command1 = input("Enter the score rewarded when player cooperates and opponent cooperates: ")
      if not is_number(command1):
        print("Invalid input. Please enter a number.")
        continue
      break
    while True:
      command2 = input("Enter the score rewarded when player cooperates and opponent defects: ")
      if not is_number(command2):
        print("Invalid input. Please enter a number.")
        continue
      break
    while True:
      command3 = input("Enter the score rewarded when player defects and opponent cooperates: ")
      if not is_number(command3):
        print("Invalid input. Please enter a number.")
        continue
      break
    while True:
      command4 = input("Enter the score rewarded when player defects and opponent defects: ")
      if not is_number(command4):
        print("Invalid input. Please enter a number.")
        continue
      break
    cc = int(command1)
    cd = int(command2)
    dc = int(command3)
    dd = int(command4)

    # Last Move
    while True:
      command5 = input("Enter the number of moves for each game: ")
      if not command5.isdigit():
        print("Invalid input. Please enter a positive integer.")
        continue
      if int(command5) == 0:
        print("Invalid input. Please enter a positive integer.")
        continue
      last_move = int(command5)
      break

    # Probability of Mistakes
    while True:
      command6 = input("Enter the probability of players not cooperating by \
mistake in integer percentage: ")
      if not command6.isdigit():
        print("Invalid input. Please enter an integer from 0 to 100.")
        continue
      if int(command6) > 100:
        print("Invalid input. Please enter an integer from 0 to 100.")
        continue
      failure_c_p = int(command6)
      break
    while True:
      command7 = input("Enter the probability of players not defecting by \
mistake in integer percentage: ")
      if not command7.isdigit():
        print("Invalid input. Please enter an integer from 0 to 100.")
        continue
      if int(command7) > 100:
        print("Invalid input. Please enter an integer from 0 to 100.")
        continue
      failure_d_p = int(command7)
      break


def enter_players():
  invalid_name = True
  while invalid_name:
    string_of_names = input("\nPlease enter all players in the tournament, separated by a comma.\n")
    name_list = string_of_names.split(',')
    for name in name_list:
      invalid_name = not (name.strip() in available_players)
      if invalid_name:
        print("One or more unavailable players typed or invalid input. Please try again.\n")
        break

  # Create a dictionary to keep track of name counts
  name_counts = {}
  unique_names = []

  # Iterate through the names and create unique strings
  for name in name_list:
    name = name.strip()  # Remove leading/trailing whitespaces
    if name not in name_counts:
      name_counts[name] = 1
      unique_names.append(f"{name} 1")
    else:
      name_counts[name] += 1
      unique_names.append(f"{name} {name_counts[name]}")
  return unique_names


def viewing_setting():
  global view_moves
  global view_scores
  while True:
    view_moves = input("\nDo you want to print the moves made by each player? \
Enter y for yes and n for no: ").lower()
    if not (view_moves == 'y' or view_moves == 'n'):
        print("Invalid input. Please enter y or n.")
        continue
    break
  if view_moves == 'y':
    view_scores == 'y'
  elif view_moves== 'n':
    while True:
      view_scores = input("\nDo you want to print the scores earned by players each game? \
Enter y for yes and n for no: ").lower()
      if not (view_scores == 'y' or view_scores == 'n'):
          print("Invalid input. Please enter y or n.")
          continue
      break
  print("\n=======================================================================\n")


def play_tournament():
  enter_rules()
  players = enter_players()
  viewing_setting()
  print(tournament(players))
