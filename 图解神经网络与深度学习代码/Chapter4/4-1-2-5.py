# -*- coding: utf-8 -*-
import tensorflow as tf
#"���ֵ���������"
weights={
        'w1':tf.Variable([1,13,22],dtype=tf.float32,name='w1'),
        'w2':tf.Variable([31,32],dtype=tf.float32,name='w2')
        }
bias={
      'b1':tf.Variable([2,12],dtype=tf.float32,name='b1'),
      'b2':tf.Variable(23,dtype=tf.float32,name='b2')
      }
#"����һ��tf.train.Saver��"
saver=tf.train.Saver()
with tf.Session() as sess:
    #"���� modelMul.ckpt �ļ�"
    saver.restore(sess,'./modelMul.ckpt')
    #"��ӡֵ"
    print(sess.run(weights['w1']))
    print(sess.run(weights['w2']))
    print(sess.run(bias['b1']))
    print(sess.run(bias['b2']))
sess.close()