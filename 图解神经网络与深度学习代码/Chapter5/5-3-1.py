# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
#"�����"
x=tf.placeholder(tf.float32,(2,None))
#"��1���Ȩ�ؾ���"
w1=tf.constant(
        [[1,4,7],
        [2,6,8]],tf.float32
        )
#"��1���ƫ��"
b1=tf.constant(
        [
        [-4],
        [2],
        [1]
        ],tf.float32
        )
#"�����1����������"
l1=tf.matmul(w1,x,True)+b1
#"���� 2*x"
sigma1=2*l1
#"��2���Ȩ�ؾ���"
w2=tf.constant(
        [[2,3],
         [1,-2],
         [-1,1]
         ],tf.float32
        )
#"��2���ƫ��"
b2=tf.constant(
        [[5],[-3]],tf.float32
        )
#"�����1����������"
l2=tf.matmul(w2,sigma1,True)+b2
#"���� 2*x"
sigma2=2*l2
#"�����Ự"
session=tf.Session()
#"��x=[[3],[5]]"
print(session.run(sigma2,{x:np.array([[3],[5]],np.float32)}))