# -*- coding: utf-8 -*-
import tensorflow as tf
#"һά����"
t=tf.constant([1,2,3],tf.float32)
#"�����Ự"
session=tf.Session()
#"����ת��Ϊndarray"
array=session.run(t)
#"��ӡ�����ݽṹ���ͼ���Ӧֵ"
print(type(array))
print(array)