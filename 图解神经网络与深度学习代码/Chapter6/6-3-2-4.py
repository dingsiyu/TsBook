# -*- coding: utf-8 -*-
import tensorflow as tf
#"����\_yΪȫ������������(�������3����Ԫ)"
_y=tf.constant([[0,2,-3],[4,-5,6]],tf.float32)
#"�˹�������"
y=tf.constant([[1,0,0],[0,0,1]],tf.float32)
#"softmax��"
entroy=tf.nn.softmax_cross_entropy_with_logits_v2(logits=_y,labels=y)
#"loss"
loss=tf.reduce_sum(entroy)
#"�����Ự"
session=tf.Session()
#"��ӡ���"
print(session.run(loss))