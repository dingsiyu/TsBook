# -*- coding: utf-8 -*-
import tensorflow as tf
inputValue=tf.constant(
        [
        #"һ�������2 ��3��3�е�����"
        [
        [[2,5],[3,3],[8,2]],
        [[6,1],[1,2],[5,4]],
        [[7,9],[2,3],[-1,3]]
        ]
        ],tf.float32
        )

#"3�������2��Ϊ2��2 �еľ����"
kernels=tf.constant(
        [
        [[[3,1,-3],[1,-1,7]],[[-2,2,-5],[2,7,3]]],
        [[[-1,3,1],[-3,-8,6]],[[4,6,8],[5,9,-5]]]
        ],tf.float32
        )
#"valid���"
validResult=tf.nn.conv2d(inputValue,kernels,[1,1,1,1],'VALID')
#"�����Ự"
session=tf.Session()
#"��ӡ���"
print(session.run(validResult))