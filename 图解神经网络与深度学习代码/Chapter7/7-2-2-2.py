# -*- coding: utf-8 -*-
import tensorflow as tf
#"��ά����"
x=tf.constant([[1,2,3],[4,5,6]],tf.float32)
#"�����߽����䣬�ϲಹ1��10���²ಹ2��10���Ҳಹ1��10"
r=tf.pad(x,[[1,2],[0,1]],mode='CONSTANT',constant_values=10)
#"�����Ự"
session=tf.Session()
#"��ӡ�߽������Ľ��"
print(session.run(r))