# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
#"�Ա���(x,y)ֵ"
xy=tf.placeholder(tf.float32,[None,2])
#"��ʼ��z=w1*x+w2*y+b�е�w1��w2��b"
w=tf.Variable(tf.constant([[1],[1]],tf.float32),dtype=tf.float32,name='w')
b=tf.Variable(1.0,dtype=tf.float32,name='b')
#"��ƽ��"
z=tf.matmul(xy,w)+b
#"����һ��tf.train.Saver��"
saver=tf.train.Saver()
#"���ļ�����'./regression'�»�������ckpt�ļ�"
ckpt=tf.train.latest_checkpoint('./regression')
#"��ӡ���ص�ckpt�ļ���"
print('��õ�ckpt�ļ�:'+ckpt)
#"�����Ự"
session=tf.Session()
#"����ckpt�ļ��еı���w��b��ֵ"
saver.restore(session,ckpt)
#"����������(6,7)��(8,10)����ֵ"
pred=session.run(z,feed_dict={xy:np.array([[6,7],[8,10]],np.float32)})
print('������(6,7)��(8,10)����ֵ:')
print(pred)