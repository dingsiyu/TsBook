# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
#"ռλ��"
x=tf.placeholder(tf.float32,[2,None],name='x')
# "3��2�о���"
w=tf.constant(
        [
        [1,2],
        [3,4],
        [5,6]
        ],tf.float32
        )
#"�������"
y=tf.matmul(w,x)
#"�����Ự"
session=tf.Session()
#"��xΪ2��2�еľ���"
result1=session.run(y,feed_dict={x:np.array([[2,1],[1,2]],np.float32)})
print(result1)
#"��xΪ2��1�еľ���"
result2=session.run(y,feed_dict={x:np.array([[-1],[2]],np.float32)})
print(result2)