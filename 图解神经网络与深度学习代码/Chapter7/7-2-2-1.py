# -*- coding: utf-8 -*-
import tensorflow as tf
#"һά����"
x=tf.constant([2,1],tf.float32)
#"�����߽����䣬�ϲಹ1��0���²ಹ2��0"
r=tf.pad(x,[[1,2]],mode='CONSTANT')
#"�����Ự"
session=tf.Session()
#"��ӡ�߽������Ľ��"
print(session.run(r))