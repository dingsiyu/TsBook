# -*- coding: utf-8 -*-
import tensorflow as tf
#"�ݶ��½��ĳ�ʼ��"
x=tf.Variable(tf.constant([-4,4],tf.float32),tf.float32)
#"����"
y=tf.reduce_sum(tf.square(x))
#"�����Ự"
session=tf.Session()
session.run(tf.global_variables_initializer())
#"�ݶ��½�,���ò���Ϊ0.25"
opti=tf.train.GradientDescentOptimizer(0.25).minimize(y)
#"2�ε���"
for i in range(2):
    session.run(opti)
    #"��ӡÿ�ε�����ֵ"
    print(session.run(x))