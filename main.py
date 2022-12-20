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
###############################
import numpy as np
import tensorflow as tf
import random as rd
tf.random.set_seed(0.03) #하이퍼파라미터 튜닝을 위해 실행시 마다 변수가 같은 초기값 가지게 하기

import copy
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

x_test = np.array([
    [3, 3, 0, 3, 4, 1], #아르헨티나  
    [3, 3, 0, 4, 3, -1], #프랑스  
    [2,1,1,28,9,-19], #한국 포르투갈
    [0,1,-1,51,12,-39]
    #[]
])

y_predict = model(x_test).numpy()

#print(y_predict) #[[5.441674e-01 5.372047e-04 4.552954e-01]]
#print(y_predict[0]) #[5.441674e-01 5.372047e-04 4.552954e-01]
print(y_predict[0].argmax()) #0
print(labels[y_predict[0].argmax()], y_predict[0][y_predict[0].argmax()]) #
print(labels[y_predict[2].argmax()], y_predict[2][y_predict[2].argmax()]) #
print(labels[y_predict[3].argmax()], y_predict[3][y_predict[3].argmax()]) #
