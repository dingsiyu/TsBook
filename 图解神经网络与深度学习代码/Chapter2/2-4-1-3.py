# -*- coding: utf-8 -*-
import tensorflow as tf
#"��ά����"
x=tf.constant(
        [
        #"��1��2��2��2��ȵ���ά����"
        [
        [[2,5],[4,3]],
        [[6,1],[1,2]]
        ],
        #"��2��2��2��2��ȵ���ά����"
        [
        [[3,9],[5,7]],
        [[7,5],[2,6]]
        ]
        ],tf.float32
        )
#"����Ϊ2��һά����"
y=tf.constant([10,20],tf.float32)
#"�ӷ�����"
result=tf.add(x,y)
#"�����Ự����ӡ���"
session=tf.Session()
print(session.run(result))