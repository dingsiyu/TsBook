# -*- coding: utf-8 -*-
import tensorflow as tf
#"��������"
X=tf.constant(
        [
        [
        [[2],[3],[8]],
        [[6],[1],[5]],
        [[7],[2],[-1]]
        ]
        ],tf.float32
        )
#"�����"
K=tf.constant(
        [
        [[[4]],[[1]]],
        [[[2]],[[3]]]
        ],tf.float32
        )
#"same���"
conv=tf.nn.conv2d(X,K,(1,1,1,1),'SAME')
session=tf.Session()
#"��ӡ���"
print(session.run(conv))