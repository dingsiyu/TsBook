# -*- coding: utf-8 -*-
import tensorflow as tf
#"����"
t=tf.constant(
        [
        [False,True,False],
        [False,False,True]
        ]
        ,tf.bool)
session=tf.Session()
#"bool��ת��Ϊ��ֵ��"
r=tf.cast(t,tf.float32)
print(session.run(r))