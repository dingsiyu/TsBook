# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
#"�����:ÿһ�����밴�д洢"
x=tf.placeholder(tf.float32,(None,2))
#"��1���Ȩ�ؾ���"
w1=tf.constant(
        [
        [1,4,7],
        [2,6,8],
        ],tf.float32
        )
#"��1���ƫ��:"
b1=tf.constant([1,4,7],tf.float32)
#b1=tf.constant([[1,4,7]],tf.float32)#"����b1��������д"
#"�����һ����������"
l1=tf.matmul(x,w1)+b1
#"���� 2*x"
sigma1=2*l1
#"��2���Ȩ�ؾ���"
w2=tf.constant(
        [[2,3],
         [1,-2],
         [-1,1]],tf.float32
        )
#"��1���ƫ��"
b2=tf.constant(
        [5,-3],tf.float32
        )
#"�����2����������"
l2=tf.matmul(sigma1,w2)+b2
#"���� 2*x"
sigma2=2*l2
#"�����Ự"
session=tf.Session()
#"4������"
print(session.run(sigma2,{x:np.array([
                                     [10,11],
                                     [20,21],
                                     [30,31],
                                     [40,41]],np.float32)}))