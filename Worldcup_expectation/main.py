

import data_structure as ds


f = open("match.txt", 'r', encoding="utf-8")


world_cup = [[]]
world_cup_teams = []
#파일의 line을 하나하나 읽으면서 정보를 가져오는 코드
collection = ""






while True:
    line = f.readline()
    
    if not line: break
    #print(line)
    if line[0] == "!": 
        world_cup_teams.append(ds.get_teams_of_league(collection[:-1:]))

        collection = ""
        world_cup.append([])
    else : 
        world_cup[-1].append(ds.raw_to_json(line))


        collection += str(line)


f.close()

#print(world_cup_teams)

#16강 : [경기]
final_dictionary = {16:[],8:[],4:[],2:[],1:[]}

for round in [16,8,4,2,1]:
    for i in range(len(world_cup_teams)):
        a = ds.tracking_team(world_cup[i], world_cup_teams[i][round])
        for i in a:
            final_dictionary[round] += a[i]



x,y = [],[]
for i in final_dictionary:
    for j in final_dictionary[i]:
        #print(j)
        if i == 16:
            x.append([j["home_point"], j["away_point"], j["dif"], j["home_rank"], j["away_rank"], j["away_rank"]-j["home_rank"]])
            y.append([1,0,0,0,0])
        elif i ==8:
            x.append([j["home_point"], j["away_point"], j["dif"], j["home_rank"], j["away_rank"], j["away_rank"]-j["home_rank"]])
            y.append([0,1,0,0,0])
        elif i ==4:
            x.append([j["home_point"], j["away_point"], j["dif"], j["home_rank"], j["away_rank"], j["away_rank"]-j["home_rank"]])
            y.append([0,0,1,0,0])
        elif i ==2:
            x.append([j["home_point"], j["away_point"], j["dif"], j["home_rank"], j["away_rank"], j["away_rank"]-j["home_rank"]])
            y.append([0,0,0,1,0])
        elif i==1:
            x.append([j["home_point"], j["away_point"], j["dif"], j["home_rank"], j["away_rank"], j["away_rank"]-j["home_rank"]])
            y.append([0,0,0,0,1])

#print(len(x), len(y))
#print(x[:5], y[:5])

#머신러닝부
#x_data = np.array(eval(str(x)))
#y_data = np.array(eval(str(y)))
#print(x_data, type(x_data))
#print(np.array([[-5,4,8,-12,0,-11],[-6,3,21,-1,21,-5],[3,5,6,2,-33,-1]]), type(np.array([[-5,4,8,2,0,1],[-6,3,2,-1,2,-5],[3,5,6,2,3,-1]])))
#x_data = np.array(x)
#y_data = np.array(y)
#k = [[0, 2, -2, 7, 8, 1], [0, 1, -1, 6, 5, -1], [1, 2, -1, 20, 15, -5], [0, 2, -2, 44, 17, -27], [1, 2, -1, 13, 11, -2], [1, 1, 0, 14, 3, -11], [1, 2, -1, 22, 2, -20], [1, 1, 0, 12, 28, 16], [1, 2, -1, 47, 16, -31], [1, 4, -3, 8, 6, -2]]
#l = [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
#ax = [[-5,4,8,-12,0,-11],[-6,3,21,-1,21,-5],[3,5,6,2,-33,-1]]
#by = [[0,1,0,0,0], [0,0,0,1,0], [1,0,0,0,0]]

#인덱스 33부터

###############################
import numpy as np
import tensorflow as tf
import random as rd
tf.random.set_seed(0.03) #하이퍼파라미터 튜닝을 위해 실행시 마다 변수가 같은 초기값 가지게 하기
# 난수 만들기인데.. -> cost function 따라가면서 수렴시켜야하는데 난수에 따라서 발산 ->nan

import copy


x_data = np.array(x)
y_data = np.array(y)
labels = ['16강', '8강', '4강', "준우승", "우승"]



input_1 = tf.keras.layers.Input(shape=(6,))
net = tf.keras.layers.Dense(units=5, activation='softmax')(input_1)
model = tf.keras.models.Model(input_1, net)

def categorical_crossentropy(Y1, predictions2):
    #print(Y1, predictions2)
    cross_entropy1 = tf.math.reduce_sum(Y1 * (-tf.math.log(predictions2)), axis=1) 
    loss = tf.math.reduce_mean(cross_entropy1)

    return loss

optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)

epochs = 100 #100보다 더 넘어가면 과대적합일듯.
for epoch_index in range(epochs):
    with tf.GradientTape() as tape:
        predictions = model(x_data, training=True)
        loss_value = categorical_crossentropy(y_data, predictions)
    gradients = tape.gradient(loss_value, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))

    #print('epoch: {}/{}: loss: {:.4f}'.format(epoch_index + 1, epochs, loss_value.numpy()))


##########모델 예측

# 실제 / 알고리즘 / 사람
# 티

x_test = np.array([
    #[예측하려는 팀의 득점, 상대팀 득점, 득실차, 예측하려는 팀 피파랭킹, 상대 피파랭킹, 피파랭킹 차이]
    [3, 3, 0, 3, 4, 1], #아르헨티나  
    [3, 3, 0, 4, 3, -1], #프랑스  
    [2,1,1,28,9,-19], #한국 포르투갈
    [0,1,-1,51,12,-39] #사우디 (하위권 팀)
    #[]
])


def AI_predict(Input):
    global labels, model
    y_predict = model(np.array([Input])).numpy()
    
    return (labels[y_predict[0].argmax()], y_predict[0][y_predict[0].argmax()])

#[예측하려는 팀의 득점, 상대팀 득점, 득실차, 예측하려는 팀 피파랭킹, 상대 피파랭킹, 피파랭킹 차이]

print(AI_predict([0,1,-1,51,12,-39]))
    

y_predict = model(x_test).numpy()

#print(y_predict) #[[5.441674e-01 5.372047e-04 4.552954e-01]]
#print(y_predict[0]) #[5.441674e-01 5.372047e-04 4.552954e-01]
print(y_predict[0].argmax()) #0
print(labels[y_predict[0].argmax()], y_predict[0][y_predict[0].argmax()]) #
print(labels[y_predict[2].argmax()], y_predict[2][y_predict[2].argmax()]) #
print(labels[y_predict[3].argmax()], y_predict[3][y_predict[3].argmax()]) #












############################## Front-end ###############################3


import tkinter as tk
from tkinter import *
import tkinter.ttk

from PIL import ImageTk, Image
from tkinter import messagebox
import random as rand
from random import *

from tkinter import Tk, Label, Button



root = Tk()
root.title("predicting_platform")
root.geometry('1000x600')




#로고
my_img1 = Image.open('C:/Users/user/Desktop/CA/덱픠.png')
resize_image1 = my_img1.resize((200, 150))
img1 = ImageTk.PhotoImage(resize_image1)

label_logo = tk.Label(root,image=img1)
label_logo.pack()

label_qstn = tk.Label(root, text='왼쪽 열의 나라가 해당 경기의 월드컵에서 최대로 올라간 라운드(강수)는?', font=('Arial', 20), fg='#000033')
label_qstn.pack()
label_qstn2 = tk.Label(root, text='16강/8강/4강/준우승/우승', font=('Arial', 15), fg='#000033')
label_qstn2.pack()


def highest_round(country):
  round_cnt = []


  if country == "Morocco": return "조별리그"
  elif country =="Poland" : return "조별리그"
  for i in ds.game_log:
    if i['home'] == country or i['away'] == country:
      if i['round'] == 2:
        if i['home'] == country:
          if i['home_point'] > i['away_point'] or i['home_shootout'] > i['away_shootout']:
            round_cnt.append(1)
          else:
            round_cnt.append(2)
        elif i['away'] == country:
          if i['away_point'] > i['home_point'] or i['away_shootout'] > i['home_shootout']:
            round_cnt.append(1)
          else:
            round_cnt.append(2)

      else:
        round_cnt.append(i['round'])

  if min(round_cnt) == 1:
    return "우승"
  elif min(round_cnt) == 2:
    return "준우승"
  else:
    return f'{min(round_cnt)}강'



#표에 들어갈 2022 테스트용 데이터
matches_2022 = [
    {'home': 'Netherlands', 'away': 'United States', 'home_point': 3, 'away_point': 1, 'dif': 2, 'home_rank': 8, 'away_rank': 16, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
    {'home': 'Argentina', 'away': 'Australia', 'home_point': 2, 'away_point': 1, 'dif': 1, 'home_rank': 3, 'away_rank': 38, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
    {'home': 'Japan', 'away': 'Croatia', 'home_point': 1, 'away_point': 1, 'dif': 0, 'home_rank': 24, 'away_rank': 12, 'round': 16, 'home_shootout': 1, 'away_shootout': 3},
    {'home': 'Brazil', 'away': 'Korea Republic', 'home_point': 4, 'away_point': 1, 'dif': 3, 'home_rank': 1, 'away_rank': 28, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
    {'home': 'France', 'away': 'Poland', 'home_point': 3, 'away_point': 1, 'dif': 2, 'home_rank': 4, 'away_rank': 26, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
    {'home': 'England', 'away': 'Senegal', 'home_point': 3, 'away_point': 0, 'dif': 3, 'home_rank': 5, 'away_rank': 18, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},
    {'home': 'Morocco', 'away': 'Spain', 'home_point': 0, 'away_point': 0, 'dif': 0, 'home_rank': 22, 'away_rank': 7, 'round': 16, 'home_shootout': 3, 'away_shootout': 2},
    {'home': 'Portugal', 'away': 'Switzerland', 'home_point': 6, 'away_point': 1, 'dif': 5, 'home_rank': 9, 'away_rank': 15, 'round': 16, 'home_shootout': 0, 'away_shootout': 0},

    {'home': 'Netherlands', 'away': 'Argentina', 'home_point': 2, 'away_point': 2, 'dif': 0, 'home_rank': 8, 'away_rank': 3, 'round': 8, 'home_shootout': 3, 'away_shootout': 4},
    {'home': 'Croatia', 'away': 'Brazil', 'home_point': 1, 'away_point': 1, 'dif': 0, 'home_rank': 12, 'away_rank': 1, 'round': 8, 'home_shootout': 4, 'away_shootout': 2},
    {'home': 'England', 'away': 'France', 'home_point': 1, 'away_point': 2, 'dif': -1, 'home_rank': 5, 'away_rank': 4, 'round': 8, 'home_shootout': 0, 'away_shootout': 0},
    {'home': 'Morocco', 'away': 'Portugal', 'home_point': 1, 'away_point': 0, 'dif': 1, 'home_rank': 22, 'away_rank': 9, 'round': 8, 'home_shootout': 0, 'away_shootout': 0},

    {'home': 'Argentina', 'away': 'Croatia', 'home_point': 3, 'away_point': 0, 'dif': 3, 'home_rank': 3, 'away_rank': 12, 'round': 4, 'home_shootout': 0, 'away_shootout': 0},
    {'home': 'France', 'away': 'Morocco', 'home_point': 2, 'away_point': 0, 'dif': 2, 'home_rank': 4, 'away_rank': 22, 'round': 4, 'home_shootout': 0, 'away_shootout': 0},

    {'home': 'Argentina', 'away': 'France', 'home_point': 3, 'away_point': 3, 'dif': 0, 'home_rank': 3, 'away_rank': 4, 'round': 2, 'home_shootout': 4, 'away_shootout': 2}

]

pntsgot_per_match = {'Netherlands': 1.68, 'United States': 1.00, 'Argentina': 1.68, 'Australia': 1.10, 'Japan': 0.82, 'Croatia': 1.00, 'Brazil': 1.92, 'Korea Republic': 1.07, 'France':1.40, 'Poland':0.83, 'England':1.14,'Senegal':1.40,'Morocco':1.16,'Spain':1.81,'Portugal':1.41,'Switzerland':1.13}
pntslost_per_match = {'Netherlands':0.83, 'United States':1.43, 'Argentina':0.86, 'Australia':1.88, 'Japan':1.29, 'Croatia':1.50, 'Brazil':1.00, 'Korea Republic':1.65, 'France':0.60, 'Poland':1.83, 'England':0.85,'Senegal':1.20,'Morocco':1.66,'Spain':1.03,'Portugal':1.00,'Switzerland':1.00}

shootout_odds = {'Korea Republic': 1.0, 'Brazil': 1.0, 'Argentina': 0.67, 'France': 0.5, 'Japan': 0.0, 'Netherlands': 0.33, 'England': 0.0, 'Spain': 0.5, 'Portugal': 1.0, 'Switzerland': 0.0, 'United States': 0, 'Australia':0, 'Croatia':0, 'Poland': 0, 'Morocco':0, 'Senegal':0, 'Switzerland': 0}



#표 시각화

rndm_ind= rand.randrange(14)
match_selected = matches_2022[rndm_ind]

if rand.randrange(0,2):
    match_selected = ds.changehomeaway(match_selected)


print(rndm_ind)

# 표 생성하기. columns는 컬럼 이름, display columns는 실행될 때 보여지는 순서다.
viewer_df=tkinter.ttk.Treeview(root, columns=["index", "home_country", 'away_country'], displaycolumns=["index", "home_country", 'away_country'], height = 5)
viewer_df.pack(padx=20, pady=20)


# 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
viewer_df.column("index", width=150, anchor='center')
viewer_df.heading("index", text='', anchor='center')

viewer_df.column("home_country", width=100, anchor="center")
viewer_df.heading("home_country", text="맞출 팀", anchor="center")
#text=str(random_country_1)
#str(match_selected['home'])

viewer_df.column("away_country", width=100, anchor="center")
viewer_df.heading("away_country", text="상대 팀", anchor="center")
#text=str(random_country_2) str(match_selected['away'])

viewer_df['show'] = 'headings' #index 안 보이게 


# 표에 삽입될 데이터
datavalue_dict=[('득점', str(match_selected['home_point']), str(match_selected['away_point'])), ('승부차기 승률', shootout_odds[match_selected['home']],shootout_odds[match_selected['away']]), ('경기당 평균 득점', pntsgot_per_match[str(match_selected['home'])], pntsgot_per_match[str(match_selected['away'])]), ('경기당 평균 실점', pntslost_per_match[str(match_selected['home'])], pntslost_per_match[str(match_selected['away'])]), ('최대 실적', str(highest_round(match_selected['home'])), str(highest_round(match_selected['away'])))]
# 표에 데이터 삽입
for i in range(len(datavalue_dict)):
    viewer_df.insert('', 'end', text=i, values=datavalue_dict[i], iid=str(i)+"번")



def change_df():
    #myentry.delete(0, 'end')

    global rndm_ind, match_selected
    rndm_ind= rand.randrange(14)
    match_selected = matches_2022[rndm_ind]

    if rand.randrange(0,2):
        match_selected = ds.changehomeaway(match_selected)

    #바꾸고 
    viewer_df.item('0번', text = '0', values=('득점', str(match_selected['home_point']), str(match_selected['away_point'])))
    viewer_df.item('1번', text = '1', values=('승부차기 승률', shootout_odds[match_selected['home']],shootout_odds[match_selected['away']]))
    viewer_df.item('2번', text = '2', values=('경기당 평균 득점', pntsgot_per_match[str(match_selected['home'])], pntsgot_per_match[str(match_selected['away'])]))
    viewer_df.item('3번', text = '3', values=('경기당 평균 실점', pntslost_per_match[str(match_selected['home'])], pntslost_per_match[str(match_selected['away'])]))
    viewer_df.item('4번', text = '4', values= ('최대 실적', str(highest_round(match_selected['home'])), str(highest_round(match_selected['away']))))

    viewer_df.column("home_country", width=100, anchor="center")
    viewer_df.heading("home_country", text="맞출 팀", anchor="center")#

    viewer_df.column("away_country", width=100, anchor="center")
    viewer_df.heading("away_country", text="상대 팀", anchor="center")

   




    
#문구1
label_entry = tk.Label(root, text='알고리즘보다 실제값을 더 잘 예측할 수 있을까요?', font=('Arial', 15), fg='#000033')
label_entry.pack()




#enter 버튼을 누르면, done을 누른 것이나 마찬가지의 효과. get()함수가 그대로 작용된다. 
def shortcut(event):
   if event.state == 0 and event.keysym == 'Return':
        get_prediction()

#잘못된 이름을 입력할 경우 경고문이 뜨게 하고, get()로 가는 아이도 없게. 
def done_error():
    return messagebox.showinfo(message = '16강 / 8강 / 4강 / 준우승 / 우승 중에 선택해서 입력해주세요 !')




#창 닫을 때, 닫히기 전 경고문 뜨게 하는 구문
def closing():
    if messagebox.askyesno(title='Quit?', message = 'Do you really want to quit?'):
        root.destroy()

root.protocol('WM_DELETE_WINDOW', closing)
    
    
#dictionary_random = random.qweqwe(2022~list){'home': 'England', 'away': 'France', 'home_point': 1, 'away_point': 2, 'dif': -1, 'home_rank': 5, 'away_rank': 4, 'round': 8, 'home_shootout': 0, 'away_shootout': 0},

#사람들이 예측하는 값이 입력되는 곳 = Entry
myentry= tk.Entry(root)
myentry.bind('<KeyPress>', shortcut)
myentry.pack(pady=15, padx=15)

labels = ['16강', '8강', '4강', "준우승", "우승"]

qatar = {16: ["United States","Australia","Japan","Korea Republic","Poland","Senegal","Spain","Switzerland"], 8: ["Netherlands", "Brazil", "England", "Portugal"],4:["Croatia","Morocco"], 2: ["France"], 1: ["Argentina"]}

user_prediction = ""
#예측값을 돌려주는 함수
def get_prediction():
    global user_prediction, labels
    #myentry.delete(0, 'end')


    if myentry.get() in labels:
        print(user_prediction)  
        user_prediction = myentry.get()
        
    else:
        user_prediction = myentry.get()
        print(user_prediction)  
        done_error()
        return 0
 
    AI_prediction = AI_predict([match_selected["home_point"],match_selected["away_point"], match_selected["dif"], match_selected["home_rank"], match_selected["away_rank"], match_selected["away_rank"] - match_selected["home_rank"]]) 
    popup = Toplevel(root) 
    popup.geometry('500x500')
    popup.title('prediction_result')
    
    Label(popup, text= "예측결과", font=('Arial', 20)).pack(padx=10, pady=10)

    viewer_df=tkinter.ttk.Treeview(popup, columns=["실제값", '알고리즘 예측값', '유저의 예측값'], displaycolumns=["실제값", '알고리즘 예측값', '유저의 예측값'], height = 1)
    viewer_df.pack(padx=20, pady=20)


    # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등

    viewer_df.column("실제값", width=100, anchor="center")
    viewer_df.heading("실제값", text = '실제값', anchor="center")
    #text=str(random_country_1)

    viewer_df.column("알고리즘 예측값", width=150, anchor="center")
    viewer_df.heading("알고리즘 예측값", text = '알고리즘 예측값', anchor="center")
    #text=str(random_country_2)

    viewer_df.column("유저의 예측값", width=100, anchor="center")
    viewer_df.heading("유저의 예측값", text = '유저의 예측값', anchor="center")
    #match_selected = matches_2022[rndm_ind]
    viewer_df['show'] = 'headings' #index 안 보이게 
    
    
    
   
    datavalue_dict=[(str({j:x for x,i in qatar.items() for j in i}[match_selected['home']]), str(AI_prediction[0]), str(user_prediction))]
   
    for i in range(len(datavalue_dict)):
        viewer_df.insert('', 'end', text=i, values=datavalue_dict[i], iid=str(i)+"번")

    if str(user_prediction) == str(AI_prediction[0]) :
        Label(popup, text= "우와! 알고리즘과 예측결과가 일치하셨어요!", font=('Arial', 15)).pack(padx=20, pady=20)
    elif str(user_prediction) == str({j:x for x,i in qatar.items() for j in i}[match_selected['home']]) :
        Label(popup, text= "우와! 실제값과 일치하셨어요!", font=('Arial', 15)).pack(padx=20, pady=20)
    else:
        Label(popup, text= "흠, 값이 조금 다르군요.", font=('Arial', 15)).pack(padx=20, pady=20)


    




#예측값을 '최종 제출'하는 버튼
done_button = Button(root, text='done', font=('arial', 13), command=get_prediction, relief = 'groove', bg='#000033', fg='white', activebackground='#2a2a5f')
done_button.pack(ipadx=5, ipady=5, expand=False)

change_button = Button(root, text='다른 경기 예측하기',font=('arial', 13), command = change_df, relief = 'groove', bg='#2a2a5f', fg='white', activebackground='#49497c')
change_button.pack(ipadx=5, ipady=5, expand=False, padx=30, pady=30)





#메뉴바
menubar = tk.Menu(root)

#기여한 사람 목록 
def show_people():
    messagebox.showinfo(title='people', message='이서준, 김민서, 전하성, 권예람')

#동아리 설명
def show_info():
    messagebox.showinfo(title='club', message='소프트웨어와 하드웨어 프로젝트를 동료들과 함께 다루는 공학 연합 동아리')
 
aboutmenu= tk.Menu(menubar, tearoff = 0)
aboutmenu.add_command(label='contributers', command = show_people)
aboutmenu.add_command(label='what is DECFI', command = show_info)

menubar.add_cascade(menu=aboutmenu, label = 'About')

    
root.config(menu=menubar)



root.mainloop()

        
        
        
        
        
        
