# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
#"��һ������֪����"
x=tf.placeholder(tf.float32,[None])
y=tf.placeholder(tf.float32,[None])
z=tf.placeholder(tf.float32,[None])
#"�ڶ�������ʼ������"
w1=tf.Variable(initial_value=2.0,dtype=tf.float32,name='w1')
w2=tf.Variable(initial_Value=2.0,dtype=tf.float32,name='w2')
#"��������������ʧ����"
loss=tf.reduce_sum(tf.square(z-tf.pow((w1*x+w2*y),2.0)))
#"���Ĳ����ݶ��½���������"
opti=tf.train.GradientDescentOptimizer(0.005).minimize(loss)
#"ѵ������"
x_train=np.array([1,2,3,1,4,5],np.float32)
y_train=np.array([1,1,2,2,5,8],np.float32)
z_train=np.array([8,12,10,14,28,10],np.float32)
#"���岽�������Ự��ѵ��ģ��"
session=tf.Session()
for i in range(500):
    session.run(opti,feed_dict={x:x_train,y:y_train,z:z_train})