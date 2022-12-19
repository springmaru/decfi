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
print(x[:5], y[:5])



#머신러닝부
###############################
###############################
###############################
###############################
###############################
###############################
###############################



from keras.models import Sequential
from keras.layers import Dense
import numpy as np
 
import tensorflow as tf
tf.random.set_seed(777) #하이퍼파라미터 튜닝을 위해 실행시 마다 변수가 같은 초기값 가지게 하기
#import main
##########데이터 로드

x_data = np.array(x)

y_data = np.array(y)
#print(y)
#print(y_data.tolist())

labels = ['16강', '8강', '4강', "준우승", "우승"]



input_1 = tf.keras.layers.Input(shape=(6,))
net = tf.keras.layers.Dense(units=5, activation='softmax')(input_1)
model = tf.keras.models.Model(input_1, net)

def categorical_crossentropy(Y1, predictions2):
    #print(predictions)
    cross_entropy1 = tf.math.reduce_sum(Y1 * (-tf.math.log(predictions2)), axis=1) 
    loss = tf.math.reduce_mean(cross_entropy1)

    return loss
    
optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)

epochs = 100
for epoch_index in range(epochs):
    with tf.GradientTape() as tape:
        predictions = model(x_data, training=True)
        loss_value = categorical_crossentropy(y_data, predictions)
    gradients = tape.gradient(loss_value, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))

    print('epoch: {}/{}: loss: {:.4f}'.format(epoch_index + 1, epochs, loss_value.numpy()))

'''
#내장 루프
def categorical_crossentropy(Y, predictions):
    cross_entropy = tf.reduce_sum(Y * (-tf.math.log(predictions)), axis=1) 
    loss = tf.reduce_mean(cross_entropy)

    return loss

model.compile(loss=categorical_crossentropy, optimizer='adam')
#model.compile(loss=categorical_crossentropy, optimizer=tf.keras.optimizers.Adam(learning_rate=0.01))

model.fit(x_train, y_train, epochs=50) 
'''

##########모델 예측

x_test = np.array([
    [4, 6, 7, 8, 9, 1]
])

y_predict = model(x_test).numpy()

print(y_predict) #[[5.441674e-01 5.372047e-04 4.552954e-01]]
print(y_predict[0]) #[5.441674e-01 5.372047e-04 4.552954e-01]
print(y_predict[0].argmax()) #0
label = labels[y_predict[0].argmax()]
confidence = y_predict[0][y_predict[0].argmax()]
print(label, confidence) #
