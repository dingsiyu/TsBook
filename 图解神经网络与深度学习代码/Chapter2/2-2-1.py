# -*- coding: utf-8 -*-
import tensorflow as tf
import matplotlib.pyplot as plt
#"��ά����:�����е�ֵ������Сֵ0�����ֵ10�ľ��ȷֲ��������"
x=tf.random_uniform([10,4,20,5],minval=0,maxval=10,dtype=tf.float32)
session=tf.Session()
#"Tensorת��Ϊndarray"
array=session.run(x)
#"Ϊ�˻���ֱ��ͼ,��arrayתΪ1��һά��ndarray"
array1d=array.reshape([-1])
plt.hist(array1d)
plt.show()