# -*- coding: utf-8 -*-
import tensorflow as tf
#"��������"
x=tf.constant(
        [
        [
        [[1],[2],[3]],
        [[4],[5],[6]],
        [[7],[8],[9]]
        ]
        ],
        tf.float32
        )
# "ĳһ���� F �� sigma �ĵ���"
partial_sigma=tf.constant(
        [
        [
        [[-1],[-2],[1]],
        [[-3],[-4],[2]],
        [[-2],[1],[3]]
        ]
        ],tf.float32
        )
# "ĳһ���� F �� ����� k �ĵ���"
partial_sigma_k=tf.nn.conv2d_backprop_filter(x,(2,2,1,1),
                partial_sigma,[1,1,1,1],'SAME')
#"�����Ự"
session=tf.Session()
#"��ӡ���"
print(session.run(partial_sigma_k))