# -*- coding: utf-8 -*-
import tensorflow as tf
#"��ά����"
t=tf.constant(
        [
        [1,2,3],
        [4,5,6]
        ],
        tf.float32
        )
#"�����ĳߴ�"
#s=t.shape
s=t.get_shape()
#"��ӡs�������ݽṹ����"
print("'s��ֵ:'")
print(s)
print("'s �����ݽṹ����:'")
print(type(s))
print("'s[0]��ֵ:'")
print(s[0])
#"��ӡs[0]�������ݽṹ����"
print("'s[0]�����ݽṹ����:'")
print(type(s[0]))
#"�� s[0] ת��Ϊ������"
print("'��s[0]��ֵת��Ϊ������:'")
print(s[0].value)
print(type(s[0].value))