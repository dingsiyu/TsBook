# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
#"ռλ��"
x=tf.placeholder(tf.float32,[None,2])
keep_prob=tf.placeholder(tf.float32)
#"����㵽�������Ȩ�ؾ���"
w1=tf.constant([
        [1,3,5],
        [2,4,6]
        ],tf.float32)
#"�������ֵ"
h1=tf.matmul(x,w1)
#"dropout��"
h1_dropout=tf.nn.dropout(h1,keep_prob)
#"dropout�㵽������Ȩ�ؾ���"
w2=tf.constant(
        [
        [8,3],
        [7,2],
        [6,1]
        ],tf.float32
        )
#"������ֵ"
o=tf.matmul(h1_dropout,w2)
x_input=np.array([[2,3],[1,4]],np.float32)
#"�����Ự"
session=tf.Session()
h1_arr,h1_dropout_arr,o_arr=s=session.run(
        [h1,h1_dropout,o],feed_dict={x:x_input,keep_prob:0.5})
#"��ӡ���"
print('�������ֵ:')
print(h1_arr)
print("'dropout���ֵ:'")
print(h1_dropout_arr)
print('������ֵ:')
print(o_arr)