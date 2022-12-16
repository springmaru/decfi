# Pseudo code
※ 실제로 구현할 함수들의 목록은 쭉 아래로 내리면 "Function Needed"에 있습니다 !

## Principles
### data analyze
raw data -> data for analysis -> data for train 의 순서로 정보처리를 진행해주세요.
raw data -> data for analysis 부분은 정보를 구조화하는데에 큰 의미가 있고, 
data for train은 실제 ML을 돌리는데에 사용될 자료구조입니다.

### softmax regression
softmax regression 코드는 대부분 다 완성되어있는 상태입니다 (with tensorflow).
Github에는 ML.py라는 파일에 softmax regression 부분이 완성되어있으니 작업하시다가 궁금하신 부분은 참고해주세요 :)

### front-end
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

이 데이터는 본문에서 world cup 단위별로 collect 

### get_teams_of_league() 	

> [{"home" : "Uruguay", "away" : "Colombia", "home_point" : 0, "away_point" 	: 2, "dif" : -2, "home_rank" : 14, "away_rank" : 17, "round" :16}, {"home" : "Belgium", "away" : "United States", "home_point" : 2, "away_point" 	: 1, "dif" : 1, "home_rank" : 2, "away_rank" : 17, "round" : 8}]

Input은 하나의 worldcup 단위로 들어갑니다.




### analysis

### analysis_to_train()
