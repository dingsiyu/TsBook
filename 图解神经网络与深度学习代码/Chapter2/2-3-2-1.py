# -*- coding: utf-8 -*-
import tensorflow as tf
#"����Ϊ5��һά����"
t1=tf.constant([1,2,3,4,5],tf.float32)
#"��t1�ĵ�1��λ�ÿ�ʼ,ȡ����Ϊ3������"
t=tf.slice(t1,[1],[3])
#"�����Ự"
session=tf.Session()
#"��ӡ���"
print(session.run(t))