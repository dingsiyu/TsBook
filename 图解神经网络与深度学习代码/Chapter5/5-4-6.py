# -*- coding: utf-8 -*-
import tensorflow as tf
#"��������"
t=tf.constant([-2,0,1],tf.float32)
#"celu�����"
r=tf.nn.crelu(t)
#"�����Ự"
session=tf.Session()
#"��ӡ���"
print(session.run(r))