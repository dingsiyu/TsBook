# -*- coding: utf-8 -*-
import tensorflow as tf
#"2��3��2��ȵ���ά����"
t3d=tf.constant(
        [
        [[1,2],[4,5],[6,7]],
        [[8,9],[10,11],[12,13]]
        ],tf.float32
        )
session=tf.Session()
#"�ı���״Ϊ4��1��3��ȵ���ά����"
t1 = tf.reshape(t3d,[4,1,-1])
#"��ӡ���"
print(session.run(t1))