# -*- coding: utf-8 -*-
import tensorflow as tf
#"2��2�еľ���"
x=tf.constant(
        [[1,2],[3,4]]
        ,tf.float32
        )
#"2��1�еľ���"
w=tf.constant([[-1],[-2]],tf.float32)
#"����ĳ˷�"
y=tf.matmul(x,w)
#"�����Ự"
session=tf.Session()
#"��ӡ������˺�Ľ��"
print(session.run(y))