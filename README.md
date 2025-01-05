# Pseudo codes
※ The list of functions to actually implement can be found under "Function Needed" if you scroll down !

## Principles
### data processing
Order of processing information: raw data -> data for analysis -> data for train. 
[raw data -> data for analysis part] is very important for structuring the information, and 'data for train' will be used for training actual ML.
Most of the functions announced below are used here.

### softmax regression
The softmax regression code is mostly complete, but it seems that we still need to optimize the epochs or adjust the optimizer (with TensorFlow). 
If you have any questions while working, please refer to the softmax regression section in the ML.py file on GitHub :)

### frontend
Please work on the front-end using tkinter or other Python GUI libraries (it's best to run it in Python :D)

## Data Structure

- raw data
> Round of 16,,Sat,2014-06-28,17:00 (05:00),Colombia co,2–0,uy Uruguay,73804,Estadio Jornalista Mário Filho (Neutral Site),Björn Kuipers,Match Report,

■ The data includes a lot of information that will not be used. You need to write code to determine the number of rounds in the match based on 'Round of ~', and apply the function only to the country and score data to transform it into the data structure below !


- data for analysis
> round_of_16 = [{"home" : "Uruguay", "away" : "Colombia", "home_point" : 0, "away_point" : 2, "dif" : -2, "home_rank" : 14, "away_rank" : 17}] 

■ The target team in the home category (since Uruguay was eliminated in the round of 16, Urgruay is home--when processed from Uruguay's perspective)
■ dif = home_point - end_point (MUST)
■ It's useful to use web crawling to obtain the home_rank and away_rank (FIFA ranking).
■ For the actual model use, we will design it so that the home team is the team whose performance we want to find out (estimate) :)
 
- data for train
>x_train = [0,2,-2,14,17, 3] 
#[Home score, Away score, Home score - Away score, Home FIFA ranking, Away FIFA ranking]
y_train = [1,0,0,0,0]
 #[Teams eliminated in round of 16, Teams eliminated in quarterfinals, Teams eliminated in the semifinals, Runner-up team, Champion team] 


## Functions Needed
Please be sure to read the content about the Data Structure as well :)
### raw_to_json(text)
>Round of 16,,Sat,2014-06-28,17:00 (05:00),Colombia co,2–0,uy Uruguay,73804,Estadio Jornalista Mário Filho (Neutral Site),Björn Kuipers,Match Report,

Split the text in the above format and use indexing to

> {"home" : "Uruguay", "away" : "Colombia", "home_point" : 0, "away_point" 	: 2, "dif" : -2, "home_rank" : 14, "away_rank" : 17, "round" : 16} 

This function changes and returns the same data structure. 
For the FIFA rankings, you can create a list like fifa_ranks = ["Germany", "France"] and handle it by using the index method. 
You can get the FIFA ranking by doing fifa_ranks.index("team name") + 1. 
For the round, you can write 16 for the round of 16, 8 for the quarterfinals, 4 for the semifinals, and 2 for the final.

■ I was planning to handle FIFA rankings through web crawling, but it seems necessary to create an array manually. Why? cause we need to construct the names to be placed in the array as they appear in the actual data(Colombia, Uruguay, in this case)
■ (Since the raw data is quite lengthy, when using the actual function, I plan to process each one by running txt.readlines in a for loop.)

When using this code, proceed as follows:
> [{"home" : "Uruguay", "away" : "Colombia", "home_point" : 0, "away_point" 	: 2, "dif" : -2, "home_rank" : 14, "away_rank" : 17, "round" :16}, {"home" : "Belgium", "away" : "United States", "home_point" : 2, "away_point" 	: 1, "dif" : 1, "home_rank" : 2, "away_rank" : 17, "round" : 8}]

I will go through a World Cup and collect information from each match into a list.

### get_teams_of_league(worldcup) 	

> [{"home" : "Uruguay", "away" : "Colombia", "home_point" : 0, "away_point" 	: 2, "dif" : -2, "home_rank" : 14, "away_rank" : 17, "round" :16}, {"home" : "Belgium", "away" : "United States", "home_point" : 2, "away_point" 	: 1, "dif" : 1, "home_rank" : 2, "away_rank" : 17, "round" : 8}]

Input to be on the scale of single World Cup unit (function retrieves all the participant countries)
Inside the function, create a teams_list = []. If a team is not in teams_list, add it to the list :)
You need to check both dict["home"] and dict["away"] in the dictionary.
Also, check the round, and for the return, collect the teams that dropped out in each round. (Mark the runner-up team as 2 and the champion as 1!)
Always write the difference as home - end. 
> {16: ["Uruguay", "South Korea", "Colombia" .. ], 8: ["United States"] ... }

it'll turn out like this!

### tracking_team(match, team)

a function that goes through 'for i in match' and 'for j in team' to collect all the matches each team has played.

> ["Uruguay" : [{"home" : "Uruguay", "away" : "Colombia", "home_point" : 3, "away_point" 	: 2, "dif" : 1, "home_rank" : 14, "away_rank" : 17, "round" :16}, {"home" : "Uruguay", "away" : "Japan", "home_point" : 0, "away_point" 	: 2, "dif" : -2, "home_rank" : 14, "away_rank" : 23, "round" :8} ... ], "Country Name" : [Organize dictionary of all matches played]]

When collecting for Uruguay, please rearrange it with Uruguay as the home team, and reorganize so that the difference is calculated as home-end.


### analysis_to_train(match)
Convert the above format into a format suitable for actual training (data for train).
Inpur format is as follows: 
>{"home" : "Uruguay", "away" : "Colombia", "home_point" : 0, "away_point" 	: 2, "dif" : -2, "home_rank" : 14, "away_rank" : 17, "round" :16}

You can create a function that makes and returns the following :)

> [[3,2,1,14,17,3], [1,0,0,0,0]]
> #[[Home goals, Away goals, Goal difference, Home FIFA ranking, Away FIFA ranking, Difference in FIFA rankings], [Round of 16, Quarterfinals, Semifinals, Runner-up, Champion]]

Only 1 for max winning round, 0 for the rest
