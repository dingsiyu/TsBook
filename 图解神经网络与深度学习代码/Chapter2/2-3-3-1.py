# -*- coding: utf-8 -*-
import tensorflow as tf
#"2��3�еĶ�ά����"
x=tf.constant(
        [
        [1,2,3],
        [4,5,6]
        ],tf.float32
        )
#"�����Ự"
session = tf.Session()
#"ת��"
r=tf.transpose(x,perm=[1,0])
print(session.run(r))