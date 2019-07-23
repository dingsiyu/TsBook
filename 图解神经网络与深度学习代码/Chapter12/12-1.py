# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
#"x��1��3��3�����1������"
x=tf.placeholder(tf.float32,(1,3,3,1))
#"2x2������,������(1,1,1,1)��VALIDƽ��ֵ�ػ�����"
sigma=tf.nn.avg_pool(x,(1,2,2,1),(1,1,1,1),'VALID')
#"���������ػ������Ľ��������һ������F:�ػ�����ĺ�"
F=tf.reduce_sum(sigma)
#"�����Ự"
session=tf.Session()
#"�ֱ���� F ��ĳһ�� xvalue �� ��� sigma �� x ���ݶ�"
xvalue=np.random.randn(1,3,3,1)
grad=tf.gradients(F,[sigma,x])
results=session.run(grad,{x:xvalue})
#"��ӡ���"
print("----���sigma���ݶ�----:")
print(results[0])
print("----���x���ݶ�----:")
print(results[1])