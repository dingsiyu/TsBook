# -*- coding: utf-8 -*-
import tensorflow as tf
#"����Ϊ3��һά����"
t1=tf.constant([1,2,3],tf.float32)
#"����Ϊ3��һά����"
t2=tf.constant([7,8,9],tf.float32)
#"��0�����϶ѵ�"
t=tf.stack([t1,t2],0)
session=tf.Session()
#"��ӡ���"
print(session.run(t))