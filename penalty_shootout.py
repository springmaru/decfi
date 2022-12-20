worldcup_2022 = ['Netherlands', 'Senegal', 'England', 'United States', 'France', 'Australia', 'Argentina', 'Poland', 'Morocco', 'Croatia', 'Japan', 'Spain', 'Portugal', 'Korea Republic', 'Brazil', 'Switzerland']

def shootout_pt(total_str):
  split_list = total_str.split('\n')
  check_list = [n for n in split_list if blank_checker(n) == True]
  json_list = [raw_to_json(m) for m in check_list]
  team_list = list(set([l['home'] for l in json_list] + [l['away'] for l in json_list]))
  return_list = []
  return_dict = {}
  cnt = 0
  win = 0

  for i in team_list:
    cnt = 0
    win = 0
    for j in json_list:
      if j['home'] == i and i in worldcup_2022:
        if j['home_shootout'] != 0 or j['away_shootout'] != 0:
          cnt += 1
          if j['home_shootout'] > j['away_shootout']:
            win += 1
      elif j['away'] == i and i in worldcup_2022:
        if j['home_shootout'] != 0 or j['away_shootout'] != 0:
          cnt += 1
          if j['away_shootout'] > j['home_shootout']:
            win += 1
    if cnt != 0:
      return_list.append({i: round(win / cnt, 2)})

  for k in return_list:
    return_dict.update(k)

  return return_dict
