# -*- coding: utf-8 -*-
import tensorflow as tf
#"��ά����"
t1=tf.constant(
        [
        [1,5,7],
        [2,3,8]
        ],tf.float32
        )
#"��ά����"
t2=tf.constant(
        [
        [2,5,6],
        [7,1,8]
        ],tf.float32
        )
#"���������ĶԱ�"
r=tf.equal(t1,t2)
#"�����Ự"
session=tf.Session()
#"��ӡ���"
print(session.run(r))