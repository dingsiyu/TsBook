# -*- coding: utf-8 -*-
import tensorflow as tf
#"����Ķ�ά����"
t=tf.constant(
        [
        [1,3,2,6],
        [7,5,4,9]
        ],tf.float32
        )
#"dropout����"
r=tf.nn.dropout(t,0.5)
#"�����Ự"
session=tf.Session()
#"��ӡ���"
print(session.run(r))