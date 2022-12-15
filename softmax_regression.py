# https://wikidocs.net/35476
import numpy as np
import tensorflow as tf
tf.random.set_seed(777) #하이퍼파라미터 튜닝을 위해 실행시 마다 변수가 같은 초기값 가지게 하기

##########데이터 로드

x_data = np.array([
    [1, 2], 
    [3, 4],
    [4, 6], #[자기점수, 상대점수, 득실, 자기 피파 랭킹, 상대 랭킹]
    [4, 6],
    [4, 6],
    [2, 5],
    [8, 9],
    [9, 10],
    [6, 12],
    [9, 2],
    [6, 10],
    [4, 6]
])
y_data = np.array([
    [0 ,0, 1], 
    [0 ,0, 1],  #[16강, 8강,4강,준우승,우승]
    [1 ,0, 0], 
    [1 ,0, 0], 
    [1 ,0, 0], 
    [0 ,0, 1], 
    [0 , 1, 0], 
    [0 ,0, 1], 
    [1 ,0, 0], 
    [0 ,1, 0], 
    [1 ,0, 0], 
    [0 ,0, 1]
])

labels = ['A', 'B', 'C']

# 판 만들기 > 1. 2. 다중분류 (소프트맥스 회귀)
##########모델 생성

input = tf.keras.layers.Input(shape=(2,))
net = tf.keras.layers.Dense(units=3, activation='softmax')(input)
model = tf.keras.models.Model(input, net)

##########모델 학습 및 검증

def categorical_crossentropy(Y, predictions):
    cross_entropy = tf.math.reduce_sum(Y * (-tf.math.log(predictions)), axis=1) 
    loss = tf.math.reduce_mean(cross_entropy)

    return loss
optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)

epochs = 50
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
    [4, 6]
])

y_predict = model(x_test).numpy()

print(y_predict) #[[5.441674e-01 5.372047e-04 4.552954e-01]]
print(y_predict[0]) #[5.441674e-01 5.372047e-04 4.552954e-01]
print(y_predict[0].argmax()) #0
label = labels[y_predict[0].argmax()]
confidence = y_predict[0][y_predict[0].argmax()]
print(label, confidence) #
