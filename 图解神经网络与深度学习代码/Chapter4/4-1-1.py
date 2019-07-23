# -*- coding: utf-8 -*-
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
#"6����ĺ�����"
x=tf.constant([1,2,3,4,5,6],tf.float32)
#"6�����������"
y=tf.constant([3,4,7,8,11,14],tf.float32)
#"��ʼ��ֱ�ߵ�б��"
w=tf.Variable(1.0,dtype=tf.float32)
#"��ʼ��ֱ�ߵĽؾ�"
b=tf.Variable(1.0,dtype=tf.float32)
#"6���㵽ֱ����ֵ�����Ͼ����ƽ����"
loss=tf.reduce_sum(tf.square(y-(w*x+b)))
#�����Ự
session=tf.Session()
session.run(tf.global_variables_initializer())
#"�ݶ��½���"
opti=tf.train.GradientDescentOptimizer(0.005).minimize(loss)
#"��¼ÿһ�ε������ƽ��ƽ�����(Mean Squared Error)"
MSE=[]
#"ѭ��500��"
for i in range(500):
    session.run(opti)
    MSE.append(session.run(loss))
    #"ÿ��50�δ�ӡֱ�ߵ�б�ʺͽؾ�"
    if i%50==0:
        print((session.run(w),session.run(b)))
#"������ʧ������ֵ"
plt.figure(1)
plt.plot(MSE)
plt.show()
#"����6���㼰���������ֱ��"
plt.figure(2)
x_array,y_array=session.run([x,y])
plt.plot(x_array,y_array,'o')
xx=np.arange(0,10,0.05)
yy=session.run(w)*xx+session.run(b)
plt.plot(xx,yy)
plt.show()