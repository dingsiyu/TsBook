# -*- coding: utf-8 -*-
import tensorflow as tf
#"2��3��2��ȵ���ά����"
x=tf.constant(
        [
        [[2,5],[3,4],[8,2]],
        [[6,1],[1,2],[5,4]]
        ],tf.float32
        )
#"�����Ự"
session = tf.Session()
#"ÿһ��(0,1)ƽ���ת��"
r=tf.transpose(x,perm=[1,0,2])
print(session.run(r))