# -*- coding: utf-8 -*-
import tensorflow as tf
#"����"
t=tf.constant(
        [
        [1,2,3],
        [4,5,6]
        ]
        ,tf.float32)
session=tf.Session()
#"��������״"
s=tf.shape(t)
print('��������״:',session.run(s))