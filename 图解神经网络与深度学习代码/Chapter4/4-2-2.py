# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
#"��һ������֪����"
xy=tf.placeholder(tf.float32,[None,2])
z=tf.placeholder(tf.float32,[None,1])
#"�ڶ�������ʼ������"
w=tf.Variable(tf.constant([[1],[1]],tf.float32),dtype=tf.float32,name='w')
#"��������������ʧ����"
loss=tf.reduce_sum(tf.square(z-tf.matmul(xy,w)))
#"���Ĳ����ݶ��½���������"
opti=tf.train.GradientDescentOptimizer(0.005).minimize(loss)
#"ѵ������"
xy_train=np.array([[1,1],[2,1],[3,2],
                   [1,2],[4,5],[5,8]
                   ],np.float32)
z_train=np.array([[8],[12],[10],[14],[28],[10]],np.float32)
#"���岽�������Ự��ѵ��ģ��"
session=tf.Session()
for i in range(500):
    session.run(opti,feed_dict={xy:xy_train,z:z_train})