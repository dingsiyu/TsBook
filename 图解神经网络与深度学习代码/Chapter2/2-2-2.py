# -*- coding: utf-8 -*-
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import math
#"��ά����:�����е�ֵ������̬�ֲ���ƽ��ֵΪ10,��׼��Ϊ1���������"
sigma=1
mu=10
result=tf.random_normal([10,4,20,5],mu,sigma,tf.float32)
session=tf.Session()
#"Tensorת��Ϊndarray"
array=session.run(result)
#"����ά��ndarrayת��Ϊһά��ndarray"
array1d=array.reshape([-1])
#""���㲢��ʾֱ��ͼ""
histogram,bins,patch= plt.hist(array1d,25,facecolor='gray',
                      alpha=0.5,normed=True)
x=np.arange(5,15,0.01)
y=1.0/(math.sqrt(2*np.pi)*sigma)*
  np.exp(-np.power(x-mu,2.0)/(2*math.pow(sigma,2)))
plt.plot(x,y)
plt.show()