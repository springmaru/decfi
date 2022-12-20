import math
game_log = [{'home': 'Brazil', 'away': 'Chile', 'home_point': 1, 'away_point': 1, 'dif': 0, 'home_rank': 3, 'away_rank': 14, 'round': 16, 'home_shootout': 3, 'away_shootout': 2},
{'home': 'Colombia', 'away': 'Uruguay', 'home_point': 2, 'away_point': 0, 'dif': 2, 'home_rank': 8, 'away_rank': 7, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Netherlands', 'away': 'Mexico', 'home_point': 2, 'away_point': 1, 'dif': 1, 'home_rank': 15, 'away_rank': 20, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Costa Rica', 'away': 'Greece', 'home_point': 1, 'away_point': 1, 'dif': 0, 'home_rank': 28, 'away_rank': 12, 'round': 16, 'home_shootout': 5, 'away_shootout': 3},
{'home': 'France', 'away': 'Nigeria', 'home_point': 2, 'away_point': 0, 'dif': 2, 'home_rank': 17, 'away_rank': 44, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Germany', 'away': 'Algeria', 'home_point': 2, 'away_point': 1, 'dif': 1, 'home_rank': 2, 'away_rank': 22, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Argentina', 'away': 'Switzerland', 'home_point': 1, 'away_point': 0, 'dif': 1, 'home_rank': 5, 'away_rank': 6, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Belgium', 'away': 'United States', 'home_point': 2, 'away_point': 1, 'dif': 1, 'home_rank': 11, 'away_rank': 13, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'France', 'away': 'Germany', 'home_point': 0, 'away_point': 1, 'dif': -1, 'home_rank': 17, 'away_rank': 2, 'round': 8, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Brazil', 'away': 'Colombia', 'home_point': 2, 'away_point': 1, 'dif': 1, 'home_rank': 3, 'away_rank': 8, 'round': 8, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Argentina', 'away': 'Belgium', 'home_point': 1, 'away_point': 0, 'dif': 1, 'home_rank': 5, 'away_rank': 11, 'round': 8, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Netherlands', 'away': 'Costa Rica', 'home_point': 0, 'away_point': 0, 'dif': 0, 'home_rank': 15, 'away_rank': 28, 'round': 8, 'home_shootout': 4, 'away_shootout': 3},
{'home': 'Brazil', 'away': 'Germany', 'home_point': 1, 'away_point': 7, 'dif': -6, 'home_rank': 3, 'away_rank': 2, 'round': 4, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Netherlands', 'away': 'Argentina', 'home_point': 0, 'away_point': 0, 'dif': 0, 'home_rank': 15, 'away_rank': 5, 'round': 4, 'home_shootout': 2, 'away_shootout': 4},
{'home': 'Brazil', 'away': 'Netherlands', 'home_point': 0, 'away_point': 3, 'dif': -3, 'home_rank': 3, 'away_rank': 15, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Germany', 'away': 'Argentina', 'home_point': 1, 'away_point': 0, 'dif': 1, 'home_rank': 2, 'away_rank': 5, 'round': 2, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Uruguay', 'away': 'Korea Republic', 'home_point': 2, 'away_point': 1, 'dif': 1, 'home_rank': 16, 'away_rank': 47, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'United States', 'away': 'Ghana', 'home_point': 1, 'away_point': 2, 'dif': -1, 'home_rank': 14, 'away_rank': 32, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Germany', 'away': 'England', 'home_point': 4, 'away_point': 1, 'dif': 3, 'home_rank': 6, 'away_rank': 8, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Argentina', 'away': 'Mexico', 'home_point': 3, 'away_point': 1, 'dif': 2, 'home_rank': 7, 'away_rank': 17, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Netherlands', 'away': 'Slovakia', 'home_point': 2, 'away_point': 1, 'dif': 1, 'home_rank': 4, 'away_rank': 34, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Brazil', 'away': 'Chile', 'home_point': 3, 'away_point': 0, 'dif': 3, 'home_rank': 1, 'away_rank': 18, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Paraguay', 'away': 'Japan', 'home_point': 0, 'away_point': 0, 'dif': 0, 'home_rank': 31, 'away_rank': 45, 'round': 16, 'home_shootout': 5, 'away_shootout': 3},
{'home': 'Spain', 'away': 'Portugal', 'home_point': 1, 'away_point': 0, 'dif': 1, 'home_rank': 2, 'away_rank': 3, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Netherlands', 'away': 'Brazil', 'home_point': 2, 'away_point': 1, 'dif': 1, 'home_rank': 4, 'away_rank': 1, 'round': 8, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Uruguay', 'away': 'Ghana', 'home_point': 1, 'away_point': 1, 'dif': 0, 'home_rank': 16, 'away_rank': 32, 'round': 8, 'home_shootout': 4, 'away_shootout': 2},
{'home': 'Argentina', 'away': 'Germany', 'home_point': 0, 'away_point': 4, 'dif': -4, 'home_rank': 7, 'away_rank': 6, 'round': 8, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Paraguay', 'away': 'Spain', 'home_point': 0, 'away_point': 1, 'dif': -1, 'home_rank': 31, 'away_rank': 2, 'round': 8, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Uruguay', 'away': 'Netherlands', 'home_point': 2, 'away_point': 3, 'dif': -1, 'home_rank': 16, 'away_rank': 4, 'round': 4, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Germany', 'away': 'Spain', 'home_point': 0, 'away_point': 1, 'dif': -1, 'home_rank': 6, 'away_rank': 2, 'round': 4, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Uruguay', 'away': 'Germany', 'home_point': 2, 'away_point': 3, 'dif': -1, 'home_rank': 16, 'away_rank': 6, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Netherlands', 'away': 'Spain', 'home_point': 0, 'away_point': 1, 'dif': -1, 'home_rank': 4, 'away_rank': 2, 'round': 2, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Germany', 'away': 'Sweden', 'home_point': 2, 'away_point': 0, 'dif': 2, 'home_rank': 19, 'away_rank': 16, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Argentina', 'away': 'Mexico', 'home_point': 2, 'away_point': 1, 'dif': 1, 'home_rank': 9, 'away_rank': 4, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'England', 'away': 'Ecuador', 'home_point': 1, 'away_point': 0, 'dif': 1, 'home_rank': 10, 'away_rank': 39, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Portugal', 'away': 'Netherlands', 'home_point': 1, 'away_point': 0, 'dif': 1, 'home_rank': 7, 'away_rank': 3, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Italy', 'away': 'Australia', 'home_point': 1, 'away_point': 0, 'dif': 1, 'home_rank': 13, 'away_rank': 43, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Switzerland', 'away': 'Ukraine', 'home_point': 0, 'away_point': 0, 'dif': 0, 'home_rank': 35, 'away_rank': 45, 'round': 16, 'home_shootout': 0, 'away_shootout': 3},
{'home': 'Brazil', 'away': 'Ghana', 'home_point': 3, 'away_point': 0, 'dif': 3, 'home_rank': 1, 'away_rank': 48, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Spain', 'away': 'France', 'home_point': 1, 'away_point': 3, 'dif': -2, 'home_rank': 6, 'away_rank': 8, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Germany', 'away': 'Argentina', 'home_point': 1, 'away_point': 1, 'dif': 0, 'home_rank': 19, 'away_rank': 9, 'round': 8, 'home_shootout': 4, 'away_shootout': 2},
{'home': 'Italy', 'away': 'Ukraine', 'home_point': 3, 'away_point': 0, 'dif': 3, 'home_rank': 13, 'away_rank': 45, 'round': 8, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'England', 'away': 'Portugal', 'home_point': 0, 'away_point': 0, 'dif': 0, 'home_rank': 10, 'away_rank': 7, 'round': 8, 'home_shootout': 1, 'away_shootout': 3},
{'home': 'Brazil', 'away': 'France', 'home_point': 0, 'away_point': 1, 'dif': -1, 'home_rank': 1, 'away_rank': 8, 'round': 8, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Germany', 'away': 'Italy', 'home_point': 0, 'away_point': 2, 'dif': -2, 'home_rank': 19, 'away_rank': 13, 'round': 4, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Portugal', 'away': 'France', 'home_point': 0, 'away_point': 1, 'dif': -1, 'home_rank': 7, 'away_rank': 8, 'round': 4, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Germany', 'away': 'Portugal', 'home_point': 3, 'away_point': 1, 'dif': 2, 'home_rank': 19, 'away_rank': 7, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Italy', 'away': 'France', 'home_point': 1, 'away_point': 1, 'dif': 0, 'home_rank': 13, 'away_rank': 8, 'round': 2, 'home_shootout': 5, 'away_shootout': 3},
{'home': 'Germany', 'away': 'Paraguay', 'home_point': 1, 'away_point': 0, 'dif': 1, 'home_rank': 11, 'away_rank': 18, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Denmark', 'away': 'England', 'home_point': 0, 'away_point': 3, 'dif': -3, 'home_rank': 20, 'away_rank': 12, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Sweden', 'away': 'Senegal', 'home_point': 1, 'away_point': 2, 'dif': -1, 'home_rank': 19, 'away_rank': 42, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Spain', 'away': 'Republic of Ireland', 'home_point': 1, 'away_point': 1, 'dif': 0, 'home_rank': 8, 'away_rank': 15, 'round': 16, 'home_shootout': 3, 'away_shootout': 2},
{'home': 'Mexico', 'away': 'United States', 'home_point': 0, 'away_point': 2, 'dif': -2, 'home_rank': 7, 'away_rank': 13, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Brazil', 'away': 'Belgium', 'home_point': 2, 'away_point': 0, 'dif': 2, 'home_rank': 2, 'away_rank': 23, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Japan', 'away': 'Turkey', 'home_point': 0, 'away_point': 1, 'dif': -1, 'home_rank': 32, 'away_rank': 22, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Korea Republic', 'away': 'Italy', 'home_point': 2, 'away_point': 1, 'dif': 1, 'home_rank': 40, 'away_rank': 6, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'England', 'away': 'Brazil', 'home_point': 1, 'away_point': 2, 'dif': -1, 'home_rank': 12, 'away_rank': 2, 'round': 8, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Germany', 'away': 'United States', 'home_point': 1, 'away_point': 0, 'dif': 1, 'home_rank': 11, 'away_rank': 13, 'round': 8, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Spain', 'away': 'Korea Republic', 'home_point': 0, 'away_point': 0, 'dif': 0, 'home_rank': 8, 'away_rank': 40, 'round': 8, 'home_shootout': 3, 'away_shootout': 5},
{'home': 'Senegal', 'away': 'Turkey', 'home_point': 0, 'away_point': 1, 'dif': -1, 'home_rank': 42, 'away_rank': 22, 'round': 8, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Germany', 'away': 'Korea Republic', 'home_point': 1, 'away_point': 0, 'dif': 1, 'home_rank': 11, 'away_rank': 40, 'round': 4, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Brazil', 'away': 'Turkey', 'home_point': 1, 'away_point': 0, 'dif': 1, 'home_rank': 2, 'away_rank': 22, 'round': 4, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Korea Republic', 'away': 'Turkey', 'home_point': 2, 'away_point': 3, 'dif': -1, 'home_rank': 40, 'away_rank': 22, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Germany', 'away': 'Brazil', 'home_point': 0, 'away_point': 2, 'dif': -2, 'home_rank': 11, 'away_rank': 2, 'round': 2, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Italy', 'away': 'Norway', 'home_point': 1, 'away_point': 0, 'dif': 1, 'home_rank': 14, 'away_rank': 7, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Brazil', 'away': 'Chile', 'home_point': 4, 'away_point': 1, 'dif': 3, 'home_rank': 1, 'away_rank': 9, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'France', 'away': 'Paraguay', 'home_point': 1, 'away_point': 0, 'dif': 1, 'home_rank': 18, 'away_rank': 29, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Nigeria', 'away': 'Denmark', 'home_point': 1, 'away_point': 4, 'dif': -3, 'home_rank': 74, 'away_rank': 27, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Germany', 'away': 'Mexico', 'home_point': 2, 'away_point': 1, 'dif': 1, 'home_rank': 2, 'away_rank': 4, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Netherlands', 'away': 'Yugoslavia', 'home_point': 2, 'away_point': 1, 'dif': 1, 'home_rank': 25, 'away_rank': 8, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Romania', 'away': 'Croatia', 'home_point': 0, 'away_point': 1, 'dif': -1, 'home_rank': 22, 'away_rank': 19, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Argentina', 'away': 'England', 'home_point': 2, 'away_point': 2, 'dif': 0, 'home_rank': 6, 'away_rank': 5, 'round': 16, 'home_shootout': 4, 'away_shootout': 3},
{'home': 'Italy', 'away': 'France', 'home_point': 0, 'away_point': 0, 'dif': 0, 'home_rank': 14, 'away_rank': 18, 'round': 8, 'home_shootout': 3, 'away_shootout': 4},
{'home': 'Brazil', 'away': 'Denmark', 'home_point': 3, 'away_point': 2, 'dif': 1, 'home_rank': 1, 'away_rank': 27, 'round': 8, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Netherlands', 'away': 'Argentina', 'home_point': 2, 'away_point': 1, 'dif': 1, 'home_rank': 25, 'away_rank': 6, 'round': 8, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Germany', 'away': 'Croatia', 'home_point': 0, 'away_point': 3, 'dif': -3, 'home_rank': 2, 'away_rank': 19, 'round': 8, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Brazil', 'away': 'Netherlands', 'home_point': 1, 'away_point': 1, 'dif': 0, 'home_rank': 1, 'away_rank': 25, 'round': 4, 'home_shootout': 4, 'away_shootout': 2},
{'home': 'France', 'away': 'Croatia', 'home_point': 2, 'away_point': 1, 'dif': 1, 'home_rank': 18, 'away_rank': 19, 'round': 4, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Netherlands', 'away': 'Croatia', 'home_point': 1, 'away_point': 2, 'dif': -1, 'home_rank': 25, 'away_rank': 19, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Brazil', 'away': 'France', 'home_point': 0, 'away_point': 3, 'dif': -3, 'home_rank': 1, 'away_rank': 18, 'round': 2, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Germany', 'away': 'Belgium', 'home_point': 3, 'away_point': 2, 'dif': 1, 'home_rank': 1, 'away_rank': 27, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Spain', 'away': 'Switzerland', 'home_point': 3, 'away_point': 0, 'dif': 3, 'home_rank': 5, 'away_rank': 12, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Saudi Arabia', 'away': 'Sweden', 'home_point': 1, 'away_point': 3, 'dif': -2, 'home_rank': 34, 'away_rank': 10, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Romania', 'away': 'Argentina', 'home_point': 3, 'away_point': 2, 'dif': 1, 'home_rank': 7, 'away_rank': 8, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Netherlands', 'away': 'Republic of Ireland', 'home_point': 2, 'away_point': 0, 'dif': 2, 'home_rank': 2, 'away_rank': 14, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Brazil', 'away': 'United States', 'home_point': 1, 'away_point': 0, 'dif': 1, 'home_rank': 3, 'away_rank': 23, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Nigeria', 'away': 'Italy', 'home_point': 1, 'away_point': 2, 'dif': -1, 'home_rank': 11, 'away_rank': 4, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Mexico', 'away': 'Bulgaria', 'home_point': 1, 'away_point': 1, 'dif': 0, 'home_rank': 16, 'away_rank': 29, 'round': 16, 'home_shootout': 1, 'away_shootout': 3},
{'home': 'Italy', 'away': 'Spain', 'home_point': 2, 'away_point': 1, 'dif': 1, 'home_rank': 4, 'away_rank': 5, 'round': 8, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Netherlands', 'away': 'Brazil', 'home_point': 2, 'away_point': 3, 'dif': -1, 'home_rank': 2, 'away_rank': 3, 'round': 8, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Bulgaria', 'away': 'Germany', 'home_point': 2, 'away_point': 1, 'dif': 1, 'home_rank': 29, 'away_rank': 1, 'round': 8, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Romania', 'away': 'Sweden', 'home_point': 2, 'away_point': 2, 'dif': 0, 'home_rank': 7, 'away_rank': 10, 'round': 8, 'home_shootout': 4, 'away_shootout': 5},
{'home': 'Bulgaria', 'away': 'Italy', 'home_point': 1, 'away_point': 2, 'dif': -1, 'home_rank': 29, 'away_rank': 4, 'round': 4, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Sweden', 'away': 'Brazil', 'home_point': 0, 'away_point': 1, 'dif': -1, 'home_rank': 10, 'away_rank': 3, 'round': 4, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Sweden', 'away': 'Bulgaria', 'home_point': 4, 'away_point': 0, 'dif': 4, 'home_rank': 10, 'away_rank': 29, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
{'home': 'Brazil', 'away': 'Italy', 'home_point': 0, 'away_point': 0, 'dif': 0, 'home_rank': 3, 'away_rank': 4, 'round': 2, 'home_shootout': 3, 'away_shootout': 2}]


#피파 랭킹 - {연도: 순위} 형태로 정리됨
fifa_ranking = {2014: ['Spain', 'Germany', 'Brazil', 'Portugal', 'Argentina', 'Switzerland', 'Uruguay', 'Colombia', 'Italy', 'England', 'Belgium', 'Greece', 'United States', 'Chile', 'Netherlands', 'Ukraine', 'France', 'Croatia', 'Russia', 'Mexico', 'Bosnia and Herzegovina', 'Algeria', 'Denmark', "Côte d'Ivoire", 'Slovenia', 'Ecuador', 'Scotland', 'Costa Rica', 'Romania', 'Serbia', 'Panama', 'Sweden', 'Honduras', 'Czech Republic', 'Turkey', 'Egypt', 'Ghana', 'Armenia', 'Cape Verde Islands', 'Venezuela', 'Wales', 'Austria', 'IR Iran', 'Nigeria', 'Peru', 'Japan', 'Hungary', 'Tunisia', 'Slovakia', 'Paraguay'], 2010: ['Brazil', 'Spain', 'Portugal', 'Netherlands', 'Italy', 'Germany', 'Argentina', 'England', 'France', 'Croatia', 'Russia', 'Egypt', 'Greece', 'United States', 'Serbia', 'Uruguay', 'Mexico', 'Chile', 'Cameroon', 'Australia', 'Nigeria', 'Norway', 'Ukraine', 'Switzerland', 'Slovenia', 'Israel', "Côte d'Ivoire", 'Romania', 'Turkey', 'Algeria', 'Paraguay', 'Ghana', 'Czech Republic', 'Slovakia', 'Colombia', 'Denmark', 'Sweden', 'Honduras', 'Bulgaria', 'Costa Rica', 'Republic of Ireland', 'Gabon', 'Scotland', 'Ecuador', 'Japan', 'Latvia', 'Korea Republic', 'Burkina Faso', 'Venezuela', 'Lithuania'], 2006: ['Brazil', 'Czech Republic', 'Netherlands', 'Mexico', 'United States', 'Spain', 'Portugal', 'France', 'Argentina', 'England', 'Nigeria', 'Denmark', 'Italy', 'Turkey', 'Cameroon', 'Sweden', 'Egypt', 'Japan', 'Germany', 'Greece', 'Tunisia', 'Uruguay', 'IR Iran', 'Croatia', 'Romania', 'Costa Rica', 'Colombia', 'Senegal', 'Poland', 'Korea Republic', 'Republic of Ireland', "Côte d'Ivoire", 'Paraguay', 'Saudi Arabia', 'Switzerland', 'Morocco', 'Russia', 'Bulgaria', 'Ecuador', 'Norway', 'Slovakia', 'Honduras', 'Australia', 'Serbia and Montenegro', 'Ukraine', 'Jamaica', 'Trinidad and Tobago', 'Ghana', 'Finland', 'Israel'], 2002: ['France', 'Brazil', 'Argentina', 'Colombia', 'Portugal', 'Italy', 'Mexico', 'Spain', 'Netherlands', 'Yugoslavia', 'Germany', 'England', 'United States', 'Romania', 'Republic of Ireland', 'Czech Republic', 'Cameroon', 'Paraguay', 'Sweden', 'Denmark', 'Croatia', 'Turkey', 'Belgium', 'Uruguay', 'Slovenia', 'Honduras', 'Nigeria', 'Russia', 'Costa Rica', 'IR Iran', 'Tunisia', 'Japan', 'Norway', 'Saudi Arabia', 'Trinidad and Tobago', 'Ecuador', 'South Africa', 'Poland', 'Morocco', 'Korea Republic', 'Finland', 'Senegal', 'Egypt', 'Ukraine', 'Chile', "Côte d'Ivoire", 'Peru', 'Australia', 'Slovakia', 'China PR'], 1998: ['Brazil', 'Germany', 'Czech Republic', 'Mexico', 'England', 'Argentina', 'Norway', 'Yugoslavia', 'Chile', 'Colombia', 'United States', 'Japan', 'Morocco', 'Italy', 'Spain', 'Russia', 'Egypt', 'France', 'Croatia', 'Korea Republic', 'Tunisia', 'Romania', 'Zambia', 'South Africa', 'Netherlands', 'Ecuador', 'Denmark', 'Sweden', 'Paraguay', 'Jamaica', 'Austria', 'Australia', 'Bolivia', 'Saudi Arabia', 'Bulgaria', 'Belgium', 'Peru', 'Uruguay', 'Portugal', 'Slovakia', 'Scotland', 'IR Iran', 'Kuwait', "Côte d'Ivoire", 'Lithuania', 'Republic of Ireland', 'Israel', 'Trinidad and Tobago', 'Cameroon', 'Thailand', 'China PR', 'Georgia', 'Turkey', 'Poland', 'Greece', 'Angola', 'Algeria', 'Costa Rica', 'United Arab Emirates', 'Guinea', 'Finland', 'Hungary', 'Zaire', 'Ukraine', 'Ghana', 'Mali', 'Burkina Faso', 'El Salvador', 'Mozambique', 'Quatar', 'FYR Macedonia', 'Iceland', 'Togo', 'Nigeria', 'Guatemala'], 1994: ['Germany', 'Netherlands', 'Brazil', 'Italy', 'Spain', 'Norway', 'Romania', 'Argentina', 'Denmark', 'Sweden', 'Nigeria', 'Switzerland', 'France', 'Republic of Ireland', 'England', 'Mexico', 'Colombia', 'Uruguay', 'Russia', 'Zambia', "Côte d'Ivoire", 'Portugal', 'United States', 'Cameroon', 'Egypt', 'Ghana', 'Belgium', 'Morocco', 'Bulgaria', 'Tunisia', 'Greece', 'Poland', 'Scotland', 'Saudi Arabia', 'Wales', 'Austria', 'Korea Republic', 'Iceland', 'Ecuador', 'Chile', 'Northern Ireland', 'Zimbabwe', 'Bolivia', 'Slovakia', 'Czech Republic', 'Finland', 'Australia', 'Algeria', 'Mali', 'Honduras']}


def raw_to_json(text):
  split_text = text.split(',')
  #1998~2014 월드컵과 1994 월드컵의 문자열 길이가 달라서 1998~2014 월드컵의 split_text에서 빈 문자열을 제거
  if len(split_text) == 13:
    split_text.remove(split_text[1])

  #승부차기를 했을 때
  if len(split_text[5]) != 3:
    home_away_score = int(split_text[5][4])
    home_shootout = int(split_text[5][1])
    away_shootout = int(split_text[5][9])
    json_text = {"home": split_text[4][:-3], "away": split_text[6][3:], "home_point": home_away_score, "away_point": home_away_score, "dif": 0, "home_rank": fifa_ranking[int(split_text[2][:4])].index(split_text[4][:-3]) + 1, "away_rank": fifa_ranking[int(split_text[2][:4])].index(split_text[6][3:]) + 1, "round": 16, "home_shootout": home_shootout, "away_shootout": away_shootout}

  #승부차기를 하지 않았을 때
  else:
    home_point = int(split_text[5].split('–')[0])
    away_point = int(split_text[5].split('–')[1])
    json_text = {"home": split_text[4][:-3], "away": split_text[6][3:], "home_point": home_point, "away_point": away_point, "dif": home_point - away_point, "home_rank": fifa_ranking[int(split_text[2][:4])].index(split_text[4][:-3]) + 1, "away_rank": fifa_ranking[int(split_text[2][:4])].index(split_text[6][3:]) + 1, "round": 16, "home_shootout": 0, "away_shootout": 0}

  #몇 강 경기인지
  if split_text[0] == 'Round of 16':
    json_text['round'] = 16
  elif split_text[0] == 'Quarter-finals':
    json_text['round'] = 8
  elif split_text[0] == 'Semi-finals':
    json_text['round'] = 4
  elif split_text[0] == 'Final':
    json_text['round'] = 2
  
  return json_text



def get_teams_of_league2(worldcup):
    for i in worldcup:
        pass


def get_teams_of_league(worldcup):
  worldcup_str = worldcup.split('\n')
  split_list = [] 
  country_list = []
  dictionary_list = []
  return_dict = [{16: []}, {8:[]}, {4:[]}, {2:[]}, {1:[]}]

#엔터(\n)를 기준으로 쪼개진 값을 딕셔너리 형태로 변환 - split_list로 들어감
  split_list = [raw_to_json(i) for i in worldcup_str]

#참가한 나라들 모두 나열(중복 X) - country_list로 들어감
  country_list = set([j['home'] for j in split_list] + [j['away'] for j in split_list])
  
  for k in country_list:
    #한 나라가 참가한 모든 경기를 team_gamecollection에 넣음
    team_gamecollection = []
    for l in split_list:
      if k == l['home'] or k == l['away']:
        #결승 진출 팀 분리: 우승 팀에는 team_gamecollection에 '우승'을 넣음
        if l['round'] == 2:
          if k == l['home']:
            if l['home_point'] > l['away_point'] or l['home_shootout'] > l['away_shootout']:
              team_gamecollection.append('우승')
            else: 
              team_gamecollection.append(l)
          elif k == l['away']:
            if l['away_point'] > l['home_point'] or l['away_shootout'] > l['home_shootout']:
              team_gamecollection.append('우승')
            else:
              team_gamecollection.append(l)
        else:
          team_gamecollection.append(l)

    #team_gamecollection에 1이 들어간 경우를 확인함
    if '우승' in team_gamecollection:
      #max_level: 몇 강까지 올라갔는지 (우승팀은 1)
      max_level = 1
    else:
      max_level = min([m['round'] for m in team_gamecollection])
    dictionary_list.append({max_level: k}) #{최고 강 수: 나라} 형태로 dictionary_list에 들어감

  #딕셔너리 형태로 들어있는 자료를 return_dict(반환값)에다 집어넣음
  for n in dictionary_list:
    key = list(n.keys())[0]
    value = n[key]
    return_dict[4 - int(math.log2(key))][key].append(value)
  new_re_dict = {}
  for i in return_dict:
    key, value = list(i.keys())[0], list(i.values())[0]
    new_re_dict[key] = value
    # new_re_dict.append()
  return new_re_dict





#tracking_team에서 대상 팀이 어느 경기에서 away 팀으로 배정되는 경우 home과 away의 위치를 바꾸는 함수
def changehomeaway(for_variable):
  cng_home = for_variable['away']
  cng_away = for_variable['home']
  cng_home_p = for_variable['away_point']
  cng_away_p = for_variable['home_point']
  cng_home_f = for_variable['away_rank']
  cng_away_f = for_variable['home_rank']
  cng_home_s = for_variable['away_shootout']
  cng_away_s = for_variable['home_shootout']
  cng_dif = cng_home_p - cng_away_p

  for_variable['home'] = cng_home
  for_variable['away'] = cng_away
  for_variable['home_point'] = cng_home_p
  for_variable['away_point'] = cng_away_p
  for_variable['home_rank'] = cng_home_f
  for_variable['away_rank'] = cng_away_f
  for_variable['home_shootout'] = cng_home_s
  for_variable['away_shootout'] = cng_away_s
  for_variable['dif'] = cng_dif

  return for_variable


def tracking_team(match1, team1):
    #return 형태는 {"Korea" : [경기들ㅎㅎ]}
    for_return = {i:[] for i in team1}

    for team in team1:
        for match in match1:
            if team == match["home"]: 
                for_return[team].append(match)
                
                #승부차기
            elif team == match["away"] : 
                #match
                processed_match = {"home": match["away"],"away" : match["home"], "home_point" : match["away_point"], "away_point" : match["home_point"], 
                "dif" : -match["dif"], "home_rank": match["away_rank"], "away_rank": match["home_rank"], 
                "round" : match["round"],
                "home_point" : match["away_point"], "away_point" : match["home_point"]}
                for_return[team].append(processed_match)

    return for_return



'''
  worldcup_str = team1.split('\n')
  split_list = [] 

#엔터(\n)를 기준으로 쪼개진 값을 딕셔너리 형태로 변환 - split_list로 들어감
  for i in worldcup_str:
    split_list.append(raw_to_json(i))

#참가한 게임임 모두 team_gamecollection에 넣음
  team_gamecollection = []
  for j in split_list:
    if j['home'] == team:
      team_gamecollection.append(j)
    elif j['away'] == team:
      team_gamecollection.append(changehomeaway(j))
  
  return {team: team_gamecollection}
'''







def analysis_to_train(match):
    train_set=[[match["home_point"], match["away_point"], match["dif"], match["home_rank"], match["away_rank"], match["home_rank"]-match["away_rank"]]]
    round_cnt=[0,0,0,0,0]
    if match["round"]==16: round_cnt[0]+=1
    elif match["round"]==8: round_cnt[1]+=1
    elif match["round"]==4: round_cnt[2]+=1
    elif match["round"]==2: round_cnt[3]+=1
    else: round_cnt[4] +=1
    train_set.append(round_cnt)
    return train_set

# c.f) 월드컵 연도 나누는 함수
def worldcup_year(string):
  split_string = string.split('!\n')
  return_list = [n for n in split_string if blank_checker(n) == True]
  return return_list

#worldcup_year(game_string)

# c.f) 빈 문자열 체크해주는 함수
def blank_checker(string):
  if string != '' and string != '!' and string != '! ' and string != '\n':
    return True
  else:
    return False
