# -*- coding: utf-8 -*-
import tensorflow as tf
#"��ʼ������2����������״��model.cpkt�ļ��б����Ǳ�����ȵ�"
v1=tf.Variable([11,12,13],dtype=tf.float32,name='v1')
v2=tf.Variable([15,16],dtype=tf.float32,name='v2')
#"����һ��tf.train.Saver��"
saver =tf.train.Saver()
with tf.Session() as sess:
    #"����model.ckpt�ļ�"
    saver.restore(sess,'./model.ckpt')
    #"��ӡ����������ֵ"
    print(sess.run(v1))
    print(sess.run(v2))
sess.close()