# -*- coding: utf-8 -*-
import tensorflow as tf
#"��ά����"
t=tf.constant([[1,3],[2,0]],tf.float32)
#"sigmod����"
result=tf.nn.sigmoid(t)
#"�����Ự"
session=tf.Session()