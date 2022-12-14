# 추워요 #옷 입으세요

# 형식 : 16강 = [{home = "Brazil", away = "Korea", home_score = 3 , away_score =4 }, {}]


## demo ver. 2018 

# round별 데이터 정리 (2018 월드컵)

round_of_16 = [
    {"home" : "프랑스", "away" : "아르헨티나", "home_score": 4 , "away_score" : 3},  #이 형식에 맞춰서 입력해주셔요 !
    {"home" : "우루과이", "away" : "포르투갈", "home_score": 2 , "away_score" : 1},
    {"home" : "브라질", "away" : "멕시코", "home_score": 2 , "away_score" : 0},
    {"home" : "벨기에", "away" : "일본", "home_score": 3 , "away_score" : 2},

    {"home" : "스웨덴", "away" : "스위스", "home_score": 1 , "away_score" : 0},
    {"home" : "콜롬비아", "away" : "영국", "home_score": 1.3 , "away_score" : 1.4},
    
]
round_of_8 = [
    {"home" : "우루과이", "away" : "프랑스", "home_score": 0 , "away_score" : 2},
    {"home" : "브라질", "away" : "벨기에", "home_score": 1 , "away_score" : 2},
    {"home" : "러시아", "away" : "크로아티아", "home_score": 2.3 , "away_score" : 2.4},
    {"home" : "스웨덴", "away" : "영국", "home_score": 0 , "away_score" : 2}
]
round_of_4 = [
    {"home" : "프랑스", "away" : "벨기에", "home_score": 1 , "away_score" : 0},
    {"home" : "크로아티아", "away" : "영국", "home_score": 2 , "away_score" : 1}
]
round_of_2 = [
    {"home" : "프랑스", "away" : "크로아티아", "home_score": 4 , "away_score" : 2}
]


team_list = []
all_match = round_of_16 + round_of_8 + round_of_4 + round_of_2

def get_drop_teams(array):
    team_drop_array = []
    #3123
    for i in array :
        if i["home_score"] > i["away_score"]: 
            team_drop_array.append(i["away"])
        else: team_drop_array.append(i["home"])
    
    return team_drop_array

drop_from_16 = get_drop_teams(round_of_16)
drop_from_8 = get_drop_teams(round_of_8)
drop_from_4 = get_drop_teams(round_of_4)
drop_from_2 = get_drop_teams(round_of_2)
#final_winner = 


def get_all_matches(team):
    global all_match
    array = {}
    for i in team:
        for j in all_match:
            if i in j["home"] or i in j["away"]:
                try : array[i] += [j]
                except : array[i] = [j]
    return array

print(get_all_matches(drop_from_8))
