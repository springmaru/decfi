import numpy as np
import tensorflow as tf
tf.random.set_seed(777) #하이퍼파라미터 튜닝을 위해 실행시 마다 변수가 같은 초기값 가지게 하기
#import main
##########데이터 로드
import random as rd

print([[rd.randint(-10,10),rd.randint(1,10),rd.randint(1,10),rd.randint(1,10),rd.randint(1,10),rd.randint(1,10)] for i in range(1,3)])
print([ [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]][rd.randrange(0,5)] for i in range(1,3)])
x_data = np.array([[rd.randint(-10,10),rd.randint(1,10),rd.randint(1,10),rd.randint(1,10),rd.randint(1,10),rd.randint(1,10)] for i in range(1,100)])

y_data = np.array([ [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]][rd.randrange(0,5)] for i in range(1,100)])
labels = ['16강', '8강', '4강', "준우승", "우승"]

# analysis_to_train(match)

# 판 만들기 > 1. 2. 다중분류 (소프트맥스 회귀)
##########모델 생성

input = tf.keras.layers.Input(shape=(6,))
net = tf.keras.layers.Dense(units=5, activation='softmax')(input)
model = tf.keras.models.Model(input, net)

##########모델 학습 및 검증

def categorical_crossentropy(Y, predictions):
    cross_entropy = tf.math.reduce_sum(Y * (-tf.math.log(predictions)), axis=1) 
    loss = tf.math.reduce_mean(cross_entropy)

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
