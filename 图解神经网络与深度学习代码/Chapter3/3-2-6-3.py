# -*- coding: utf-8 -*-
import tensorflow as tf
#"�ݶ��½��ĳ�ʼ��"
x1=tf.Variable(-4.0,dtype=tf.float32)
x2=tf.Variable(4.0,dtype=tf.float32)
#"����"
y=tf.square(x1)+tf.square(x2)
#"�����Ự"
session=tf.Session()
session.run(tf.global_variables_initializer())
#"�ݶ��½�,���ò���Ϊ0.25"
opti=tf.train.GradientDescentOptimizer(0.25).minimize(y)
#"2�ε���"
for i in range(2):
    session.run(opti)
    #"��ӡÿ�ε�����ֵ"
    print((session.run(x1),session.run(x2)))