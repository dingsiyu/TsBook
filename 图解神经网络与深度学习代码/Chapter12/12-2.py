# -*- coding: utf-8 -*-
import tensorflow as tf
#"��ʼ��x��ֵ"
x=tf.Variable(tf.constant([
                           [
                           [[8],[2],[9],[3]],
                           [[4],[6],[7],[10]],
                           [[20],[13],[1],[5]],
                           [[12],[18],[19],[14]]
                           ]
                           ],tf.float32),dtype=tf.float32)
#"2x2���룬����Ϊ2x2����󻯳ػ�����"
x_maxPool=tf.nn.max_pool(x,(1,2,2,1),(1,2,2,1),'VALID')
#"�����ϵ���󻯳ػ����������ƽ����"
F=tf.reduce_sum(tf.square(x_maxPool))
#"�����Ự"
session=tf.Session()
session.run(tf.global_variables_initializer())
#"�ݶ��½���"
opti=tf.train.GradientDescentOptimizer(0.5).minimize(F)
#"��ӡǰ2�εĽ��"
for i in range(2):
    session.run(opti)
    print(session.run(x))