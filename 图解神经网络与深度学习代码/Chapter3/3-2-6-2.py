# -*- coding: utf-8 -*-
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import math
#"���Ƚ�������ʼ��:�ݶ��½��ĳ�ʼ��"
x=tf.Variable(15.0,dtype=tf.float32)
#"����"
y=tf.pow(x-1,2.0)
#"�ݶ��½�,����ѧϰ��Ϊ0.25"
opti=tf.train.GradientDescentOptimizer(0.05).minimize(y)
#"������"
value=np.arange(-15,17,0.01)
y_value=np.power(value-1,2.0)
plt.plot(value,y_value)
#"�����Ự"
session=tf.Session()
session.run(tf.global_variables_initializer())
#"���ε���"
for i in range(100):
    session.run(opti)
    if(i%10==0):
        v=session.run(x)
        plt.plot(v,math.pow(v-1,2.0),'go')
        print('�� %d �ε� x �ĵ���ֵ: %f'%(i+1,v))
plt.show()