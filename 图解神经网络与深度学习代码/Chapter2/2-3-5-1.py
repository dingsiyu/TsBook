# -*- coding: utf-8 -*-
import tensorflow as tf
#"һά����"
t1d=tf.constant([3,4,1,5],tf.float32)
#"���"
sum0=tf.reduce_sum(t1d)
#"��ӡ���"
session=tf.Session()
print(session.run(sum0))