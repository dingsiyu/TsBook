# -*- coding: utf-8 -*-
import tensorflow as tf
#"1�� 3 �� 2 �����Ϊ 2 ������"
x=tf.constant(
        [
        [
         [[2,5],[3,3],[8,2]],
         [[6,1],[1,2],[5,4]],
         [[7,9],[2,3],[-1,3]]
                ]
                ],tf.float32
        )
#" 1�� 2 �� 2 �����Ϊ 2 �ľ����"
k=tf.constant(
        [
        [[[3],[1]],[[-2],[2]]],
        [[[-1],[-3]],[[4],[5]]]
                ],tf.float32
        )
#"ÿһ��ȷֱ������,Ȼ�����"
x_conv2d_k=tf.nn.conv2d(x,k,[1,1,1,1],'VALID')
#"�����Ự"
session=tf.Session()
#"��ӡ���"
print(session.run(x_conv2d_k))