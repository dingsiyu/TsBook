# -*- coding: utf-8 -*-
import tensorflow as tf
#"��ά����"
t=tf.constant([[1,2,3],[4,5,6]],tf.float32)
#"ˮƽ����"
rh=tf.reverse(t,axis=[0])
#"��ֱ����"
rv=tf.reverse(t,axis=[1])
#"��ʱ�뷭ת180�㣺����ˮƽ�����ֱ����(�����ȴ�ֱ�����ˮƽ����)"
r=tf.reverse(t,axis=[0,1])
#"�����Ự"
session=tf.Session()
#"��ӡ���"
print('ˮƽ����Ľ��')
print(session.run(rh))
print('��ֱ����Ľ��')
print(session.run(rv))
print('��ʱ�뷭ת180�Ľ��')
print(session.run(r))