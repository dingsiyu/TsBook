# -*- coding: utf-8 -*-
import tensorflow as tf
#"��������"
x=tf.constant([[1,2,1],
               [2,2,2]],tf.float32)
#"�ֱ��ÿһ�У���"1"���򣩽���softmax����"
s=tf.nn.softmax(x,1)
#"�����Ự"
session=tf.Session()
#"��ӡ���"
print(session.run(s))