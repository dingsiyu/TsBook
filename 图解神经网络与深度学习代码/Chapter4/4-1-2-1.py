# -*- coding: utf-8 -*-
import tensorflow as tf
#"��1��Variable����ʼ��Ϊһ������Ϊ3��һά����"
v1=tf.Variable(tf.constant([1,2,3],tf.float32),dtype=tf.float32,name='v1')
#"��2��Variable����ʼ��Ϊһ������Ϊ2��һά����"
v2=tf.Variable(tf.constant([4,5],tf.float32),dtype=tf.float32,name='v2')
#"����һ��tf.train.Saver����"
saver =tf.train.Saver()
#"�����Ự"
session=tf.Session()
#"��ʼ������"
session.run(tf.global_variables_initializer())
#"������ v1 �� v2 ���浽��ǰ�ļ����µ�model.ckpt�ļ���"
save_path=saver.save(session,'./model.ckpt')
session.close()