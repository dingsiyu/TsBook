# -*- coding: utf-8 -*-
import tensorflow as tf
#"����"
t=tf.constant(
        [
        [0,2,0],
        [0,0,1]
        ]
        ,tf.float32)
session=tf.Session()
#"��ֵ��ת��Ϊbool����"
r=tf.cast(t,tf.bool)
print(session.run(r))