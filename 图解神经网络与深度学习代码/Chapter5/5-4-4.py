# -*- coding: utf-8 -*-
import tensorflow as tf
#"����"
x=tf.Variable(tf.constant([[2,1,3]],tf.float32))
w=tf.constant([[2],[3],[4]],tf.float32)
#"����g"
g=tf.matmul(x,w)
#"����f=leaky\_relu(g)"
f=tf.nn.leaky_relu(g,alpha=0.2)
#"ţ���ݶ��½���"
opti=tf.train.GradientDescentOptimizer(0.5).minimize(f)
session=tf.Session()
session.run(tf.global_variables_initializer())
#"��ӡ���"
for i in range(3):
    session.run(opti)
    print('��%d�ε���ֵ'%(i+1))
    print(session.run(x))