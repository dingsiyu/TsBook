# -*- coding: utf-8 -*-
import tensorflow as tf
#"3��4�еĶ�ά����"
t2=tf.constant(
        [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
        ],tf.float32
        )
#"��[0,1]λ�ÿ�ʼ,ȡ��2��2������"
t=tf.slice(t2,[0,1],[2,2])
#"�����Ự"
session=tf.Session()
#"��ӡ���"
print(session.run(t))