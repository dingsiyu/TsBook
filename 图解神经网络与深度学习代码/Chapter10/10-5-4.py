# -*- coding: utf-8 -*-
import tensorflow as tf
#"��ʼ���������� t=1 ʱ��ֵ"
x=tf.Variable(initial_value=5,dtype=tf.float32,trainable=False,name='v')
#"���������ƶ�ƽ���Ķ���"
exp_moving_avg=tf.train.ExponentialMovingAverage(0.7)
update_moving_avg=exp_moving_avg.apply([x])
#"�����Ự"
session=tf.Session()
session.run(tf.global_variables_initializer())
for i in range(4):
    #"��ӡָ���ƶ�ƽ��ֵ"
    session.run(update_moving_avg)
    print('��{}�ε��ƶ�ƽ��ֵ:'.format(i+1))
    print(session.run(exp_moving_avg.average(x)))
    session.run(x.assign_add(5))