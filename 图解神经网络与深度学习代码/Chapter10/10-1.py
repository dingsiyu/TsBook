# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
#"��������"
input_tensor=tf.placeholder(tf.float32,[None,3,3,2])
#"3�� ��2��2���2�ľ����"
kernel=tf.constant(
        [
        [ [ [-1,1,0],[1,-1,-1] ],[ [0,0,-1],[0,0,0] ] ],
        [ [ [0,0,0],[0,0,1] ], [ [1,-1,1],[-1,1,0] ]  ]
        ],tf.float32
        )
#"���"
conv2d=tf.nn.conv2d(input_tensor,kernel,(1,1,1,1),'SAME')
#"ƫ��"
bias=tf.constant([1,2,3],tf.float32)
conv2d_add_bias=tf.add(conv2d,bias)
#"�����"
active=tf.nn.relu(conv2d_add_bias)
#"pool����"
active_maxPool=tf.nn.max_pool(active,(1,2,2,1),(1,1,1,1),'VALID')
#"����"
shape=active_maxPool.get_shape ()
num=shape[1].value*shape[2].value*shape[3].value
flatten=tf.reshape(active_maxPool,[-1,num])
#flatten=tf.contrib.layers.flatten(active_maxPool)
#"��ӡ���"
session=tf.Session()
print(session.run(flatten,feed_dict={
        input_tensor:np.array([
                         #"��1�� 3��3��2��ȵ���ά����"
                         [
                         [[2,5],[3,3],[8,2]],
                         [[6,1],[1,2],[5,4]],
                         [[7,9],[2,8],[1,3]]
                         ],
                         #"��2�� 3��3��2��ȵ���ά����"
                         [
                         [[1,2],[3,6],[1,2]],
                         [[3,1],[1,2],[2,1]],
                         [[4,5],[2,7],[1,2]]
                         ],
                         #"��3�� 3��3��2��ȵ���ά����"
                         [
                         [[2,3],[3,2],[1,2]],
                         [[4,1],[3,2],[1,2]],
                         [[1,0],[4,1],[4,3]]
                         ],
                         ],np.float32)}))