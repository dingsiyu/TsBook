# -*- coding: utf-8 -*-
import tensorflow as tf
#"���Ƚ�������ʼ��:�ݶ��½��ĳ�ʼ��"
x=tf.Variable(4.0,dtype=tf.float32)
#"����"
y=tf.pow(x-1,2.0)
#"�ݶ��½�,ѧϰ��Ϊ0.25"
opti=tf.train.GradientDescentOptimizer(0.25).minimize(y)
#"�����Ự"
session=tf.Session()
session.run(tf.global_variables_initializer())
#"���ε���"
for i in range(3):
    session.run(opti)
    #"��ӡÿ�ε�����ֵ"
    print(session.run(x))