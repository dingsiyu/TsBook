# -*- coding: utf-8 -*-
import tensorflow as tf
#"1��������3�����3������"
x=tf.constant(
        [
         [[2,5,2],[6,1,-1],[7,9,-5]]
                ],tf.float32
        )
#"1��������2�����3�ľ����"
k=tf.constant(
        [
        [[-1],[5],[4]],[[2],[1],[6]]
                ],tf.float32
        )
#"һάsame���"
v_conv1d_k=tf.nn.conv1d(x,k,1,'SAME')
#"�����Ự"
session=tf.Session()
#"��ӡ���"
print(session.run(v_conv1d_k))