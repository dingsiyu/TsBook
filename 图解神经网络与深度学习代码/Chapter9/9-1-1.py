# -*- coding: utf-8 -*-
import tensorflow as tf
#"������״Ϊ[1,4,4,1]������"
value2d = tf.constant(
        [
        #"��1��4��4��1��ȵ���ά����"
        [
        [[2],[3],[8],[-2]],
        [[6],[1],[5],[9]],
        [[7],[2],[-1],[8]],
        [[1],[4],[3],[5]]
                ]
                ],tf.float32
        )
#"���ػ�����"
value2d_maxPool=tf.nn.max_pool(value2d,(1,2,3,1),[1,1,1,1],'SAME')
#"�����Ự"
session=tf.Session()
#"��ӡ���"
print(session.run(value2d_maxPool))