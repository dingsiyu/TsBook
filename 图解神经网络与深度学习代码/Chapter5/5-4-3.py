# -*- coding: utf-8 -*-
import tensorflow as tf
#"����"
x=tf.Variable(tf.constant([[2,1,3]],tf.float32))
w=tf.constant([[2],[3],[4]],tf.float32)
#"����g"
g=tf.matmul(x,w)
#"����f=relu(g)"
f=tf.nn.relu(g)
#"����f��(2,1,3)���ĵ���"
gradient=tf.gradients(f,[g,x])
session=tf.Session()
session.run(tf.global_variables_initializer())
#"��ӡ���"
print(session.run(gradient))