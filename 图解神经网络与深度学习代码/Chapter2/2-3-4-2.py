# -*- coding: utf-8 -*-
import tensorflow as tf
#"��ά����"
t4d=tf.constant(
        [
        #"��1�� ��2��3���2����ά����"
        [
        [[2,5],[3,3],[8,2]],
        [[6,1],[1,2],[5,4]]
        ],
        #"��2�� ��2��3���2����ά����"
        [
        [[1,2],[3,6],[1,2]],
        [[3,1],[1,2],[2,1]]
        ]
        ],tf.float32
        )
#"ת��Ϊ��Ϊ2�Ķ�ά����"
t2d=tf.reshape(t4d,[2,-1])
#t2d=tf.reshape(t4d,[-1,3*3*2])
#"�����Ự"
session=tf.Session()
#"��ӡ���"
print(session.run(t2d))