# -*- coding: utf-8 -*-
import tensorflow as tf
#"�����"
kernel=tf.constant(
        [
        [[[3]],[[4]]],
        [[[5]],[[6]]]
        ],tf.float32
        )
#"ĳһ������� sigma �ĵ���"
out=tf.constant(
        [
        [
        [[-1],[1]],
        [[2],[-2]]
        ]
        ],tf.float32
        )
#"���δ֪�����ĵ����ķ������"
inputValue=tf.nn.conv2d_backprop_input((1,3,3,1),
                kernel,out,[1,1,1,1],'VALID')
#"�����Ự"
session=tf.Session()
print(session.run(inputValue)