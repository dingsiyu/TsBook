# -*- coding: utf-8 -*-
import tensorflow as tf
#"���ֵ���������"
weights={
        'w1':tf.Variable([11,12,13],dtype=tf.float32,name='w1'),
        'w2':tf.Variable([21,22],dtype=tf.float32,name='w2')
        }
bias={
      'b1':tf.Variable([101,102],dtype=tf.float32,name='b1'),
      'b2':tf.Variable(2,dtype=tf.float32,name='b2')
      }
#"�����Ự"
session=tf.Session()
#"����һ��tf.train.Saver��"
saver=tf.train.Saver()
with tf.Session() as sess:
    #"������ʼ��"
    sess.run(tf.global_variables_initializer())
    #"�����������ڵ�ǰ�ļ����µ� modelMul.ckpt �ļ���"
    saver.save(sess,'./modelMul.ckpt')