# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
#"ռλ������֪����"
x=tf.placeholder(tf.float32,(None,1))
keep_pro=tf.placeholder(tf.float32)
#"����㵽�������Ȩ�ؾ���"
w1=tf.Variable(tf.constant([[10]],tf.float32),dtype=tf.float32)
l1=tf.matmul(x,w1)
#" dropout ��"
l1_dropout=tf.nn.dropout(l1,keep_pro)
#"�����㵽������Ȩ�ؾ���"
w2=tf.Variable(tf.constant([[6]],tf.float32),dtype=tf.float32)
l=tf.matmul(l1_dropout,w2)
#"�����������ֵ���캯��f"
f=tf.reduce_sum(l)
#"�ݶ��½���"
opti=tf.train.GradientDescentOptimizer(0.01).minimize(f)
#"���������ֵ"
x_array=np.array([[3]],np.float32)
#"4�ε�������ӡÿһ�ε����������ֵ������Ȩ��"
with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    for i in range(4):
        _,l1_dropout_array=session.run([opti,l1_dropout],
                            {x:x_array,keep_pro:0.5})
        print('"----��"{}"�ε���"----'.format(i+1))
        print("'dropout���ֵ'")
        print(l1_dropout_array)
        print('���統ǰ��Ȩ��')
        print(session.run([w1,w2]))