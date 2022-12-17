# Pseudo codes
※ 실제로 구현할 함수들의 목록은 쭉 아래로 내리면 "Function Needed"에 있습니다 !

## Principles
### data processing
raw data -> data for analysis -> data for train 의 순서로 정보처리를 진행할겁니다.
raw data -> data for analysis 부분은 정보를 구조화하는데에 큰 의미가 있고, 
data for train은 실제 ML을 돌리는데에 사용될 자료구조입니다.
아래 공지한 대부분의 함수는 여기에 사용됩니다.

### softmax regression
softmax regression 코드는 대부분 다 완성되어있는 상태입니다 (with tensorflow).
Github에는 ML.py라는 파일에 softmax regression 부분이 있으니 작업하시다가 궁금하신 부분은 참고해주세요 :)

### frontend
front-end는 tkinter나 다른 파이썬 GUI 제작 라이브러리를 이용해서 작업해주세요

## Data Structure

- raw data
> Round of 16,,Sat,2014-06-28,17:00 (05:00),Colombia co,2–0,uy Uruguay,73804,Estadio Jornalista Mário Filho (Neutral Site),Björn Kuipers,Match Report,

■ 사용하지 않을 정보가 대거 포함되어있습니다. Round of ~ 에 따라 몇 강의 경기인지 판단하고, 국가와 점수 데이터만 함수 적용시켜 아래 자료구조로 변형하는 코드를 짜야합니다 !


- data for analysis
> round_of_16 = [{"home" : "Uruguay", "away" : "Colombia", "home_point" : 0, "away_point" : 2, "dif" : -2, "home_rank" : 14, "away_rank" : 17}] 

■ 홈에는 대상팀 ( 우루과이가 16강에서 떨어졌으니까 이 경기를 우루과이 입장에서 처리할 때는 home 이 우루과이, 나중에 8강에서 떨어진 콜롬비아 입장에서는 
■ dif는 무조건 home_point - end_point로 계산해주세요
■ home_rank 와 away_rank(피파 랭킹)은 웹크롤링을 이용해서 가져오는게 유용해요.
■ 실제 모델 사용에는 home team이 성과를 알아내고 싶은 (추정하려는) 팀이 들어가도록 제작할겁니다 :)
 
- data for train
>x_train = [0,2,-2,14,17, 3] 
#[홈점수, 상대점수, 홈점수-상대점수, 홈 피파랭킹, 상대 피파랭킹]
y_train = [1,0,0,0,0]
 #[16강에서 떨어진 팀, 8강에서 떨어진 팀, 4강에서 떨어진 팀, 준우승 팀, 우승 팀] 


## Functions Needed
Data Structure 에 대한 내용도 포함되어있으니 꼭 읽어주세요 :)
### raw_to_json(text)
>Round of 16,,Sat,2014-06-28,17:00 (05:00),Colombia co,2–0,uy Uruguay,73804,Estadio Jornalista Mário Filho (Neutral Site),Björn Kuipers,Match Report,

위 형태인 text를 split으로 쪼개고 indexing 이용하여

> {"home" : "Uruguay", "away" : "Colombia", "home_point" : 0, "away_point" 	: 2, "dif" : -2, "home_rank" : 14, "away_rank" : 17, "round" : 16} 

같은 data structure로 바꿔서 return하는 함수입니다.
피파랭킹 같은 경우에는 fifa_ranks = ["Germany", "France"] list를 만들어서 인덱스를 이용하는 방법으로 처리할 수 있습니다. 
fifa_ranks.index("팀이름") + 1하면 피파랭킹이 나오는 식으로 처리하면 됩니다.
round는 16강이면 16, 8강이면 8, 4강이면 4, 결승이면 2로 작성해주시면 됩니다.

■ 피파랭킹은 웹크롤링으로 처리하려고 했으나 직접 array를 만들던지 해야할 것 같습니다.. why? : 실제로 데이터에 있는 형태로 (여기선 Colombia, Uruguay)로 array에 넣을 이름을 구성해야해서..
■ (raw data가 많이 길기 때문에 실제 함수를 사용할 때에는 txt.readlines를 for로 돌면서 하나하나 처리할 예정입니다.)

실제 이 코드를 활용할 때는 아래와 같이
> [{"home" : "Uruguay", "away" : "Colombia", "home_point" : 0, "away_point" 	: 2, "dif" : -2, "home_rank" : 14, "away_rank" : 17, "round" :16}, {"home" : "Belgium", "away" : "United States", "home_point" : 2, "away_point" 	: 1, "dif" : 1, "home_rank" : 2, "away_rank" : 17, "round" : 8}]

하나의 월드컵을 쫙 돌면서 각 match의 정보들을 list로 모아놓을거에요.

### get_teams_of_league(worldcup) 	

> [{"home" : "Uruguay", "away" : "Colombia", "home_point" : 0, "away_point" 	: 2, "dif" : -2, "home_rank" : 14, "away_rank" : 17, "round" :16}, {"home" : "Belgium", "away" : "United States", "home_point" : 2, "away_point" 	: 1, "dif" : 1, "home_rank" : 2, "away_rank" : 17, "round" : 8}]

Input은 하나의 worldcup 단위로 들어간다고 보시면 됩니다. (한 월드컵에 참여한 모든 국가를 구하는 함수)
function 내부에 teams_list = [] 를 만들고 if team not in teams_list일 때 teams_list에 추가하는 방식으로 진행하면 됩니다 :)
dictionary의 dict["home"]과 dict["away"]를 모두 검사해줘야합니다.
round를 같이 검사해줘서, return으로는 각 라운드에서 떨어진 team을 모아줄거에요. (준우승 팀은 2, 우승팀은 1로 표기해주면 되요 !)
dif는 무조건 home - end로 적어주세요.
> {16: ["Uruguay", "South Korea", "Colombia" .. ], 8: ["United States"] ... }

처럼 나오게 되는거죠 !

### tracking_team(match, team)

for i in match와 for j in team을 돌면서 각 team이 경기한 경기를 모두 collect하는 function입니다.  

> ["Uruguay" : [{"home" : "Uruguay", "away" : "Colombia", "home_point" : 3, "away_point" 	: 2, "dif" : 1, "home_rank" : 14, "away_rank" : 17, "round" :16}, {"home" : "Uruguay", "away" : "Japan", "home_point" : 0, "away_point" 	: 2, "dif" : -2, "home_rank" : 14, "away_rank" : 23, "round" :8} ... ], "국가 이름" : [국가가 한 경기 dictionary 모두 정리]]

우루과이에 대해 collect 할 때는 우루과이를 home team으로 해서 re-arrangement 해주시고, dif도 home-end가 될 수 있게 재정리해주세요.


### analysis_to_train(match)
위에 나온 형태를 실제 학습용 (data for train) 형태로 바꿔줘야합니다.
Input 형태는 아래와 같습니다.
>{"home" : "Uruguay", "away" : "Colombia", "home_point" : 0, "away_point" 	: 2, "dif" : -2, "home_rank" : 14, "away_rank" : 17, "round" :16}

여기서 아래와 같이 만들어서 리턴해주는 함수를 제작해주시면 됩니다 :)

> [[3,2,1,14,17,3], [1,0,0,0,0]]
> #[[홈득점, 상대득점,득실,홈피파랭킹,상대피파랭킹,피파랭킹차이], [16강, 8강, 4강, 준우승, 우승 중 해당하는거만 1, 나머지는 0]]
