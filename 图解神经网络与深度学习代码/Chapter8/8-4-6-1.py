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
#"1�� 2 �� 2 �����Ϊ 2 �ľ���� depthwiseFilter"
depthwise_filter=tf.constant(
        [
        [[[3],[1]],[[-2],[2]]],
        [[[-1],[-3]],[[4],[5]]]
                ],tf.float32
        )
# "1��1�����Ϊ2�ľ���� pointwiseFilter"
pointwise_filter=tf.constant(
        [
        [[[-1],[1]]],
        ],tf.float32
        )
#"������"
result=tf.nn.separable_conv2d(x,depthwise_filter,
                  pointwise_filter,[1,1,1,1],'VALID')
#"�����Ự"
session=tf.Session()
#"��ӡ���"
print(session.run(result))