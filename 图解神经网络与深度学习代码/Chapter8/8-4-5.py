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
#" 3�� 2 �� 2 �����Ϊ 2 �ľ����"
k=tf.constant(
        [
        [[[3,1,-3],[1,-1,7]],[[-2,2,-5],[2,7,3]]],
        [[[-1,3,1],[-3,-8,6]],[[4,6,8],[5,9,-5]]]
                ],tf.float32
        )
#
#"ÿһ��ȷֱ������"
x_depthwise_conv2d_k=tf.nn.depthwise_conv2d(x,k,[1,1,1,1],'VALID')
#"�����Ự"
session=tf.Session()
#"��ӡ���"
print(session.run(x_depthwise_conv2d_k))