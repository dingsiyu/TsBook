# -*- coding: utf-8 -*-
import tensorflow as tf
#"�����"
kernel=tf.constant(
        [
        [[[3]],[[4]]],
        [[[5]],[[6]]]
        ],tf.float32
        )
# "ĳһ������ F �� sigma �ĵ���"
partial_sigma=tf.constant(
        [
        [
        [[-1],[1],[3]],
        [[2],[-2],[-4]],
        [[-3],[4],[1]]
        ]
        ],tf.float32
        )
# "���δ֪���������ķ������"
partial_x=tf.nn.conv2d_backprop_input((1,3,3,1),kernel,
            partial_sigma,[1,1,1,1],'SAME')
#"�����Ự"
session=tf.Session()
#"��ӡ���"
print(session.run(partial_x))