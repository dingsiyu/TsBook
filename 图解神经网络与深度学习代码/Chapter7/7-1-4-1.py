# -*- coding: utf-8 -*-
import tensorflow as tf
#"��������I"
I=tf.constant(
        [
         [[3],[4],[1],[5],[6]]
                ],tf.float32
        )
#"�����"
K=tf.constant(
        [
        [[-1]],[[-2]],[[2]],[[1]]
                ],tf.float32
        )
#"same���"
I_conv1d_K=tf.nn.conv1d(I,K,1,'SAME')
#"�����Ự"
session=tf.Session()
#"��ӡ���"
print(session.run(I_conv1d_K))